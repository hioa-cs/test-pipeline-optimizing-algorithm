#!/bin/bash 

TESTS=$1
DEPS=$2

FILENAME=dataset_${TESTS}_${DEPS}.csv
# generate the dataset

./test_generator.py $TESTS $DEPS $FILENAME

echo "### BEGIN INPUT"
cat $FILENAME
echo "### END INPUT"

# run the test

echo "### BEGIN ALGORITM"
./test_reordering_algorithm.py $FILENAME
echo "### END ALGORITHM"

echo "### BEGIN SORTED"
cat ${FILENAME}_sorted.csv
echo "### END SORTED"

# cat the output
echo "### BEGIN TIME"
cat ${FILENAME}_time.txt
echo "### END TIME"
