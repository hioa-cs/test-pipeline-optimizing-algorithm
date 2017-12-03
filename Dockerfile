FROM ubuntu:16.04
MAINTAINER Kyrre Begnum

RUN apt-get update && apt-get install -y python python2.7
ADD test_reordering_algorithm_fastest.py /
ADD run_data_and_test.sh /
ADD test_generator.py /

