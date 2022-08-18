#!/bin/bash
# bash script that prints the content length in bytes
curl -sI "$1" | grep Content-Length | awk '{print $2}'
