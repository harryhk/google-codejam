import sys 
import copy


def fill_data( data2, r1, c1, r2, c2, c  ):
    
    for i in range( r1, r2+1):
        for j in range( c1, c2+1 ):
            data2[i][j] = 
            

    

def solve(r ,c ):
    data = []
    for line in range(r):
        data.append( [ i for i in sys.stdin.readline().strip()  ] )
    
    data2 = copy.deepcopy(data)
    pos = {}
    for i in range(r):
        for j in range(c):
            kid = data[i][j] 
            if kid == '?':
                if pos.has_key(kid):
                    # update
                    r1, c1, r2, c2 = pos[kid]
                    r1 = min( i, r1 )
                    c1 = min( j, c1 )
                    r2 = max( i, r2 )
                    c2 = max( j, c2 )
                    pos[kid] = ( r1, c1, r2, c2 )

                else:
                    pos[kid]=[ i, j , i, j   ]

    fill_data( data2, pos )

        



cases = int( sys.stdin.readline().strip() )
for i  in range(cases):
    r,c =  sys.stdin.readline().strip().split()
    r  = int(r)
    c  = int(c)

    print "Case #%d: " % ( i+1  )
    solve( r, c )
