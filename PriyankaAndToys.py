# The problem is here:
# https://www.hackerrank.com/challenges/priyanka-and-toys

n = int(raw_input())
a = sorted(map(int, raw_input().split(' ')))

i = 0
count = 0
curr = -5

while i < n:
	if curr <= a[i] and a[i] <= curr+4:
		i += 1
		continue
	curr = a[i]
	i += 1
	count += 1

print count
