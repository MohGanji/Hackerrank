# the problem is here:
# https://www.hackerrank.com/challenges/insertion-sort

#!/usr/bin/python

    
counter = 0
    
def merge(l, a, b, mid):
    global counter
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            l[k] = a[i]
            i, k = i+1, k+1
        else:
            l[k] = b[j]
            j, k = j+1, k+1
            counter += mid-i
            
    if i >= len(a):
        while j < len(b):
            l[k] = b[j]
            j, k = j+1, k+1
    else:
        while i < len(a):
            l[k] = a[i]
            i, k = i+1, k+1
            
    return l

def mergeSort(l):
    if len(l) <= 1:
        return l
    mid = len(l)/2
    a = mergeSort(l[:mid])
    b = mergeSort(l[mid:])
    l = merge(l, a, b, mid)
    return l

n = input()
for iterate in range( n ):
    x = input()
    a = [ int( i ) for i in raw_input().strip().split() ]
    a = mergeSort(a)
    #print a
    print counter
    counter = 0
