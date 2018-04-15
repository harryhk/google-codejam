import fileinput 


def getIter( agg, psum, N  ):
    rlt = [] 
    s = 0 ;
    i = 0;
    while i < len(agg):
        s += agg[i]
        if s > psum:
            raise RuntimeError
        if s == psum:
            rlt.append( i+1 )
            s = 0
        i+=1
    
    if  rlt[-1] != len(agg):
        raise RuntimeError
    
    rlt.insert(0, 0)
    #print rlt 
    return rlt 

def check( r, c, table, expect_sum ):
    rb, re = r
    cb, ce = c
    
    #print r, c, expect_sum
    s= 0

    for i in range( rb, re ):
        for j in range( cb, ce ):
            s += 1 if  table[i][j] == '@' else 0

    if s != expect_sum:
        raise RuntimeError
    


def solve( table, R, C, H, V ):
    
    row_agg = [ 0 for i in range(R) ]

    col_agg = [ 0 for i in range(C) ]


    for i in range( R ):
        for j in range(C):
            
            row_agg[i] += 1 if table[i][j] == '@' else 0
            col_agg[j] += 1 if table[i][j] == '@' else 0
    
    sum_row = sum( row_agg )
    sum_col = sum( col_agg )


    H +=1;
    V +=1;
    if  sum_row % H != 0 or sum_col % V != 0:
        return "IMPOSSIBLE"

    row_part_sum = sum_row / H 
    col_part_sum = sum_col / V 

    try: 
        row_inter = getIter( row_agg, row_part_sum , H )
        col_inter = getIter( col_agg, col_part_sum , V )
        
        expect_sum = sum_row / H / V

        for r in  zip( row_inter[:-1], row_inter[1:] ):
            for c in  zip( col_inter[:-1], col_inter[1:] ):
                check( r, c, table , expect_sum ) 
        
        return "POSSIBLE"


    except RuntimeError:
        return "IMPOSSIBLE"
        

    

def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for _ in range(n):
         R, C, H, V = map(int, d.readline().strip().split() )
         table = []
         for _i in range(R):
            table.append( [ i for i in  d.readline().strip() ] )
         print "Case #%d: %s" % ( (_+1), solve( table, R, C, H, V ) )

main()
