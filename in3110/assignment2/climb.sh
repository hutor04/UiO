#!/bin/bash

function climb {
counter=$1
if [ "$1" = "" ]; then
    echo "Provide the number of directories to jump up"
else
  while [ "$counter" != "0"  ];do
    cd ..
    counter=$((counter-1))
  done
fi
}
