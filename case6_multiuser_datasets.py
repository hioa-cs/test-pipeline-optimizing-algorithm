#! /usr/bin/env python

import sys
import operator
import random
import string
import csv
import time

filename = sys.argv[1]
users = int(sys.argv[2])
outfilename = sys.argv[3]
no_of_users = range(users)

tests = []
newtests = []
testsnew = []

# need same testset for all user with different prob_fail value
# so that we can sort for each user to see how much it optimizes per user.

def get_data(filename): # funtion in class as attribute can be a METHOD
    f = open(filename,"r")
    dataset = f.readlines()

    for line in dataset:
        line.split(',')
        tests.append(line.replace('\n',''))
#    print "unsorted test dataset COLLECTED"
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
#        print pos
        test = test.split(',')
        new_prob = 0
        new_prob = get_probabilities()
#        testnew = []
    #    testnew = test[0], test[1], new_prob[0], test[3:]
    #    tests[pos] = list(testnew) #test[0], test[1], new_prob[0], test[3:]
    #    testsnew.append(list(testnew))
        if not test[3:]:
            dep = ' '
    #        print "space"
        else:
    #        dep = test[3] # works for one dependency
            dep = test[3:]
            dep.split(",")
#        print dep
        tests[pos] = test[0], test[1], new_prob[0], dep # test[3:]
#    print tests
    return tests

def write_data(newtests,i):
    timestr = time.strftime("%H%M%S")
#    testfilename = 'datasets/testdataset_{0}{1}{2}{3}'.format(timestr,"_USER_",i,".csv")
    testfilename = outfilename
    testing = csv.writer(open(testfilename, 'wb'), lineterminator='\n')
    for line in tests:
        testing.writerow(line)


def main():

#    print tests
#    print "\n"

    i = 1
    get_data(filename)
    newtests = set_new_prob(tests)
    #    print newtests
    write_data(newtests,i)

    for i in no_of_users :
        del tests[:]
#        tests[:] = []
        newtests[:] = []
        i += 1

        get_data(filename)
        newtests = set_new_prob(tests)
        #    print newtests
        write_data(newtests,i)

if __name__ == '__main__':
    main()
