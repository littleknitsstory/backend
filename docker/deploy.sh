#!/usr/bin/env bash

set -e;

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/.."

image_tag="latest";
image_full_name="63phc/lks:$image_tag";

echo "Building image '$image_full_name'";
docker build . -t "$image_full_name";

echo "Authenticating";
echo "$DOCKER_PASS" | docker login -u="$DOCKER_USERNAME" --password-stdin;

echo "Pushing image '$image_full_name'";
docker push "$image_full_name";
echo "Push finished!";

exit 0;
