#!/usr/bin/env python
import sys
import numpy as np
from copy import deepcopy

def fill_array(array, tofill, i):
    print "tofill", tofill , 'i', i
    row = array[i]
    col = [ _[i] for _ in array ]

    while len( tofill ) > 0:
        line = tofill[0]
        if row[:i+1] == line[:i+1]:
            print row, line
            print 'array', array
            for ii in range(n):
                array[i][ii] = line[ii]
            print 'array', array
            tofill.remove(line)
            continue
        if col[:i+1] == line[:i+1]:
            print col, line
            for ii in range(n):
                array[ii][i] = line[ii]
            tofill.remove(line)
            continue


            
    



def fill_diag( array, lines_org):
    i=0 
    lines = deepcopy( lines_org )
    while len(lines) > 0:
        aMin = min( l[i] for l in lines)
        array[i][i] = aMin
        
        tofill = [ l[:] for l in lines if l[i] == aMin ]
        fill_array( array, tofill, i )

        lines = [ l for l in lines if l[i] != aMin ]
        i +=1
    
        
    

def RF(n, lines ):
    array = [ [ 0 for ii in range(n) ]   for i in range(n) ]

    fill_diag( array, lines)

    print array

    

    

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    n = int(fin.readline().strip())
    lines = []
    for _ in range(2*n-1):
        lines.append( map(int , fin.readline().strip().split())   )
        
    print "Case #%d: %s" % ( i+1 , RF(n, lines) )
