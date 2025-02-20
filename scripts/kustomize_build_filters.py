import yaml
import subprocess
import argparse

DEFAULT_KINDS = ["Deployment", "Service", "Ingress", "Job", "CronJob", "StatefulSet", "DaemonSet", "Pod", "ConfigMap", "Secret", "ServiceAccount", "Role", "RoleBinding", "ClusterRole"]

def kustomize_build_filter(path, name, kinds=None):

    try:
        output = subprocess.check_output(["kustomize", "build", path])
    except subprocess.CalledProcessError as e:
        print(f"Error running kustomize build: {e}")
        return

    resources = yaml.safe_load_all(output)

    if kinds is None or kinds == []:
        kinds = DEFAULT_KINDS

    found_kinds = set()
    for resource in resources:
        if resource["metadata"]["name"] == name and resource["kind"] in kinds:
            print(yaml.dump(resource))
            found_kinds.add(resource["kind"])

    for kind in kinds:
        if kind not in found_kinds:
            print(f"Error: Resource kind '{kind}' not found for name '{name}'")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to the kustomization file")
    parser.add_argument("--name", "-n", type=str, required=True, help="Name of the resource")
    parser.add_argument("--kind", "-k", type=str, action="append", help="Kind of the resource")

    args = parser.parse_args()

    kustomize_build_filter(args.path, args.name, args.kind)