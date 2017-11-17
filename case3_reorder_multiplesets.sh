#! /bin/bash

for tf in datasets/case_3/100tests_max_80_8/*.csv; do
  python test_reordering_algorithm_fast.py "$tf"
done

for tf in datasets/case_3/100tests_mid_50_3/*.csv; do
  python test_reordering_algorithm_fast.py "$tf"
done

for tf in datasets/case_3/100tests_min_20_2/*.csv; do
  python test_reordering_algorithm_fast.py "$tf"
done
