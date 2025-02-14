import yaml
import subprocess

# Define the path to the kustomization file
kustomization_path = "PATH"

# Run kustomize build with the specified path
output = subprocess.check_output(["kustomize", "build", kustomization_path])

# Parse the YAML output
resources = yaml.safe_load_all(output)

# Iterate over the resources and find the desired one
for resource in resources:
    if resource["kind"] == "Deployment" and resource["metadata"]["name"] == "DEPLOY":
        print(yaml.dump(resource))
        break