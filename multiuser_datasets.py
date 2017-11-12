#! /usr/bin/env python

import sys
import operator
import random
import string
import csv

filename = sys.argv[1]

tests = []
newtests = []

# need same testset for all user with different prob_fail value
# so that we can sort for each user to see how much it optimizes per user.

def get_data(filename): # funtion in class as attribute can be a METHOD
    f = open(filename,"r")
    dataset = f.readlines()

    for line in dataset:
        line.split(',')
        tests.append(line.replace('\n',''))
    print "unsorted test dataset COLLECTED"
    f.close()
    return


def get_probabilities():
    prob_fail = random.uniform(0.0001, 1.0000)
    prob_fail = repr(prob_fail)
    prob_fail = prob_fail.split(',')
#    print prob_fail
    return prob_fail

def set_new_prob(tests): # in progress
#    pos = tests.index(test)
    for test in tests:
        pos = tests.index(test)
        print pos
        test = test.split(',')
    #    new_prob = get_probabilities()
    #    test[2] = new_prob
    #    print test[2]

def write_data(newtests):
    timestr = time.strftime("%H%M%S")
    testfilename = 'datasets/testdataset_{0}{1}'.format(timestr,".csv")
    testing = csv.writer(open(testfilename, 'wb'), lineterminator='\n')
    for line in tests:
        testing.writerow(line)


def main():

    get_data(filename)
#    print tests
    set_new_prob(tests)
#    write_data(tests)

    outfile_name = '{0}{1}{2}'.format(filename,"_USER",".csv")
#    with open('datasets/sorted_testdataset.csv', 'w') as f:
    with open(outfile_name, 'w') as f:
        for s in newtests:
            f.write(s + '\n')


if __name__ == '__main__':
    main()
