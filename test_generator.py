#! /usr/bin/env python

import sys
import operator
import random
import string
import csv

no_of_tests = range(7)
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
    # with open('sorted_testlist.csv', 'w') as f:
    #
            testing = csv.writer(open('datasets/testdataset.csv', 'wb'), lineterminator='\n')
            for line in tests:
                testing.writerow(line)
    #        testing.writerow(tests)
    #        print testing
    #        print '\n'
    #       s = [x for y in tests for x in y]
    #        for line in s:
            #    string = str(line)

            #    print string
#    return s

def get_tests(testname, counter, prob_fail, dependency):
    test_data = testname + counter + prob_fail + dependency_generator(alltests)   #dependency #+ get_dependencies(alltests)
    print test_data
    tests.append(test_data)
    print tests


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
#    dependency = [[] for _ in range(3)]
    dependency = []
    for i in range(3):
        dep = random.choice(alltests)
        if dep not in dependency and dep != testname:
            dependency.append(dep)

    dependencies = [x for y in dependency for x in y]
    return dependencies

def dependency_generator(alltests):
    dependency = []
    for i in no_of_tests:
        dependency = get_dependencies(alltests)
    return dependency

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
        prob_fail = get_probabilities() #['0.5']# get_probabilities()
#        print prob_fail
        if i > 0:
            dependency = get_dependencies(alltests,testname)
    #        print dependency

        test_data = testname + counter + prob_fail + dependency #+ get_dependencies(alltests)
        tests.append(test_data)


    return tests


#    return testname, counter, prob_fail
#        test_data = testname + counter + prob_fail + dependency #+ get_dependencies(alltests)
#        print test_data
#        tests.append(test_data)
#        print tests

def main():

    testset = generator()
#    print testset
    write_data(testset)

if __name__ == '__main__':
    main()
