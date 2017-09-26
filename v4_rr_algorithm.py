#! /usr/bin/env python

import sys
import time
import datetime
import argparse
import logging
import re
import pprint
import csv

#https://stackoverflow.com/questions/20157824/how-to-take-input-file-from-terminal-for-python-script#20158514
filename = sys.argv[1]

class Softtest: #define a class object
    def __init__(self, test_name, test, probability_failure, position, subsequent_tests, pre_tests ): # class test with value
        self.test_name = test_name # unique name of the tests (test1,test2,test3,etc.)
        self.test = test # the test itself that needs to be done (could be a test that needs to be called, like a test function checking for smth?)
        self.probability_failure = probability_failure # probability of this test failing
        self.position = position # position of test in testing pipeline now
        self.subsequent_tests = subsequent_tests # tests that come after the current test,
                                    # meaning ti should come before these tests
        self.pre_tests = pre_tests # tests that come before the current test,
                                    # meaning ti should come after these tests

        #Average time to discover failure
        # sum of (test position * probability of failure)
        def get_one_failure_discover_time(self):
            return float(self.position * self.probability_failure)

        # To get the average - get the sum of this / how?

#reading dataset as table
#https://stackoverflow.com/questions/9171157/how-to-read-data-table-column-by-column-from-a-txt-in-python
#reads the testdataset
def read_tests(filename):
    tests = {} # empty dictionary for storing testdataset
    tests_list = [] #emptry list to store omly test_name
    position = 0
    skip = True
    with open(filename, 'rb') as f:
        for r in csv.reader(f, delimiter = ','):
#            print r
            if skip:
                skip = False
                continue
            test_name = r[0].strip('\'')
#            print test_name
#            print test_name
            probability_failure = r[1].strip('\'')
#            print probability_failure
#            probability_failure = float(probability_failure)
            if r[2]:
                subsequent_tests = r[2].strip('\'')
#                print subsequent_tests
            else:
                subsequent_tests = []

            test = test_name # give location of the file that contains the test to be done
            position += 1
            tests[test_name] = Softtest(test_name, test, probability_failure, position, subsequent_tests, pre_tests=[])
#            print tests
            tests_list.append(test_name)
#            print tests_list
    return tests, tests_list

def compute_pre_tests(tests):
    for test in tests:
        name_test = tests[test].test_name
        if tests[test].subsequent_tests:
            for r in tests[test].subsequent_tests:
                tests[r].pre_tests.append(name_test)


# finds the mamimum position in the pre_tests and subsequent_tests list
def find_max(tests, test, lst):
    logging.debug("test: %s" % test)
    logging.debug("lst: ")
    logging.debug(lst)
    if lst == []:
        #return tests[test].position
        #return len(tests) + 1
        return -1
    max_position = 0
    for r in lst:
        r_position = tests[r].position
        if max_position < r_position:
            max_position = r_position
    return max_position

# finds the minimum position in the pre_tests and subsequent_tests list
def find_min(tests, test, lst):
    logging.debug("test: %s" % test)
    logging.debug("lst: ")
    logging.debug(lst)
    if lst == []:
        #return tests[test].position
        #return -1
        return len(tests) + 1
    min_position = len(tests) + 1
    for r in lst:
        r_position = tests[r].position
        if min_position > r_position:
            min_position = r_position
    return min_position


#tests is the array of tests
# rx position of test x
# ry positon of test y
def swap(tests, rx, ry):
    logging.debug("Swapping test: %s to %s" % (rx,ry))
    temp_position = tests[rx].position
    tests[rx].postion = tests[ry].position
    tests[ry].position = temp_position


def reorderTests(tests):
    for rx in tests:
        maxim = 0
        max_test = None
        for ry in tests:
            new = 0
            if rx != ry:
                if tests[rx].position < tests[ry].position:
                    rx_subsequent_tests_min_position = find_min(tests, rx, tests[rx].subsequent_tests)
                    ry_pre_tests_max_position = find_max(tests, ry, tests[ry].pre_tests)

                    if tests[rx].position < ry_pre_tests_max_position and tests[ry].position > rx_subsequent_tests_min_position:
                        if tests[rx].probability_failure < tests[ry].probability_failure:
                            # new value of decrease in time by doing swapping
                            # difference in test positions - difference in porbability of a test failing
                            new = tests[ry].probability_failure - tests[rx].probability_failure * tests[ry].position - tests[rx].position
                            if maxim < new:
                                maxim = new
                                max_test = ry
                else:
                    ry_subsequent_tests_min_position = find_min(tests, ry, tests[ry].subsequent_tests)
                    rx_pre_tests_max_position = find_max(tests, rx, tests[rx].pre_tests)
                    if tests[ry].position < rx_pre_tests_max_position and rx.position > ry_subsequent_tests_min_position:
                        if tests[ry].probability_failure < tests[rx].probability_failure:
                            new = tests[rx].probability_failure - tests[ry].probability_failure * tests[rx].position - tests[ry].position
                            if maxim < new:
                                maxim = new
                                max_test = ry
        if maxim > 0:
    	   swap(tests, rx, max_test)
        else:
            continue
	return maxim


# MAIN
def main():

# You can return a tuple of lists, and use sequence unpacking to assign them to two different names when calling the function
# https://stackoverflow.com/questions/11690333/is-it-possible-to-return-two-lists-from-a-function-in-python
    tests, tests_list = read_tests(filename)
#    tests = read_tests(filename)
    print 'Before swap:\n'
    print tests
    print '\n'
    print tests_list
    print '\n'

# compute_pre_tests(tests)

#    length_list = len(tests_list)
#    for i in range(1):
#        reorderTests(tests)

    print 'After swap:\n'
#    print tests
    print '\n'

if __name__ == '__main__':
    main()
