I'll help you create a simple program to run from Docker. Let's build a basic example that you can easily customize later.

<antArtifact identifier="docker-hello-world" type="application/vnd.ant.code" language="dockerfile" title="Basic Docker Hello World">
# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY app.py .

# Run the script when container launches
CMD ["python", "app.py"]
</antArtifact>

<antArtifact identifier="python-app" type="application/vnd.ant.code" language="python" title="Simple Python App">
# app.py

    import time
    def main():
        print("Hello from Docker container!")
        print("This is a simple Python application running in a container")
        
        # Counter to show the app is running
        counter = 1
        while True:
            print(f"Container has been running for {counter} seconds")
            time.sleep(1)
            counter += 1
    
    if __name__ == "__main__":
        main()
</antArtifact>

To build and run this Docker container:

1. Create two files in the same directory:
   - `Dockerfile` (with the content from the first code block)
   - `app.py` (with the content from the second code block)

2. Build the Docker image:
   ```bash
   docker build -t simple-python-app .
   ```

3. Run the container:
   ```bash
   docker run simple-python-app
   ```

This will start a container that prints a greeting message and then counts seconds. To stop it, press `Ctrl+C`.

If you want to run the container in the background:
```bash
docker run -d --name my-python-app simple-python-app
```

And to see the logs:
```bash
docker logs -f my-python-app
```

Would you like me to modify this example or create something more specific?
