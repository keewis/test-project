#!/usr/bin/env bash
ref="$0"
keywords="$1"

git log -n 1 --pretty=format:%s "$ref" | grep -q "$keywords"
if [[ $? -eq 0 ]]; then
    result="true"
else
    result="false"
fi

echo "found trigger: $result"

echo "::set-output name=CI_TRIGGERED::$result"
