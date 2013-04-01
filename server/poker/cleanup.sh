#!/bin/sh

# Cleanup removes all the .pyc files from all directories

find . -name *.pyc -exec rm -rf {} \;
