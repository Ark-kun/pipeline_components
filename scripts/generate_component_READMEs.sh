#!/usr/bin/env bash

set -e

#find -name "component.yaml" | while read file; do
#    echo "$file"
#    python generate_component_README.py "$file"
#done

script_dir=$(dirname "$0")

find -name "component.yaml" | python "$script_dir/generate_component_README.py" -
