# ArgoCD Local deployment

## Get admin password

> kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo