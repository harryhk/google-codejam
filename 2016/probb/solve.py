#!/usr/bin/env python
import sys

def flips( pancakes, target ):
    if len(pancakes) == 1:
        return 0 if pancakes[0] == target else 1

    if pancakes[-1] == target:
        return flips( pancakes[:-1], pancakes[-1] )
    else:
        return flips( pancakes[:-1], pancakes[-1] ) + 1
    

        
    

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    pancakes = fin.readline().strip() 
    pancakes = [ _ for _ in pancakes ]
    print "Case #%d: %s" % ( i+1 ,  flips(pancakes, '+') )
