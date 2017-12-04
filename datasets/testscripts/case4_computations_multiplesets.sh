#! /bin/bash

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
#  python test_computations.py datasets/case_4/t$n.csv datasets/case_4/t$n.csv_sorted.csv
  python test_computations.py datasets/case_4/run1/t$n.csv_sorted.csv datasets/case_4/run2/t$n.csv_sorted.csv_sorted.csv
  python test_computations.py datasets/case_4/run2/t$n.csv_sorted.csv_sorted.csv datasets/case_4/run3/t$n.csv_sorted.csv_sorted.csv_sorted.csv
  python test_computations.py datasets/case_4/run3/t$n.csv_sorted.csv_sorted.csv_sorted.csv datasets/case_4/run4/t$n.csv_sorted.csv_sorted.csv_sorted.csv_sorted.csv
  python test_computations.py datasets/case_4/run4/t$n.csv_sorted.csv_sorted.csv_sorted.csv_sorted.csv datasets/case_4/run5/t$n.csv_sorted.csv_sorted.csv_sorted.csv_sorted.csv_sorted.csv
  python test_computations.py datasets/case_4/run5/t$n.csv_sorted.csv_sorted.csv_sorted.csv_sorted.csv_sorted.csv datasets/case_4/run6/t$n.csv_sorted.csv_sorted.csv_sorted.csv_sorted.csv_sorted.csv
done
