# The problem is here:
# https://www.hackerrank.com/contests/codeagon/challenges/robber-and-warehouse

#!/bin/python

import sys


n,c = map(int, raw_input().strip().split(' '))
crate = []
for crate_i in xrange(c):
	t, p = map(int,raw_input().strip().split(' '))
	crate.append((t, p))
sum =0
crate = sorted(crate, key= lambda x : x[1], reverse=True)
for i in crate:
	if n == 0:
		break
	if n >= i[0]:
		sum += i[0] * i[1]
		n -= i[0]
	elif n < i[0]:
		sum += i[1] * n
		n = 0

print sum

