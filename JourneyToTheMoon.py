# the problem is here:
# https://www.hackerrank.com/challenges/journey-to-the-moon

#!/bin/bash/python

def DFS_Visit_Non_Recursive(graph, v, visited, countries):
    stack = [v]
    while stack:
        Node = stack.pop()
        if visited[Node]:
            continue
        visited[Node] = True
        countries[-1].append(Node)
        for i in graph[Node]:
            if not visited[i]:
                stack.append(i)
    return countries

def DFS_Visit(graph, v, visited, countries):
    visited[v] = True
    countries[-1].append(v)
    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            DFS_Visit(graph, graph[v][i], visited, countries)
    return countries

N,l = map(int,raw_input().split())

graph = [[] for i in range(N)]
visited = [False for i in range(N)]
for i in range(l):
    a,b = map(int,raw_input().split())
    graph[a].append(b)
    graph[b].append(a)
    
countries = []
    
for i in range(N):
    if not visited[i]:
        countries.append([])
        counteries = DFS_Visit_Non_Recursive(graph, i, visited, countries)
        
result = 0
for i in countries:
    #print i
    result += (N-len(i)) * len(i)

print result/2
