#!/bin/bash

echo "Creating package in dist directory"
python3 setup.py bdist_wheel

echo "Finished"