# Hashicorp Vault Installation

## Namespace and certs

Create namespace vault

Add new certificates (this example just add a self-signed one)

```
openssl req -newkey rsa:2048 -keyout certs/domain.key -out certs/domain.csr

openssl x509 -signkey certs/domain.key -in certs/domain.csr -req -days 365 -out certs/domain.crt
```

Add them to .gitignore to now push self signed certificates to git


## Helm

helm repo add hashicorp https://helm.releases.hashicorp.com

helm install vault hashicorp/vault --set “server.dev.enabled=true”

### First initialization

```
kubectl exec -it POD-NAME -- vault operator init

kubectl exec -it POD-NAME -- vault operator unseal
```

> Need to unseal 3 times using the tokens provided by the init command

## Deploy ingress using kustomize

> kustomize build | kubectl apply -f -



