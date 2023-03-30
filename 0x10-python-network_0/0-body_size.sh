#!/bin/bash
# Take URL as argument
url=$1 | response=$(curl -sS "$url") | echo -n "$response" | wc -c
