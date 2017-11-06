#! /usr/bin/env python

import sys
import operator

filename = sys.argv[1]
tests = []
dataset = []
pre_tests = {}
sub_tests = {}
#pret = [['A','C','D'],['B','A','C'],['C','D'],['D','B']]

######################### GETTING TESTS from FILE #########################

def get_data(filename): # funtion in class as attribute can be a METHOD
    f = open(filename,"r")
    dataset = f.readlines()

    for line in dataset:
        line.split(',')
        tests.append(line.replace('\n',''))
    print tests
    return tests


######################### GETTING SUB TESTS #########################

def get_subtest(tname,stest,pre_tests):
    # tname = the test we are searching on behalf of
    # stest = a test we found for the subtest list
    # pre_tests = is a dictionary of dependencies of each test
    for t in pre_tests:
        if t not in sub_tests[test]:
            print "storing " + t + " as a subtest for " + test
            sub_tests[tname].append(t)
            for stest in pre_tests:
                if t == stest[0]:
                    get_subtest(tname,stest,pre_tests)

def compute_subtest(tests,pre_tests):

    for k in pre_tests:
        tname = reduce(operator.concat, pre_tests[k])
        tname = reduce(operator.concat, tname)
        if len(tname) == 0 and tname == '' :
               print "No known subtest for " + k + ", skipping"
               continue
        print k
        print tname
        print 'storing {} as a subtest for {}'.format(k, tname)
        sub_tests[tname].append(k)
        for stest in pre_tests[k]:
            if stest == k:
                print 'storing {} as a subtest for {}'.format(stest, tname)
                sub_tests[tname].append(stest)
                get_subtest(tname,stest,pre_tests)
    print sub_tests
    return sub_tests

######################### END OF GETTING SUB TESTS #########################


############################## Getting pre_tests - dependencies for test ###############################

def get_dependencies(test,ptest,ptests):
    # ptests has the same thing as tests
    # test = the test we are searching on behalf of
    # ptest = a test we found down the dependencie line (ptest is a list containing everything about this test)
    # pre_list = is an empty list that is assigned the ptest[] list as found in test
    pre_list = []
    pre_list = ptest[3:]
    # 1. get all known get_dependencies
    print "Finding all unknown dependencies for " + test + " from " + ptest[0]
    if len(pre_list) == 0:
        print "No known dependencies for " + ptest[0] + ", skipping"
        return

    for t in pre_list:
        if t not in pre_tests[test]:
            print "storing " + t + " as a dependencie for " + test
            pre_tests[test].append(t)
            for dep in ptests:
                if t == dep[0]:
                    get_dependencies(test,dep,ptests)

    # 2. add all known dependencies to t's list (if not there already)

    # 3. Call get dependencies for all known dependencies

def compute_pre_tests(ptests): # whole tests list, particular test positon - pos
#     ptests has the same thing as tests
#    print 'Compute pre test'
#    print ptests
    # pre_list = is an empty list that is assigned the r[3:] list of dependencies as found in ptests[]
    pre_list = []

    for r in ptests:
        r = r.split(',')
        pre_list = r[3:]
#        print pre_list
        sublen = len(pre_list)
        tname = r[0]
        pre_tests[tname] = []
        print "Finding all dependencies for " + tname
        if len(pre_list) == 1 and pre_list[0] == '':
            print "No known dependencies for " + tname + ", skipping"
        #    return # with this return it skips finding dependencies if pre_list is empty
#        print pre_list
        for t in pre_list:
            t = t.split(',') #newly added for splitting, because t was printing and storing the commas as values
            print 'storing {} as a dependency for {}'.format(t,tname)
            pre_tests[tname].append(t)
            for test in ptests:
                if t == test[0]:
                    get_dependencies(tname,test,ptests)
                    # test.append(tname)

#    pre_tests has all dependencies for each test
#    print pre_tests
    return pre_tests


######################### END of Getting pre_tests - dependencies for test #####################


########################### COMPUTING MAX AND MIN VALUES ########################################

#call with - find_max(tests, subsequent_tests/ pre_tests)
# for each test in the pre or sub list find the position of that test in the main tests!
# from that compute the test with the max position in tests

# def find_max(tests, test, tlist)

def find_max(tests, tlist): # might need to fix tlist as its a dictionary now # can use key to point to value now.
    if tlist == []:
        return -1
    max_position = 0

    for t in tlist: #tlist is a dictionary now
        for test in tests:
            if test[0] == tlist[t]:
                t_position = test[1]
                if t_position > max_position:
                    max_position = t_position
#    print 'MAX'
#    print max_position
    return max_position

#call with - find_min(tests, subsequent_tests/ pre_tests)
#for each test in the pre or sub list find the position of that test in the main tests!
# compute the test with the min postion in tests

# def find_min(tests, test, tlist)
def find_min(tests, tlist): # might need to fix tlist as its a dictionary now # can use key to point to value now.
#    print xpos
    if tlist == []:
        return len(tests) + 1
    min_position = len(tests) + 1
#    print min_position

    for t in tlist: #tlist is a dictionary now
        for test in tests:
            if test[0] == tlist[t]:
                t_position = test[1]
                if t_position < min_position:
                    min_position = t_position

#    print 'MIN'
#    print min_position
    return min_position

########################### END OF COMPUTING MAX AND MIN VALUES ############################


##################################### SWAPPING TESTS #######################################
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

##################################### REORDER ALGORITHM #######################################
#Using Lists
def reorder(tests,pre_tests,sub_tests):
    print tests
#    print pre_tests
    for rx in tests:
        xpos = rx[1]
        x_prob_fail= float(rx[2])
        delta_max = 0
        delta_max_test = 0

        for ry in tests:
            new = 0
            ypos = ry[1]
            y_prob_fail = float(ry[2])

            if rx != ry:
                if xpos < ypos:
#                    print 'else xpos < ypos'
                    rx_sub_test_minpos = find_min(tests, sub_tests)
                    ry_pre_test_maxpos = find_max(tests, pre_tests) # FIND MAX find_max(tests, ry, pre_tests[])
                    if xpos > ry_pre_test_maxpos and ypos < rx_sub_test_minpos:
                        if x_prob_fail < x_prob_fail:
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
                    ry_sub_test_minpos = find_min(tests, sub_tests) #FIND MIN find_min(tests, rx, v[3:])
                    rx_pre_test_maxpos = find_max(tests, pre_tests) # FIND MAX find_max(tests, rx, pre_tests[])

                    if ypos > rx_pre_test_maxpos and xpos < ry_sub_test_minpos:
                        if x_prob_fail < xpos:
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

    return delta_max

##################################### END OF REORDER ALGORITHM ####################################

def main():

    compute_pre_tests(get_data(filename))
    print "with:"
    print pre_tests
    compute_subtest(tests,pre_tests)
    print sub_tests
#    reorder(get_data(filename),pre_tests, sub_tests)



if __name__ == '__main__':
    main()
