#!/bin/bash

TAG=1.0.2

IMAGE=spark-executor

set -euo pipefail

docker build -t natandias1/${IMAGE}:${TAG} -f ./Dockerfile .

if [ $? -eq "--push" ]; then
    docker push natandias1/${IMAGE}:${TAG}
fi