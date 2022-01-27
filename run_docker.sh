#!/bin/bash

CONTAINER="repro"

#build docker container
docker build -t $CONTAINER .

#run docker container interactive mode
docker run -it $CONTAINER
