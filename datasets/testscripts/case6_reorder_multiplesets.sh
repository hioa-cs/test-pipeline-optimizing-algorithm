#! /bin/bash

for tf in datasets/case_6/t3_min/*.csv; do
  python test_reordering_algorithm_fastest.py "$tf"
done

for tf in datasets/case_6/t10/*.csv; do
  python test_reordering_algorithm_fastest.py "$tf"
done
