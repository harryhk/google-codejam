import sys



def solv( D, N ):
    t =  -1
    for _ in range(N):
        k, s = fin.readline().strip().split()
        k = int(k)
        s = float(s)

        t = max( t, ( D - k ) / s )
    
    return D / t 
        

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    D,N =  fin.readline().strip().split()
    D = int(D)
    N = int(N)
    print "Case #%d: %.6f" % ( i+1 , solv(D, N) )
