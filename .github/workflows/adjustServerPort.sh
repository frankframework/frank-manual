#!/bin/bash
#
# Update the port of baseUrl in cypress.config.ts
#
export fileName=$1
export port=$2

sed -i "s|://localhost|://localhost:${port}|g" ${fileName}