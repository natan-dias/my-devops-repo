# This Python script monitors a folder for changes in the Dockerfile, then builds a Docker image 
# based on the folder's name and pushes it to a repository

import os
import subprocess
import sys

# Define the folder to monitor
#folder_path = "/path/to/your/folder"

# Function to check for changes in Dockerfile
#def check_dockerfile_change():
#    dockerfile_path = os.path.join(folder_path, "Dockerfile")
#    if os.path.exists(dockerfile_path):
#        # Check for changes in Dockerfile
#        # You can implement your own logic to detect changes here
#        return True
#    return False

# Function to build and push Docker image
def build_and_push_image(folder_path):
    folder_name = os.path.basename(folder_path)
    image_name = f"natandias1/{folder_name}:latest"
    
    # Build Docker image
    print("Building Docker image...")
    subprocess.run(["docker", "build", "-t", image_name, folder_path])
    
    # Push Docker image to repository
    print("Pushing Docker image...")
    subprocess.run(["docker", "push", image_name])

# Main function
def main():
    if len(sys.argv) < 2:
        print("Please provide the affected folder as a command-line argument.")
        return
    
    affected_folder = sys.argv[1]
    folder_path = f"/images/{affected_folder}"
    
    build_and_push_image(folder_path)

if __name__ == "__main__":
    main()