# Spark Iceberg deployment

## Deployment structure

Using Kustomize to build and deploy for now. Base has only the namespace. And for now two overlays with slightly different deployments. One using a base custom image from Tabulario, and another one build my own image with JDK 11.

## Remarks

I had an issue with deployment names, which can be followed on this [GitHub Issue](https://github.com/big-data-europe/docker-spark/issues/128) and this [Medium Article](https://medium.com/@varunreddydaaram/kubernetes-did-not-work-with-apache-spark-de923ae7ab5c) explaining why we cant name k8s deployment for Spark as spark-master.

## Base article for build

The base article I got for this deployment:

- [Creating a Spark Standalone Cluster with Docker and docker-compose](https://dev.to/mvillarrealb/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-2021-update-6l4)
- [Spark and Iceberg Quickstart](https://iceberg.apache.org/spark-quickstart/)

## Some cool scripts

- start.sh

Both ovewrlays can be deployed by just using the **start.sh** script on its folders. The **spark-base** overlay has a small logic to apply annotation, if defined during your call to the start script. 

- fake-certificates.sh

Just a small script to create fake certificates to use in you ingress, if you want to test port 443.

- update-images.sh

I am testing using [Kind](https://kind.sigs.k8s.io/) so you can update images on your kind cluster, if you are testing locally and still didn't push the new images to a registry.

## Quick Tests

In order to test this spark instance, just go to **spark-test** folder and copy the spark submit content. You will need to connect with your worker instance and run spark-submit from there. In this test, a small aplication to display the value of PI runs.

## To do

- Test spark-subimt with K8s API