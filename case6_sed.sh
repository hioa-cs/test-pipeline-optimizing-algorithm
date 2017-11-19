#! /bin/bash

for (( n=1; n<=10; n++ ))
do
  sed 's/"//g' datasets/case_6/_USER_$n.csv > datasets/case_6/t3_min/t3_min_USER_$n.csv
done
