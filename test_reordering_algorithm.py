#! /usr/bin/env python
# v3

import sys

filename = sys.argv[1]
tests = []
dataset = []

def get_data(filename): # funtion in class as attribute can be a METHOD
        dataset = [i.strip('\n').split(',') for i in open(filename)]
#        print 'before: '
#        print dataset
        return dataset

######EXAMPLE##########
# l = [[A, 1, 2], [B, 2, 5], [C, 2]]
#for item in l:
#   print item[0], ', '.join(map(str, item[1:]))
#############################

def compute_pre_tests(test,tname):
    pre_tests = []
    name_test = tname
    if test[3]:
        for t in test[3:]:
            pre_tests.append(name_test)
    print 'PRE TESTS'
    print pre_tests
    return pre_tests

# finds the mamimum position in the pre_tests and subsequent_tests list
def find_max(tests, p, stest):
#    print 'stest'
#    print stest
    if stest == []:
        #return tests[test].position
        #return len(tests) + 1
        return -1
    max_position = 0

    for t in stest:
        t_position = p
        if max_position < t_position:
            max_position = t_position
    print 'MAX'
    print max_position
    return max_position

# finds the minimum position in the pre_tests and subsequent_tests list
#call with - find_min(tests, rx, subsequent_tests)
def find_min(tests, p, stest):
#    print xpos
    if stest == []:
        return len(tests) + 1
    min_position = len(tests) + 1

    for t in stest:
        t_position = p
        if min_position > t_position:
            min_position = t_position
    print 'MIN'
    print min_position
    return min_position

#tests is the array of tests
# rx position of test x
# ry positon of test y
def swap(tests, x, y):
    temp_position = tests[x]
#    print temp_position
    tests[x] = tests[y]
    tests[y] = temp_position
    print 'SWAP'
    print tests[x],tests[y]

#Using Lists
def reorder(tests):
    for rx in tests:
        xpos = float(rx[1])
        x_prob_fail= float(rx[2])
        delta_max = 0
        delta_max_test = 0
#        print rx
#        print xpos, x_prob_fail
        for ry in tests:
            new = 0
            ypos = float(ry[1])
            y_prob_fail = float(ry[2])
#            print ry
#            print ypos, y_prob_fail
            if rx != ry:
                if xpos < ypos:
#                    pre_tests = compute_pre_tests(ry,ry[0])
#                    print pre_tests
#                    print xpos,ypos
                    print 'ry'
                    print ry[1],ry,ry[0]
                    rx_sub_test_minpos = find_min(tests, rx[1], rx[3:])
                    ry_pre_test_maxpos = find_max(tests, ry[1], compute_pre_tests(ry,ry[0])) # FIND MAX find_max(tests, ry, pre_tests[])
                    print 'xpos < ypos'
#                    print ry_pre_test_maxpos
#                    print rx_sub_test_minpos
                    if xpos < ry_pre_test_maxpos and ypos > rx_sub_test_minpos:
                        print 'xpos < ry_pre_test_maxpos and ypos > rx_sub_test_minpos'
                        if x_prob_fail < x_prob_fail:
                            print 'x_prob_fail < x_prob_fail'
                            # new value of decrease in time by doing swapping
                            # difference in test positions - difference in porbability of a test failing
                            new = float(x_prob_fail - x_prob_fail * xpos - ypos)
                            print new
                            if delta_max < new:
                                delta_max = new
                                delta_max_test = ry[1]
                                print delta_max_test
                else:
#                    print xpos,ypos
                    print 'else xpos > ypos'
                    ry_sub_test_minpos = find_min(tests, ry[1], ry[3:]) #FIND MIN find_min(tests, rx, v[3:])
                    rx_pre_test_maxpos = find_max(tests, rx[1], compute_pre_tests(rx,rx[0])) # FIND MAX find_max(tests, rx, pre_tests[])
#                    print ry_sub_test_minpos
#                    print rx_pre_test_maxpos
                    if ypos < rx_pre_test_maxpos and xpos > ry_sub_test_minpos:
                        print 'else: ypos < rx_pre_test_maxpos and xpos > ry_sub_test_minpos:'
                        if x_prob_fail < xpos:
                            print 'else: x_prob_fail < xpos'
                            new = x_prob_fail - x_prob_fail * xpos - ypos
#                            print new
                            if delta_max < new:
                                delta_max = new
                                delta_max_test = ry[1]
#                                print delta_max_test
#            print tests

        if delta_max > 0:
            swap(tests, xpos, delta_max_test)
        else:
            continue
#    print tests
#    print delta_max
    return delta_max

def main():
    reorder(get_data(filename))



if __name__ == '__main__':
    main()
