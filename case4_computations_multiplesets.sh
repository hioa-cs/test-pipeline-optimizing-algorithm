#! /bin/bash

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python test_computations.py datasets/case_4/t$n.csv datasets/case_4/t$n.csv_sorted.csv
done
