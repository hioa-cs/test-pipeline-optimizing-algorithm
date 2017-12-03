#! /usr/bin/env python

valuelist = []
for value in range(1,10000):
    if value % 100 == 0:
        valuelist.append(value)

vfile = open('value.txt', 'w')

for item in valuelist:
  vfile.write("%s\n" % item)

vfile.close()
