#!/usr/bin/env python
import sys

def countSleep(n):
    if n == 0:
        return "INSOMNIA"

    bucket=[ 0 for _ in range(10) ]
    i = 1 
    while not all(bucket):
        
        for digit in str(n * i ):
            bucket[int(digit)]=1
        
        i +=1
    
    return n * ( i-1 )

        
    

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    n = int ( fin.readline().strip() )  
    print "Case #%d: %s" % ( i+1 , countSleep(n) )
