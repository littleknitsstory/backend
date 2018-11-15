#!/usr/bin/env bash

set -e;

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#cd "$DIR/$BUILD_ENV/backend"

image_tag="latest";
image_full_name="$DOCKER_REPO:$image_tag";

echo "Building image '$image_full_name'";
docker build -t "$image_full_name" -f "$DIR/$BUILD_ENV/backend/Dockerfile" .;

echo "Authenticating";
echo "$DOCKER_PASS" | docker login -u="$DOCKER_USERNAME" --password-stdin;

echo "Pushing image '$image_full_name'";
docker push "$image_full_name";
echo "Push finished!";

exit 0;
