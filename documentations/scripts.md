# Scripts Documentation

## build_and_push.py

Builds a Docker image from a given folder and pushes it to Docker Hub under the `natandias1/` org. The image name is derived from the folder name. Accepts the folder path as a CLI argument.

```bash
python scripts/build_and_push.py webserver-example
# Builds and pushes natandias1/webserver-example:latest
```

---

## docker_hub_tags.py

Fetches the 10 most recently pushed tags for a Docker Hub image and prints them as JSON, including name, status, and last push date.

```bash
python scripts/docker_hub_tags.py -r natandias1 -i webserver-example
```

---

## python_auto_pr_approve.py

Auto-approves a GitHub pull request when it touches specific files. Reads the repo and PR number from environment variables and uses a bot account (`natan-bot`) to submit the approval via PyGithub.

Requires env vars: `GH_TOKEN`, `GITHUB_REPOSITORY`, `PULL_REQUEST_NUMBER`.

```bash
GH_TOKEN=ghp_... GITHUB_REPOSITORY=natandias/my-devops-repo PULL_REQUEST_NUMBER=42 \
  python scripts/python_auto_pr_approve.py
```

---

## kustomize_build_filters.py

Runs `kustomize build` on a given path and filters the output to resources matching a specific name and kind. Prints the matching YAML and reports any requested kinds that were not found.

```bash
python scripts/kustomize_build_filters.py -p infra/redis -n redis -k Deployment -k Service
```
