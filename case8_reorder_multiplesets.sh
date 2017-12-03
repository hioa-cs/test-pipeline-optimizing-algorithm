#! /bin/bash

for tf in datasets/case_8/100tests_max_80_8/*.csv; do
  python test_reordering_algorithm_fastest_multi_iteration.py "$tf"
done

for tf in datasets/case_8/100tests_mid_50_3/*.csv; do
  python test_reordering_algorithm_fastest_multi_iteration.py "$tf"
done

for tf in datasets/case_8/100tests_min_20_2/*.csv; do
  python test_reordering_algorithm_fastest_multi_iteration.py "$tf"
done

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python test_computations.py datasets/case_8/100tests_max_80_8/t$n.csv datasets/case_8/100tests_max_80_8/t$n.csv_sorted.csv
done

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python test_computations.py datasets/case_8/100tests_mid_50_3/t$n.csv datasets/case_8/100tests_mid_50_3/t$n.csv_sorted.csv
done

for (( n=1; n<=10; n++ ))
do
  echo "Running computations on Test $n"
  python test_computations.py datasets/case_8/100tests_min_20_2/t$n.csv datasets/case_8/100tests_min_20_2/t$n.csv_sorted.csv
done
