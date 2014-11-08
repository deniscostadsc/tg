#!/bin/bash

cd $(dirname $0)

dev_appserver.py \
    --show_mail_body \
    --datastore_path=dev.sqlite3 . \
    --blobstore_path=~/blob
