#! /bin/bash

for tf in datasets/case_5/*.csv; do
  python test_reordering_algorithm_fastest.py "$tf"
done
