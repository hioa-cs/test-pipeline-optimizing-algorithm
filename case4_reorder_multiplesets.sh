#! /bin/bash

for tf in datasets/case_4/*.csv; do
  python test_reordering_algorithm_fast.py "$tf"
done
