import weaviate

# Connect to the Weaviate instance
client = weaviate.Client("http://localhost:8080")

# Check if the server is ready
if client.is_ready():
    print("Weaviate is up and running!")
else:
    print("Weaviate is not reachable.")



#Add a schema
client.schema.create_class({
    "class": "Document",
    "description": "A class for storing documents",
    "properties": [
        {"name": "content", "dataType": ["string"]}
    ]
})

# # Add a document with a vector
client.data_object.create(
    data_object={"content": "First Vector DB Insertion."},
    class_name="Document10",
    vector=[0.1, 0.2, 0.3, 0.4]
)

# Search for a similar vector
result = client.query.get("Document10", ["content"]) \
    .with_near_vector({"vector": [0.1, 0.2, 0.3, 0.4]}) \
    .do().values()

print(result)
    