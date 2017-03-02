# The problem is here:
# https://www.hackerrank.com/challenges/30-regex-patterns
#   This was perticularly enkoyable for me cause it was my first attempt
#   on regex

#!/bin/python

import sys
import re

N = int(raw_input().strip())
	names = []
	for a0 in range(N):
		firstName,emailID = raw_input().strip().split(' ')
		firstName,emailID = [str(firstName),str(emailID)]
		obj = re.search(r'.*@gmail.com$', emailID)
		if obj:
			names.append(firstName)


names = sorted(names)
for name in names:
	print name

