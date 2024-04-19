#!/bin/bash

# USAGE: sh ./update-images.sh IMAGE-NAME OLD_TAG NEW_TAG

docker exec -it $(kind get clusters | head -1)-worker2 crictl rmi $1:$2
docker exec -it $(kind get clusters | head -1)-worker crictl rmi $1:$2
docker exec -it $(kind get clusters | head -1)-control-plane crictl rmi $1:$2

#Load new image

kind load --name=local-kind-cluster docker-image $1:$3
