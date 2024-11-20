Here is a step-by-step guide to install Weaviate, check if it's running, and verify its functionality:
Step 1: Install Weaviate

You can run Weaviate locally using Docker or use a hosted version. Below, we focus on the Docker installation.
1.1 Install Docker
==================

    Download and install Docker:
        Windows/Mac: Docker Desktop
        Linux: Install Docker via your package manager (apt, yum, etc.).

    Verify installation:

    docker --version

1.2 Download and Run Weaviate
================================

    Create a docker-compose.yml file for Weaviate. You can use the following configuration:

    version: '3.4'
    services:
      weaviate:
        image: semitechnologies/weaviate:latest
        ports:
          - "8080:8080"
        environment:
          QUERY_DEFAULTS_LIMIT: 100
          AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: 'true'
          PERSISTENCE_DATA_PATH: "./data"
          DEFAULT_VECTORIZER_MODULE: "none" # Change this to "text2vec-openai" for OpenAI integration
          ENABLE_MODULES: "none"           # Change to enable modules like "text2vec-transformers"
    
        Start the server:
    
    docker-compose up -d
    
    Check if the container is running:
    
        docker ps

    The output should show a container named something like weaviate_weaviate.

Step 2: Check if Weaviate is Running
=====================================

Once Weaviate is running, you can check its status.

2.1 Use the Ready Endpoint
===========================

Send a GET request to the /.well-known/ready endpoint:

Command:
=========

        curl http://localhost:8080/v1/.well-known/ready

Expected Response:
===================

    {
      "status": "ok"
    }

This indicates that the server is ready to process requests.

2.2 Check Logs
=================

If you don't see status: ok, check the logs for errors:

    docker logs weaviate_weaviate

Step 3: Interact with Weaviate
===============================

Once the server is running, you can interact with it using REST API, GraphQL, or the Python client.

3.1 Explore the Schema
========================

    Check the schema to verify if Weaviate is up:

curl http://localhost:8080/v1/schema

Expected Response: If the schema is empty:

    {
      "classes": []
    }

3.2 Open GraphQL Console
==========================

    Open the browser at: http://localhost:8080/console
    You can run GraphQL queries to verify the setup.

3.3 Test with Python Client
============================

    Install the Python client:

pip install weaviate-client

Connect to Weaviate and check readiness:

    import weaviate

    # Connect to the Weaviate instance
    client = weaviate.Client("http://localhost:8080")

    # Check if the server is ready
    if client.is_ready():
        print("Weaviate is up and running!")
    else:
        print("Weaviate is not reachable.")

Step 4: (Optional) Configure Vectorizer Modules
================================================

If you want to use prebuilt vectorization modules (e.g., OpenAI, Hugging Face transformers), update the docker-compose.yml file.
Example for OpenAI Integration:

Add the following lines under the environment section:
    
    DEFAULT_VECTORIZER_MODULE: "text2vec-openai"
    ENABLE_MODULES: "text2vec-openai"
    OPENAI_APIKEY: "your-openai-api-key"

Restart the container:

    docker-compose down
    docker-compose up -d

Step 5: Test Adding and Retrieving Data
========================================

      Example:
      
      Use Python to test adding a document and performing a search:
      
      import weaviate
      
      client = weaviate.Client("http://localhost:8080")
      
      # Add a schema
      client.schema.create_class({
          "class": "Document",
          "description": "A class for storing documents",
          "properties": [
              {"name": "content", "dataType": ["string"]}
          ]
      })
      
      # Add a document with a vector
      client.data_object.create(
          data_object={"content": "This is a test document."},
          class_name="Document",
          vector=[0.1, 0.2, 0.3, 0.4]
      )
      
      # Search for a similar vector
      result = client.query.get("Document", ["content"]) \
          .with_near_vector({"vector": [0.1, 0.2, 0.3, 0.4]}) \
          .do()
      
      print(result)
