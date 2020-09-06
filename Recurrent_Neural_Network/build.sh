#!/usr/bin/env bash
DIR=$(basename $PWD |  tr '[:upper:]' '[:lower:]')
docker build -t $DIR .
docker run -it --rm --name $DIR $DIR bash
#docker exec -it $DIR bash
