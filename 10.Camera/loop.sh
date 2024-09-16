#!/bin/bash

dir=$(pwd)
while true; 
  do
  git pull
  for i in `seq 1 100`
  do 
    python $dir/send.sh 
    sleep 1
  done
done

