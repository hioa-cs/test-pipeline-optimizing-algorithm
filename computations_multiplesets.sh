#! /bin/bash

# WIP

# get directory name dname = sys.argv[1]
#for tf in datasets/dname/testdataset_*.csv; do
# how to do this? hmmm .....

# ./computations.py datasets/testdataset_010556_USER_5.csv datasets/testdataset_010556_USER_5.csv_sorted.csv

for tf in datasets/testdataset_*.csv; do
  python test_reordering_algorithm.py "$tf"
done
