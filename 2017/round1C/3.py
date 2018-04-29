import fileinput 
from collections import Counter


def solve( N, K,U, table ):
    
    tc = Counter( table )

    keys = sorted( tc.keys() ) + [1.0]

    #print tc, N,K,U, keys

    i = 0

    while keys[i] < 1.0:
        j = i+1

        step = keys[j] - keys[i]
        if U >= step * tc[ keys[i] ]:
            U -= step * tc[  keys[i] ] 
            #print U, keys[i], keys[j]
            tc[ keys[j] ] += tc[ keys[i] ]
            tc.pop( keys[i] )
        else:
            break

        i+=1
    
    #print tc

    if keys[i] < 1.0 and U > 1e-6 :
        old_k = keys[i]
        new_k = keys[i] + U / tc[ old_k ]

        tc[ new_k ] = tc[ old_k]
        tc.pop( old_k )

    #print tc
    
    p = 1
    for k ,v in tc.items():
        for _ in range( v ):
            p *= k 

        
        

    return p




    

def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for case in range(n):
         N, K = map(int, d.readline().strip().split() )
         U = float( d.readline().strip() )
         table = map( float, d.readline().strip().split() )
         print "Case #%d: %.10f" % ( (case+1), solve(N,K,U, table ) )

main()
