#!/bin/bash
set -e
RED='\033[0;31m'
YLW='\033[1;33m'
CYN='\033[1;36m'
NCL='\033[0m'

if [ ! -d "$1" ]
then
    echo -e "${RED}Path \"$1\" does not exist$NCL"
    echo -e "${YLW}Usage: check.sh PATH [EXCLUDES]$NCL"
    exit 1
fi
lines=($2)
base_command="find $1 -name \"*.launch\""
if [ ! -z "$2" ]
then
    echo -e "${CYN}Some paths will be excluded from the analysis$NCL"
    base_command="$base_command | grep -v"
    for line in "${lines[@]}"
    do
        base_command="$base_command -e $line"  
    done
fi

echo $base_command