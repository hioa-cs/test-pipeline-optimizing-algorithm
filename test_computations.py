#! /usr/bin/env python

import sys
import time

filename = sys.argv[1]
sorted_filename = sys.argv[2]

print sys.argv[1]
print sys.argv[2]

computation = '{0}{1}'.format(filename,"_computation.txt")
text_file = open(computation, 'w')

tests = []
sortedtests = []

global avg_fail_discovery


def get_data(filename): # funtion in class as attribute can be a METHOD
    f = open(filename,"r")
    dataset = f.readlines()

    for line in dataset:
        line.split(',')
        tests.append(line.replace('\n',''))
    print "unsorted test DATA COLLECTED"
    f.close()
    return

def get_sorteddata(sorted_filename): # funtion in class as attribute can be a METHOD
    f = open(sorted_filename,"r")
    dataset = f.readlines()

    for line in dataset:
        line.split(',')
        sortedtests.append(line.replace('\n',''))
    print "Sorted test data COLLECTED"
    f.close()
    return

def write_data(test, avg_fail_discovery):

    if test == tests:
        text_file.write("Avg time to discover failure in list: {} \n".format(avg_fail_discovery))
    if test == sortedtests:
        text_file.write("\nAvg time to discover failure in sorted list: {} \n".format(avg_fail_discovery))

def avg_failure_discovery(tests):
    position = 0
    prob_fail = 0
    avg_fail = 0
    for test in tests:
        position = (tests.index(test)+1)
        print position
        test = test.split(',')
        prob_fail = float(test[2])
        print prob_fail
        fail_discovery = position * prob_fail
        avg_fail = avg_fail + fail_discovery
#    print avg_fail
    return avg_fail

def main():

    get_data(filename)
#    print tests

    get_sorteddata(sorted_filename)
#    print sortedtests

    avg_fail_discovery = avg_failure_discovery(tests)
    print avg_fail_discovery
    write_data(tests, avg_fail_discovery)

    sorted_avg_fail_discovery = avg_failure_discovery(sortedtests)
    write_data(sortedtests, sorted_avg_fail_discovery)
    print avg_fail_discovery

    simple_impact_value = avg_fail_discovery - sorted_avg_fail_discovery
    print simple_impact_value

    text_file.write("\nSimple impact value of sorting: {} \n".format(simple_impact_value))
    text_file.close()

if __name__ == '__main__':
    main()
