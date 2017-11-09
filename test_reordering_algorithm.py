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
    print "TEST DATA COLLECTED FROM FILE and Stored in List"
    print tests
    return tests


######################### GETTING SUB TESTS #########################

def get_subtest(testkey,pre_tests,k,origin):
    # ptest = one test list such as > C:'B','A'
    # pre_tests = is a dictionary of dependencies of each test
    # k = key
    ptest = pre_tests[testkey]

    if len(ptest) == 1 and ptest == '' :
        print "No known subtest for " + k + ", skipping"
        return

    for tname in ptest:
        # if k in sub_tests and tname not in sub_tests[k]: # the new sub_tests dictionary > A:'B','C','D' , B:'C','D', C:'', D:''
        if tname == k:
            print 'storing {} as a subtest for {} in get_subtest'.format(tname, origin)
            if not testkey in sub_tests[origin]:
                sub_tests[origin].append(testkey) # the new sub_tests dictionary > A:'B','C','D' , B:'C','D', C:'', D:''
            for ktest in pre_tests: # parsing pre_tests key / A,B,C,D
                get_subtest(ktest,pre_tests,testkey,origin)

def compute_subtest(tests,pre_tests):
    for k in pre_tests:     # k = key of pre_tests / A,B,C,D
        ptest = pre_tests[k] # ptest >> A:'',  B:'A',  C:'B','A',  D:'B','A'
        print k
        print ptest
#        if len(ptest) == 1 and ptest == '' :
#            print "No known subtest for " + k + ", skipping"
#            return
        for tname in ptest: # parsing pre_tests test data > tname > A:'',  B:'A',  C:'B','A',  D:'B','A'
            if tname == '' :
                print "No known pre test for " + k + ", skipping"
            else:
                print "tname " + tname
                if not tname in sub_tests:
                    sub_tests[tname] = []
                print "tname in compute sub_tests " + tname
                print 'storing {} as a subtest for {}'.format(k, tname)
                if not k in sub_tests[tname]:
                    sub_tests[tname].append(k) # the new sub_tests dictionary > A:'B','C','D' , B:'C','D', C:'', D:''
                print sub_tests
                for ktest in pre_tests:
                    get_subtest(ktest,pre_tests,k,tname)

    for k in pre_tests:     # k = key of pre_tests / A,B,C,D
        if not k in sub_tests:
            sub_tests[k] = []
#    print sub_tests
    return sub_tests

######################### END OF GETTING SUB TESTS #########################


############################## Getting pre_tests - dependencies for test ###############################

def get_dependencies(test,ptest,ptests):
    # ptests has the same thing as tests
    # test = the test we are searching on behalf of
    # ptest = a test we found down the dependencie line (ptest is a list containing everything about this test)
    # pre_list = is an empty list that is assigned the ptest[] list as found in test
    pre_list = []
    pre_list = ptest.split(',')[3:]
    print "pre_list"
    print pre_list
    # 1. get all known get_dependencies
    print "Finding all unknown dependencies for " + test + " from " + ptest[0]
    if len(pre_list) == 1 and pre_list[0] == '':
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
    print "======= STARTS COMPUTING PRE-TESTS ======="
    pre_list = []

    for r in ptests:
        r = r.split(',')
        pre_list = r[3:]
        print ptests
#        print "pre_list"
#        print pre_list
        sublen = len(pre_list)
        tname = r[0]
#        print "tname in pre_tests" + tname
        pre_tests[tname] = []
#        print "Finding all dependencies for " + tname
        if len(pre_list) == 1 and pre_list[0] == '':
            print "No known dependencies for " + tname + ", skipping"
        #    return # with this return it skips finding dependencies if pre_list is empty
#        print pre_list
        for t in pre_list:
            print pre_list
            print t
    #        t = t.split(',') #newly added for splitting, because t was printing and storing the commas as values
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

def find_max(tests, pos, tlist): # might need to fix tlist as its a dictionary now # can use key to point to value now.

    print "=== Finding MAX position for dependency list ==="
#    print tlist

    if tlist == []:
        return -1
    max_position = 0

    for t in tlist:
        for test in tests:
            test = test.split(',')
            if test[0] == t:
                t_position = test[1]
    #            print "test position: " + t_position
                if int(t_position) > int(max_position):
                    max_position = t_position
    #                print max_position

    print "Max position for list: "
    print max_position
    return max_position

# call with - find_min(tests, subsequent_tests/ pre_tests)
# for each test in the pre or sub list find the position of that test in the main tests!
# compute the test with the min postion in tests

def find_min(tests, pos, tlist):

    print "=== Finding MIN position for dependency list ==="
    print tlist

    if tlist == []:
        return len(tests) + 1
    min_position = len(tests) + 1
    print min_position

    for t in tlist:
        for test in tests:
            test = test.split(',')
            if test[0] == t:
                t_position = test[1]
#                print "test position: " + t_position
#                print min_position
                if int(t_position) < int(min_position):
                    min_position = t_position
                    print min_position

    print "Min postion for list: "
    print min_position
    return min_position

########################### END OF COMPUTING MAX AND MIN VALUES ############################

############ find POSITION #############

def find_xpos(tests,tx):
    tlen = len(tests)
    print 'Finding position of x for swapping'
    i = 0
#    print tests

    for t in tests:
        print t
        print tx
        print t[0:2]
        print tx[0]
        if tx[0] == t[0:2]:
            xpos = i

        i = i+1
    print xpos
    return int(xpos)


def find_ypos(tests,ty):
    tlen = len(tests)
    print 'finding position of y for swapping'
    i = 0
#    for i in range(tlen):
#        print i
    for t in tests:
        print t
        if ty[0] == t[0:2]: # testname sizes can't be limited to 1 or 2 letters?
            print t[0]
            print ty[0]
            ypos = i
        i = i+1
    print ypos
    return int(ypos)


##################################### SWAPPING TESTS #######################################
#tests is the array of tests
# rx position of test x
# ry positon of test y
def swap(tests, tx, ty):
    print "Swapping is Valid, therefore SWAPPING tests:"
    print tx, ty
    temp = []
    t = []
    xpos = find_xpos(tests,tx)
    ypos = find_ypos(tests,ty)
    print xpos, ypos
#    t = tx
    temp = tests[xpos]
#    tx = ty
    tests[xpos] = tests[ypos]
#    ty = t
    tests[ypos] = temp
#    print tx, ty
    return tests


##################################### REORDER ALGORITHM #######################################
#Using Lists
def reorder(tests,pre_tests,sub_tests):
    print " ====== ***** Running Reorder Algorithm ***** ======"
    print tests
    for rx in tests:
        rx = rx.split(',')
        txname = rx[0]
        xpos = int(rx[1])
        x_prob_fail= float(rx[2])
        delta_max = 0
        delta_max_test = 0
        for ry in tests:
            ry = ry.split(',')
            tyname = ry[0]
            delta_new= 0
            ypos = int(ry[1])
            y_prob_fail = float(ry[2])
            if rx != ry:
                if xpos < ypos:
            #        print 'xpos < ypos'
            #        print 'sub_tests testname : '
            #        print sub_tests[txname]
                    # if there are no dependencies these functions return zero
                    rx_sub_test_minpos = int(find_min(tests, xpos, sub_tests[txname]))
                    ry_pre_test_maxpos = int(find_max(tests, ypos, pre_tests[tyname]))
                #    print "print max and min"
                #    print rx_sub_test_minpos
                #    print ry_pre_test_maxpos
                # if there are no dependencies at all the loop fails to continue
                    if int(xpos) > int(ry_pre_test_maxpos) and int(ypos) < int(rx_sub_test_minpos):
                        print "Comparing positions of tests for swapping"
                        if float(y_prob_fail) > float(x_prob_fail) :
                            # new value of decrease in time by doing swapping
                            # difference in test positions - difference in porbability of a test failing
                            delta_new = (y_prob_fail - x_prob_fail) * (ypos - xpos)
                    #        print "delta new "
                    #        print delta_new
                            if delta_max < delta_new:
                                delta_max = delta_new
                                delta_max_test = ry
#                                print delta_max_test
                    #            print "DELTA MAX = "
                    #            print delta_max
                else:
                #    print 'xpos > ypos'
                #    print 'sub_tests test name : '
                #    print sub_tests[txname]
                    ry_sub_test_minpos = int(find_min(tests, ry, sub_tests[txname]))
                    rx_pre_test_maxpos = int(find_max(tests, rx, pre_tests[txname]))
                #    print "print max and min"
                #    print ry_sub_test_minpos
                #    print rx_pre_test_maxpos
                    if int(ypos) > int(rx_pre_test_maxpos) and int(xpos) < int(ry_sub_test_minpos):
                        print "Comparing positions of tests for swapping"
                        if float(x_prob_fail) > float(y_prob_fail) :
                            delta_new = (x_prob_fail - y_prob_fail) * (xpos - ypos)
                        #    print "delta new "
                        #    print delta_new
                            if delta_max < delta_new:
                                delta_max = delta_new
                                delta_max_test = ry # the whole test and its elements
                        #        print "DELTA MAX = "
                        #        print delta_max_test

        if delta_max > 0:
            tests = swap(tests, rx, delta_max_test)
            print tests

#        else:
#            continue

    print " ====== Finished Running Reorder Algorithm ======"
    print " ====== Returning delta_max ======"
    print delta_max
    return delta_max

##################################### END OF REORDER ALGORITHM ####################################

def main():

    compute_pre_tests(get_data(filename))
    print "pre_tests:"
    print pre_tests
    print "======== STARTS COMPUTING SUB TESTS ======="
    compute_subtest(tests,pre_tests)
    print "sub_tests:"
    print sub_tests
    print "before swapping"
    print tests
    reorder(tests, pre_tests, sub_tests)
    print "after swapping:"
    print tests

#    sorted_tests = sorted(tests, key=operator.itemgetter(2))
#    print "Sorted based on Test Position number: "
#    print sorted_tests

#    print "Storing sorted list to sorted_testlist.csv"

#    with open('sorted_testlist.csv', 'w') as f:
#        for s in sorted_tests:
#            f.write(s + '\n')


if __name__ == '__main__':
    main()
