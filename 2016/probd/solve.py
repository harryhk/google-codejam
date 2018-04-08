#!/usr/bin/env python
import sys
import math

def tiles( length, complexity):
    rlt=[] 
    for i in range(1, length+1):
        tmp = i
        for c in range(complexity-1):
            tmp = (tmp -1 ) * length + i

        rlt.append(tmp)

    return " ".join(map(str, rlt) )
        


fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    length, complexity, students = map( int , fin.readline().strip().split() )
    print "Case #%d: %s" % ( i+1 , tiles(length, complexity )) 
