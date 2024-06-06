#!/bin/bash

export currentFrankConfig=$1

export frankConfigsIafUtilAllowed=" \
    frank-manual/srcSteps/NewHorizons/v510
    frank-manual/src/deploymentTomcat"

# Copied from StackOverflow - checks whether ${currentFrankConfig}
# is in ${frankConfigsIafUtilAllowed} and returns 0 in this case.
echo ${frankConfigsIafUtilAllowed} | grep -w -q ${currentFrankConfig}
if [ $? == 0 ]; then
  export result="AllowIafUtilWarning"
else
  export result="NoWarnings"
fi
echo "${result}"
echo "expectedBehaviorTag=${result}" >> $GITHUB_OUTPUT