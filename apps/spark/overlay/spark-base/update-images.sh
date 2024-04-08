#!/bin/bash

# USAGE: sh ./update-images.sh OLD_TAG NEW_TAG

docker exec -it $(kind get clusters | head -1)-worker2 crictl rmi natandias1/spark-base:$1
docker exec -it $(kind get clusters | head -1)-worker crictl rmi natandias1/spark-base:$1
docker exec -it $(kind get clusters | head -1)-control-plane crictl rmi natandias1/spark-base:$1

#Load new image

kind load --name=local-kind-cluster docker-image natandias1/spark-base:$2
