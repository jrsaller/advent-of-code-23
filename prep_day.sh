#!/bin/bash
echo $1
mkdir day$1
touch day$1/day$1.py day$1/readme.txt day$1/source.txt  day$1/test_source.txt
cp shared.py day$1/shared.py 