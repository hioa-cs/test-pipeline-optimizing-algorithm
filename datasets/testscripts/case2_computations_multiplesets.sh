#! /bin/bash

for (( n=100; n<=1000; n+100 ))
do
  echo "Running computations on Test $n"
  python test_computations.py datasets/case_2/$n*.csv datasets/case_2/$n*.csv_sorted.csv
done
