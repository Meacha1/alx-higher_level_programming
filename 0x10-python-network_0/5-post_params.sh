#!/bin/bash
# Send POST request with email and subject variables and display response body
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -H "Content-Type: application/x-www-form-urlencoded" -H "X-School-User-Id: 98" -s "$1"
