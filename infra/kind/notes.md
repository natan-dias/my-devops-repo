# Some notes

## PVC stuck in terminate state

> kubectl patch pvc {PVC_NAME} -p '{"metadata":{"finalizers":null}}'

## Check images inside node

> docker exec -it $(kind get clusters | head -1)-worker crictl images

### Remove images

> docker exec -it $(kind get clusters | head -1)-worker2 crictl rmi IMAGE TAG

## Apply Ingress controller

> kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

## Load images

> kind load --name=local-kind-cluster docker-image apache/spark:3.5.1

## List images

> docker exec -it $(kind get clusters | head -1)-control-plane crictl images

## Deploy Metrics Server

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.7.1/components.yaml

kubectl patch -n kube-system deployment metrics-server --type=json -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'

