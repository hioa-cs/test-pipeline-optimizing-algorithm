#! /usr/bin/env python
# v3

import sys

filename = sys.argv[1]
tests = []
dataset = []
withpretests = []
pre_tests = {}
#pret = [['A','C','D'],['B','A','C'],['C','D'],['D','B']]

def get_data(filename): # funtion in class as attribute can be a METHOD
    dataset = [i.strip('\n').split(',') for i in open(filename)]
    return dataset


def get_dependencies(test,ptest,ptests):
    # test = the test we are searching on behalf of
    # ptest = a test we found down the dependencie line
    sub_tests = []

    sub_tests = ptest[3:]
    # 1. get all known get_dependencies
    print "Finding all unknown dependencies for " + test + " from " + ptest[0]
    if len(sub_tests) == 0:
        print "No known dependencies for " + ptest[0] + ", skipping"
        return
    
    for t in sub_tests:
        if t not in pre_tests[test]:
            print "storing " + t + " as a dependencie for " + test
            pre_tests[test].append(t)            
            for dep in ptests:
                if t == dep[0]:
                    get_dependencies(test,dep,ptests)




    # 2. add all known dependencies to t's list (if not there already)

    # 3. Call get dependencies for all known dependencies


def compute_pre_tests(ptests): # whole tests list, particular test positon - pos
#    print 'Compute pre test'
#    print ptests
    sub_tests = []

    for r in ptests:
        sub_tests = r[3:]
        sublen = len(sub_tests)
        rlen = len(r)
        ppos = (rlen - sublen) + 1
        tname = r[0]
        pre_tests[tname] = []
        print "Finding all dependencies for " + tname
        if len(sub_tests) == 1 and sub_tests[0] == '':
            print "No known dependencies for " + tname + ", skipping"
            return
        for t in sub_tests:
            print "storing " + t + " as a dependencie for " + tname
            pre_tests[tname].append(t)            
            for test in ptests:
                if t == test[0]:
                    get_dependencies(tname,test,ptests)
                    # test.append(tname)
#                    print test[ppos:]

#    print ptests[pos][ppos:]
#    return ptests[pos][ppos:]
#    print ptests
    return ptests

#call with - find_max(tests, subsequent_tests/ pre_tests)
# for each test in the pre or sub list find the position of that test in the main tests!
# from that compute the test with the max position in tests

def find_max(tests, tlist):
    if tlist == []:
        return -1
    max_position = 0

    for t in tlist:
        for test in tests:
            if test[0] == t:
                t_position = test[1]
                if t_position > max_position:
                    max_position = t_position
#    print 'MAX'
#    print max_position
    return max_position

#call with - find_min(tests, subsequent_tests/ pre_tests)
#for each test in the pre or sub list find the position of that test in the main tests!
# compute the test with the min postion in tests

def find_min(tests, tlist):
#    print xpos
    if tlist == []:
        return len(tests) + 1
    min_position = len(tests) + 1
#    print min_position

    for t in tlist:
        for test in tests:
            if test[0] == t:
                t_position = test[1]
                if t_position < min_position:
                    min_position = t_position

#    print 'MIN'
#    print min_position
    return min_position

#tests is the array of tests
# rx position of test x
# ry positon of test y
def swap(tests, x, y):
    temp = []
#    tpos = x
    temp = tests[x]
    tests[x] = tests[y]
    tests[y] = temp
    print 'SWAP'
    print tests[x],tests[y]

#Using Lists
def reorder(tests,withpretests):
    print tests
    print withpretests
    for rx in tests:
        xpos = int(rx[1])
        x_prob_fail= float(rx[2])
        delta_max = 0
        delta_max_test = 0
        xsublen = len(rx[3:])
        xlen = len(rx)
        xppos = (xlen - xsublen)
        for ry in tests:
            new = 0
            ypos = int(ry[1])
            y_prob_fail = float(ry[2])
            ysublen = len(ry[3:])
            ylen = len(ry)
            yppos = (ylen - ysublen)
            if rx != ry:
                if xpos < ypos:
#                    print 'ry'
#                    print ry[1],ry,ry[0]
                    rx_sub_test_minpos = find_min(tests, rx[3:])
                    ry_pre_test_maxpos = find_max(tests, withpretests[yppos:]) # FIND MAX find_max(tests, ry, pre_tests[])
#                    print 'xpos < ypos'
                    if xpos > ry_pre_test_maxpos and ypos < rx_sub_test_minpos:
#                        print 'xpos < ry_pre_test_maxpos and ypos > rx_sub_test_minpos'
                        if x_prob_fail < x_prob_fail:
#                            print 'x_prob_fail < x_prob_fail'
                            # new value of decrease in time by doing swapping
                            # difference in test positions - difference in porbability of a test failing
                            new = (x_prob_fail - x_prob_fail) * (xpos - ypos)
#                            print new
                            if delta_max < new:
                                delta_max = new
                                delta_max_test = ry
#                                print delta_max_test
                else:
#                    print 'else xpos > ypos'
                    ry_sub_test_minpos = find_min(tests, ry[3:]) #FIND MIN find_min(tests, rx, v[3:])
                    rx_pre_test_maxpos = find_max(tests, withpretests[xppos:]) # FIND MAX find_max(tests, rx, pre_tests[])

                    if ypos > rx_pre_test_maxpos and xpos < ry_sub_test_minpos:
#                        print 'else: ypos < rx_pre_test_maxpos and xpos > ry_sub_test_minpos:'
                        if x_prob_fail < xpos:
#                            print 'else: x_prob_fail < xpos'
                            new = (x_prob_fail - x_prob_fail) * (xpos - ypos)
#                            print new
                            if delta_max < new:
                                delta_max = new
                                delta_max_test = ry # the whole test and its elements
#                                print delta_max_test
        if delta_max > 0:
#            swap(tests, rx, delta_max_test)
            swap(tests, xpos, delta_max_test[1]) #delta_max_test[1] has ry[1] meaning the position of ry
        else:
            continue
#    print tests
#    print delta_max
    return delta_max

def main():

#    compute_pre_tests(get_data(filename),(3-1)) # 3-1 for line 3

    withpretests = compute_pre_tests(get_data(filename))

    reorder(get_data(filename),withpretests)



if __name__ == '__main__':
    main()
