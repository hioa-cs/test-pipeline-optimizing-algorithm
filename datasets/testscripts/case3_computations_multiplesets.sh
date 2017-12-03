#! /bin/bash

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python test_computations.py datasets/case_3/100tests_max_80_8/t$n.csv datasets/case_3/100tests_max_80_8/t$n.csv_sorted.csv
done

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python test_computations.py datasets/case_3/100tests_mid_50_3/t$n.csv datasets/case_3/100tests_mid_50_3/t$n.csv_sorted.csv
done

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python test_computations.py datasets/case_3/100tests_min_20_2/t$n.csv datasets/case_3/100tests_min_20_2/t$n.csv_sorted.csv
done
