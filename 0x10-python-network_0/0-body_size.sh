#!/bin/bash
# script that request and display the size of the body of that response
# with the flag -I, we obtain only headers
# with the flag -s, we disable the progression display
# with the grep, we filter the output, in order that it only show the content
# with the awk, we filter the content of the length, so we only get the number
curl -sI "$1" | grep Content-Length | awk '{print $2}'
