To stop an active Docker build that's currently running, you can use these methods:

1. Press `Ctrl+C` in the terminal where the build is running. This sends a SIGINT signal to interrupt the process.

2. If that doesn't work or you started the build in the background, find the Docker process ID and kill it:
   ```bash
   docker ps -a  # Find the container ID
   docker kill <container-id>
   ```

3. For a build process specifically:
   ```bash
   docker system events  # In a separate terminal to see the build process
   ```
   Then in another terminal:
   ```bash
   docker builder prune --force
   ```

4. If you're using Docker Desktop, you can also try stopping the build from the Dashboard interface by clicking on the "Stop" button next to the running build.

If you have multiple builds running simultaneously and need to stop all Docker activities:
```bash
docker system prune --force
```

Would you like me to explain any of these methods in more detail?
