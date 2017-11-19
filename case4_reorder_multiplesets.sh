#! /bin/bash

for tf in datasets/case_6/t3_min/*.csv; do
  python test_reordering_algorithm_fast.py "$tf"
done
