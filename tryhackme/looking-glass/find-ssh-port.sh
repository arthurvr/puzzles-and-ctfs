#!/bin/bash

IP=10.10.230.117

LOWER_PORT=9000
HIGHER_PORT=13783

function search() {
  PORT=$(($LOWER_PORT + ($HIGHER_PORT - $LOWER_PORT - 1) / 2))
  echo "Trying $PORT"

  result="$(ssh -o StrictHostKeyChecking=no root@$IP -p $PORT)"

  echo $result

  if echo $result | grep -q 'Lower'; then
    echo "Lower!!"
    LOWER_PORT=$PORT
    search
  elif echo $result | grep -q 'Higher'; then
    echo "Higher!!"
    HIGHER_PORT=$PORT
    search
  else
    echo "This port!!"
  fi
}

search
