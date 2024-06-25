#!/bin/bash

namespace="spark"

echo "CHECK IF NAMESPACE $namespace EXISTS"

if kubectl get namespace $namespace; then
    echo "NAMESPACE $namespace EXISTS"
else
    kubectl create --save-config namespace $namespace
fi

echo "ANNOTATE CHANGE CAUSE REVISION | TAG TO APPLY: $1"

export revision_tag="$1"

kustomize build | kubectl apply -f -

deployments=$(kubectl get deploy -o=jsonpath='{.items[*].metadata.name}')
for deployment in $deployments; do
  kubectl annotate deploy $deployment kubenetes.io/change-cause="$revision_tag"
  echo "ANNOTATED $deployment"
done