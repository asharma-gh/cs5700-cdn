#!/bin/bash

mkdir www
while read LINE; do
    curl --raw -sD - http://ec2-54-166-234-74.compute-1.amazonaws.com:8080/$LINE > www/"$(echo -n "/$LINE" | sha256sum | head -c 64)"
    if [ "$(du www/ | grep -o [0-9]*)" -gt 7680 ]; then
        rm www/$(echo -n "/$LINE" | sha256sum | head -c 64)
        break
    fi
done < pre-cache.txt

touch .cache_done
echo "Done downloading pre-cache"
