#! /bin/bash

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python computations.py datasets/100tests_max_80_8/t$n.csv datasets/100tests_max_80_8/t$n.csv_sorted.csv
done

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python computations.py datasets/100tests_mid_50_3/t$n.csv datasets/100tests_mid_50_3/t$n.csv_sorted.csv
done

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python computations.py datasets/100tests_min_20_2/t$n.csv datasets/100tests_min_20_2/t$n.csv_sorted.csv
done
