#!/bin/bash 

TESTS=$1
DEPS=$2
PROB=$3

LOW_CUT=$4

MED_CUT=$5

FILENAME=dataset_${TESTS}_${DEPS}.csv

COST_FILENAME=dataset_${TESTS}_${DEPS}.cost

# generate the dataset

./test_generator.py $TESTS $DEPS $PROB $FILENAME

./cost_generator.py $TESTS $LOW_CUT $MED_CUT $COST_FILENAME
echo "### BEGIN INPUT"
cat $FILENAME
echo "### END INPUT"

# run the test

echo "### BEGIN ALGORITM"
./test_reordering_algorithm_fastest_cost.py $FILENAME $COST_FILENAME
echo "### END ALGORITHM"

echo "### BEGIN SORTED"
cat ${FILENAME}_sorted.csv
echo "### END SORTED"

# cat the output
echo "### BEGIN TIME"
cat ${FILENAME}_time.txt
echo "### END TIME"

echo "### BEGIN MOVEMENT"
./cost_movement_analysis $FILENAME ${FILENAME}_sorted.csv $COST_FILENAME
echo "### END MOVEMENT"