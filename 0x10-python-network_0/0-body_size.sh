#!/bin/bash
# Take URL as argument
url=$1

# Send GET request using curl and store the response body in a variable
response=$(curl -sS "$url")

# Get the size of the response body in bytes using the "wc" command and display it
echo -n "$response" | wc -c
