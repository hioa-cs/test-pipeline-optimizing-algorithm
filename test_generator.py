#! /usr/bin/env python

import sys
import operator
import random
import string
import csv

num = int(sys.argv[1])
no_of_tests = range(num)
tests = []
testname = []
prob_fail = []
dependency = []
test_data = []
counter = []
alltests = []


def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def write_data(tests):

    testing = csv.writer(open('datasets/testdataset.csv', 'wb'), lineterminator='\n')
    for line in tests:
        testing.writerow(line)


def get_testnames():
    testname = random_char(2)
    testname = testname.split(',')
#    print testname
    return testname


def get_probabilities():
    prob_fail = random.uniform(0.0001, 1.0000)
    prob_fail = repr(prob_fail)
    prob_fail = prob_fail.split(',')
#    print prob_fail
    return prob_fail


def get_dependencies(alltests,testname):
#    print alltests
    dependency = []
    for i in range(1):
        dep = random.choice(alltests)
        if dep not in dependency and dep != testname:
            dependency.append(dep)

    dependencies = [x for y in dependency for x in y]
    return dependencies

def get_counter(i):
    counter = i+1
    counter = str(counter)
    counter = counter.split(',')
#    print counter
    return counter

def generator():
    dependency = []
    for i in no_of_tests :
        testname = get_testnames() #['D']#
#        print testname
        alltests.append(testname)
        counter = get_counter(i)
#        print counter
        prob_fail = get_probabilities() #['0.5']
#        print prob_fail
        if i > 0:
            dependency = get_dependencies(alltests,testname)
    #        print dependency
        test_data = testname + counter + prob_fail + dependency
        tests.append(test_data)

    return tests


def main():

    testset = generator()
#    print testset
    write_data(testset)

if __name__ == '__main__':
    main()
