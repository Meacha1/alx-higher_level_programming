#!/bin/bash
# Script to send a GET request to a URL and display the response body
curl -s -o /dev/null -w "%{http_code}\n" $1 | grep -q 200 && curl -s $1
