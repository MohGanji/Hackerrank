# the problem is here:
# https://www.hackerrank.com/challenges/sherlock-and-array

#!/bin/bash/python

T = int(raw_input())
for i in range(T):
    n = int(raw_input())
    a = map(int, raw_input().split(' '))
    sumRight, sumLeft, flag = 0, 0, True
    for j in a:
        sumRight += j
    for j in range(len(a)):
        sumRight -= a[j]
        if j:
            sumLeft += a[j-1]
        if sumRight == sumLeft:
            print "YES"
            flag = False
            break
    if flag:
        print "NO"
