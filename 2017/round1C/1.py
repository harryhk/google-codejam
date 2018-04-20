import fileinput 
import numpy as np
import math
import sys

def getW( k, n, table):
    R, H = table[n-1] 

    if k == 1 :
        return R*R + 2 * R * H 
    
    return 2* R * H

def solve( N, K, table ):
    L = np.zeros( (K+1, N+1), dtype=int) 
    

    for k in range(1, K+1 ):
        for n in range( k, N+1):
            if k == n :
                L[k][n] = L[k-1][n-1] + getW(k,n, table)
            else:
                L[k][n] = max( L[k][n-1], L[k-1][n-1] + getW(k,n, table) )

    return L[K][N] * np.pi  
    

def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for case in range(n):
         N, K = map(int, d.readline().strip().split() )
         table = []
         for _ in range(N):
            table.append( map(int, d.readline().strip().split() ))
         
         table = sorted( table, key = lambda x:x[0], reverse=True )
         print "Case #%d: %.10f" % ( (case+1), solve(N,K, table ) )

main()
