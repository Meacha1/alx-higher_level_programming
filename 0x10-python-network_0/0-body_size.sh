#!/bin/bash
# Take URL as argument
grl=$1 && response=$(curl -sS "$url") && echo -n "$response" | wc -c
