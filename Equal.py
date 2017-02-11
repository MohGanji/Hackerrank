# The problem is here:
# https://www.hackerrank.com/challenges/equal

def count(a):
	ans = a/5
	a = a%5
	ans += a/2
	a = a%2
	ans += a
	return ans

q = int(raw_input())
for qs in range(q):
	n = int(raw_input())
	a = map(int, raw_input().strip().split())
	
	minimum = min(a)
	
	for i in range(len(a)):
		a[i] -= minimum
	
	ans = [0 for i in range(3)]
	
	for p in range(3):
		for i in range(len(a)):
			ans[p] += count(a[i])
			a[i] += 1
	
	print min(ans)
