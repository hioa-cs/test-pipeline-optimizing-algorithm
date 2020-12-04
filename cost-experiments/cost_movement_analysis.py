#! /usr/bin/env python

#####Note: The test position found in testdataset is not used in sorting.
##### They will be used for other computations

import sys
import operator
import time
import numpy
from numpy import median

filename = sys.argv[1]
after_filename = sys.argv[2]
cost_filename = sys.argv[3]
tests = []
test_pos = {}
dataset = []
pre_tests = {}
sub_tests = {}
sub_tests_combo = []
global no_of_swap
no_of_swap = 0

######################### GETTING TESTS from FILE #########################

def get_data(filename): # funtion in class as attribute can be a METHOD
    f = open(filename,"r")
    dataset = f.readlines()

    tests = []
    for line in dataset:
        line.split(',')
        tests.append(line.replace('\n',''))
    #print "TEST DATA COLLECTED FROM FILE and Stored in List"
#    print tests
    return tests


    pre_list = ptest.split(',')[3:]

def print_stats(name,array):
    print name 
    print " -> sum: " + str(sum(array))
    print " -> average: " + str(sum(array) / float(len(array)))
    print " -> median: " + str(median(array))
    print ""



def main():
    before_tests = get_data(filename)

    after_tests = get_data(after_filename)

    cost_list = get_data(cost_filename)

    low_list = []
    medium_list = []
    high_list = []

    counter = 1
    for test in before_tests:
        testname = test.split(",")[0]
 #       print "Checking test " + str(testname)

        # find new position

        pos = 1
        for newtest in after_tests:
            if str(newtest.split(",")[0]) == str(testname):
                break
            pos += 1

#        print "-> New position: " + str(pos)
        pos_delta = pos - counter
#        print "-> Delta: " + str(pos_delta)

        # look up cost
        cost = 0
        for ctest in cost_list:
            if str(ctest.split(",")[0]) == str(testname):
                cost = str(ctest.split(",")[1])
                break

 #       print "-> cost this test: " + str(cost)

        if cost == "1":
            low_list.append(pos_delta)
        elif cost == "0.5":
            medium_list.append(pos_delta)
        else:
            high_list.append(pos_delta)

        counter += 1



    print "TEST MOVEMENT ANALYSIS: "

    print_stats("Movement by thests in the LOW category:",low_list)
    print_stats("Movement by thests in the MEDIUM category:",medium_list)
    print_stats("Movement by thests in the HIGH category:",high_list)









if __name__ == '__main__':
    main()
