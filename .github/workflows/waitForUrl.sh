#!/bin/bash

url=$1
numTries=$2
triesSoFar=0
result=1000
while [[ ${triesSoFar} -le ${numTries} ]]; do
  let triesSoFar++
  curl -s -I -L -o curlOutput.txt ${url}
  result=$?
  if [[ ${result} -eq 0 ]]; then
    echo "Curl returned 0"
    grep -E "^HTTP/" curlOutput.txt | tail -1 | cut -d" " -f2 > httpStatusCode.txt
    result=$?
    if [[ ${result} -eq 0 ]]; then
      echo "Found HTTP status code: $(cat httpStatusCode.txt)"
      grep -E "2[0-9]{2}" httpStatusCode.txt
      result=$?
      if [[ ${result} -eq 0 ]]; then
        echo "HTTP response is successful"
        break;
      else
        sleep 1
      fi
    else
      sleep 1
    fi
  else
    sleep 1
  fi
done
# We want to see the output of this command only once
curl ${url}
result=$?
echo "Curl return code: ${result}"
exit ${result}
