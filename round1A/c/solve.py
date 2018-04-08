#!/usr/bin/env python
import sys

sys.setrecursionlimit(10000)

def dfs(i, depth, friends, visited, label, seen):
    if visited[i] == 1:
        if i in seen:
            return depth - label[i]
        else:
            return 0

    else:

        visited[i] =1 
        label[i]= depth
        nextnode = friends[i]
        seen.append(i)

        return dfs( nextnode , depth +1, friends, visited, label, seen )


def depth(i, befriended, depthMem ):
    if depthMem.has_key(i):
        return depthMem[i]

    if len(befriended[i] ) == 0:
        depthMem[i] = 1
        return 1

    else:
        m = 0
        for f in befriended[i]:
            m = max(m, depth(f, befriended, depthMem) )
        depthMem[i] = m+1
        return m+1
            

def BFF(friends):
    
    n = len(friends)
    friends = [ i-1 for i in friends ]
    visited = [ 0 for _ in range(n) ]
    label = [ 0 for _ in range(n) ]
    
    maxn = 0 
    for i in range(n):
        if visited[i] == 0 :
            maxn = max(maxn, dfs(i, 0, friends, visited, label, []) )
    
    # 2 cycle case 
    befriended = {}
    for i in range(n):
        befriended[i] = []

    for i, j in enumerate(friends):
        befriended[j].append(i)
    
    maxsum = 0
    visited_2 = [ 0 for _ in range(n) ]
    depthMem = {}
    for i in range(n):
        if visited_2[i] == 0 and friends[ friends[i] ] == i:
            befriended[i].remove( friends[i] )
            befriended[friends[i] ].remove(i)
            maxsum += depth(i, befriended, depthMem) + depth(friends[i], befriended, depthMem )
            visited_2[ friends[i] ] = 1

        visited_2[i] = 1 


    return max( maxn, maxsum ) 

    



fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    fin.readline()
    friends = map( int , fin.readline().strip().split() )
    print "Case #%d: %s" % ( i+1 , BFF(friends) )
