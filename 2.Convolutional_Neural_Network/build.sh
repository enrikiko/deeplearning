#!/usr/bin/env bash
DIR=$(basename $PWD |  tr '[:upper:]' '[:lower:]')
docker build -t $DIR .
docker run -it --rm  -p 3000:3000 --name $DIR $DIR bash
#docker exec -it $DIR bash
