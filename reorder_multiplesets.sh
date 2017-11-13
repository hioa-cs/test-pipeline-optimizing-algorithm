#! /bin/bash

# think of computations like this also?


# get directory name dname = sys.argv[1]
#for tf in datasets/dname/testdataset_*.csv; do
# how to do this? hmmm .....

for tf in datasets/testdataset_*.csv; do
  python test_reordering_algorithm.py "$tf"
done
