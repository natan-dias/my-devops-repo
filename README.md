[![CI](https://github.com/natan-dias/my-devops-repo/actions/workflows/ci.yaml/badge.svg)](https://github.com/natan-dias/my-devops-repo/actions/workflows/ci.yaml) [![Release Image to Docker Hub](https://github.com/natan-dias/my-devops-repo/actions/workflows/release.yml/badge.svg)](https://github.com/natan-dias/my-devops-repo/actions/workflows/release.yml) [![codecov](https://codecov.io/gh/natan-dias/my-devops-repo/graph/badge.svg?token=GSHQHG9UAD)](https://codecov.io/gh/natan-dias/my-devops-repo)

# my-devops-repo

A personal DevOps repository for building, deploying, and managing containerized applications on Kubernetes. Includes CI/CD automation, Docker image definitions, Kubernetes infrastructure manifests, and application code.

## Repository Structure

```
.
├── .github/workflows/   # GitHub Actions CI/CD pipelines
├── apps/                # Application source code
├── argocd-deploys/      # ArgoCD Application manifests
├── images/              # Docker image definitions
├── infra/               # Kubernetes infrastructure manifests (Kustomize)
└── scripts/             # Automation and utility scripts
```

## Workflows

| Workflow | Trigger | Description |
|---|---|---|
| **CI** | Pull Request → `main` | Detects Dockerfile changes, builds the image, and pushes it to Docker Hub tagged with the Dockerfile content hash |
| **Release** | Manual (`workflow_dispatch`) | Builds and pushes a Docker image to Docker Hub with a specified release tag |
| **Codecov** | Pull Request | Runs test suite and uploads coverage report to Codecov |
| **PR Auto-Approval** | Pull Request | Auto-approves PRs opened by the repository owner |

## Applications (`apps/`)

| App | Description |
|---|---|
| `basic-python-api` | Minimal Python HTTP API |
| `basic-video-store-api-with-db` | Flask API with SQLite, simulating a video store |
| `kb-api` | Knowledge Base REST API — manages commands and notes in a structured database |

## Docker Images (`images/`)

| Image | Base | Description |
|---|---|---|
| `spark-base` | `openjdk:11.0.11-jre-slim-buster` | Apache Spark 3.5.1 base image (master/worker) |
| `spark-executor` | `natandias1/spark-base` | Spark executor for Kubernetes |
| `webserver-example` | `nginx:latest` | Nginx server serving a sample web page |
| `sql-database` | `mysql:9.3.0` | MySQL database with environment-based configuration |

## Infrastructure (`infra/`)

| Stack | Tool | Description |
|---|---|---|
| `argocd` | Kustomize | ArgoCD GitOps controller |
| `hashicorp-vault` | Kustomize + Helm | HashiCorp Vault for secrets management |
| `redis` | Kustomize | Redis in-memory cache |
| `spark` | Kustomize | Apache Spark cluster on Kubernetes |
| `webserver-example` | Kustomize | Nginx ingress example |
| `knowledge-base-app` | Kubernetes | PostgreSQL deployment for the KB API |

## ArgoCD Applications (`argocd-deploys/`)

ArgoCD Application definitions that sync the `infra/` manifests to the cluster:
- `argo-redis` — deploys `infra/redis`
- `argo-spark` — deploys `infra/spark/overlay/spark-base`

## Scripts (`scripts/`)

| Script | Description |
|---|---|
| `build_and_push.py` | Builds and pushes a Docker image by folder name |
| `docker_hub_tags.py` | Lists Docker Hub image tags for a repository |
| `python_auto_pr_approve.py` | Approves PRs via GitHub API |
| `kustomize_build_filters.py` | Utility for Kustomize operations |
