#!/bin/bash
#script that shows the status code response
curl -so dev/null -w "%{http_code}" "$1"
