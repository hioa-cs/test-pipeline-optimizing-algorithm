#! /usr/bin/env python

# this scipt generates the number of dataset given as input with the number of
# dependency per test given as input.

import sys
import operator
import random
import string
import csv
import time

num = int(sys.argv[1])
no_of_dep = int(sys.argv[2])
#tfilename = sys.argv[3]
arg_filename = str(sys.argv[3])

multidep = range(no_of_dep)
no_of_tests = range(num)
tests = []
prob_fail = []
dependency = []
test_data = []
counter = []
alltests = []
copytests = []
testname = []


def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def write_data(tests):
    timestr = time.strftime("%H%M%S")
#    testfilename = 'datasets/{0}{1}'.format(tfilename,".csv")
#    testfilename = 'datasets/testdataset_multidep_{0}{1}'.format(timestr,".csv")
    if arg_filename:
        testfilename = arg_filename

    testing = csv.writer(open(testfilename, 'wb'), lineterminator='\n')
    for line in tests:
        testing.writerow(line)


def get_testnames(testnum):
    testname = '%010d' % testnum
#    testname = str(testname)
    testname = testname.split(',')
    return testname


def get_probabilities():
    prob_fail = random.uniform(0.0001, 1.0000)
    prob_fail = repr(prob_fail)
    prob_fail = prob_fail.split(',')
    return prob_fail


def get_dependencies(alltests,testname):
#    print alltests
    dependency = []
    for i in multidep:
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
    testnum = 0
    for i in no_of_tests :
        testnum += 1
        testname = get_testnames(testnum) #['D']#
#        print testname

        alltests.append(testname)
        counter = get_counter(i)
#        print counter
        prob_fail = get_probabilities() #['0.5']
#        print prob_fail
        if i > 0:
            dependency = get_dependencies(alltests,testname)
            if not dependency:
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
