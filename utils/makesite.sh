#!/bin/bash

if [[ $1 = "-f" ]]; then
	python Makefile.py -f ../src/ ../html/
else
	python Makefile.py ../src/ ../html/
fi
