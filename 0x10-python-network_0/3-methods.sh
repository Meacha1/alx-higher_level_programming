#!/bin/bash
# Send OPTIONS request to URL and display allowed methods
curl -s -I -X OPTIONS "$1" | grep "Allow" | cut -d " " -f2-

