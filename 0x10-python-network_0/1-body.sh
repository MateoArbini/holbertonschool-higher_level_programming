#!/bin/bash
# -s --> option to disable the progression display
# -L --> option to follow all redirects
# Get is the request method
# $1 is the element we are taking to display
curl -sL GET "$1"
