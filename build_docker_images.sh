#!/usr/bin/env bash

# Changing the build context arg depending on where you're running this from.
# End result is that the build context is the same and light weight

if [ ${0%/*} = ${0##*/} ]; then
  # Building base docker image
  docker build . -f Dockerfiles/Dockerfile_selenium-ff -t selenium-ff

  # Building final docker image
  docker build . -f Dockerfiles/Dockerfile_skedda -t skedda
else
  # Building base docker image
  docker build ${0%/*} -f ${0%/*}\/Dockerfiles/Dockerfile_selenium-ff -t selenium-ff

  # Building final docker image
  docker build ${0%/*} -f ${0%/*}\/Dockerfiles/Dockerfile_skedda -t skedda
fi

