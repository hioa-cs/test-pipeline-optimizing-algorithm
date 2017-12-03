#! /bin/bash

for tf in datasets/case_2/*.csv; do
  python test_reordering_algorithm_fastest.py "$tf"
done
