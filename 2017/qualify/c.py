import sys


def solve( n, k ):
    n = int(n)
    k = int(k)
    d = { n: 1 }

    while True:
        #print d
        space = sorted( d.keys(), reverse=True )[0]
            
        if space ==1:
            return ( 0, 0)

        curr_n = d.pop( space )
        space = space -1
        small = space/2
        large = space - small

        if k <= curr_n:
            # split and return
            return ( large, small)

        else:
            # split and reduce k
            d[small] = d.get(small , 0 ) + curr_n 
            d[large] = d.get(large,  0 ) + curr_n 
            k = k - curr_n




fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    n,k =  fin.readline().strip().split()
    r_max, r_min = solve(n,k)
    print "Case #%d: %s %s" % ( i+1 , r_max, r_min )
