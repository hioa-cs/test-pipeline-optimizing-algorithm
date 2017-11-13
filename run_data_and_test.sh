#!/bin/bash 

TESTS=$1
DEPS=$2

FILENAME=dataset_${TESTS}_${DEPS}.csv
# generate the dataset

./test_generator.py $TESTS $DEPS $FILENAME

# run the test

./test_reordering_algorithm.py $FILENAME

# cat the output

cat ${FILENAME}_ 

