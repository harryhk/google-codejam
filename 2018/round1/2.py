import fileinput 

def  getUpperBound( cashiers, B ):
    
    return max(  [ c[1] * B + c[2]  for c in cashiers ] )

def getBits( cashiers, R, m ):
    
    a = [  min( c[0], ( m - c[2] ) / c[1] ) for c in cashiers  ]
    a = sorted( a , reverse = True )
    return sum( a[:R] )


def solve( R, B, cashiers ):
    
    #print R, B, cashiers

    end = getUpperBound( cashiers, B )
    start = 1

    while start < end:
        
        m = ( start + end ) /2 
        g = getBits( cashiers, R, m )
        #print start, m , end  , B, g 
        #print B > g

        if B >  g :
            start = m+1 
        else:
            end = m
            
    return end
    

def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for _ in range(n):
         R, B, C = map(int, d.readline().strip().split() )
        
         cashiers = []
         for ci in range(C):
            cashiers.append(  map(int , d.readline().strip().split() ) )
         print "Case #%d: %s" % ( (_+1), solve(R, B, cashiers) )

main()
