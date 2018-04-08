import fileinput 

def score(P):
    D = 0 ;
    B = 1 ;
    for i in P :
        if i == "S":
            D += B
        else:
            B *= 2
    return D

def findSwap( P ):
    
    i = len(P) -1 
    while i  > 0:
        if P[i] == 'S' and P[i-1] == 'C':
            break
        i = i-1
    return i

def swap( P , idx ):
    tmp = P[idx] 
    P[idx] = P [idx-1]
    P[idx-1] = tmp 

def solve( D, P ):
    c = 0 ;
    P = [ _ for _ in P ]
    idx = findSwap( P )

    while score(P) > D and idx > 0 :
        swap( P, idx )
        idx = findSwap( P ) 
        c +=1 

    return c if score(P) <= D else "IMPOSSIBLE"


def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for _ in range(n):
         D, P = d.readline().strip().split()
         print "Case #%d: %s" % ( (_+1), solve( int(D), P ) )

main()
