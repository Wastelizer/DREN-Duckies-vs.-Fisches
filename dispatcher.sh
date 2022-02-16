#!/bin/bash

CONTAINER="repro"

#build docker container
docker build -t $CONTAINER .


#run docker container interactive mode
docker run --entrypoint ./entrypoint.sh $CONTAINER 

#copy paper out of container
CONTAINER_NAME="$(docker ps -l --format "{{.Names}}")"
docker cp $CONTAINER_NAME:home/repro/paper/Repro_Paper.pdf ./paper/Repro_Paper.pdf
