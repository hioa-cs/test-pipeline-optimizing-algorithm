FROM ubuntu:16.04
MAINTAINER Kyrre Begnum

ADD test_reordering_algorithm.py /
ADD run_data_and_test.sh /
ADD test_generator.py /

