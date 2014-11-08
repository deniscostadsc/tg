#!/bin/bash

cd $(dirname $0)

if [[ -z $VIRTUAL_ENV ]]; then
    echo "You should start your virtualenv to setup the project!"
    exit 1
fi

# Create a syslink to be able to upload libs to appengine
ln -s $VIRTUAL_ENV/lib/python?.?/site-packages lib
