#!/bin/bash

kubectl create --save-config namespace spark

kustomize build | kubectl apply -f -