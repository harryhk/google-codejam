import fileinput 
import math

def agg( newInter ):
    
    newInter = sorted( newInter, key=lambda x: x[0] )

    b = newInter[0][0]
    e = newInter[0][1]

    idx = 1
    aggRange = []
    while idx < len( newInter ):
        if newInter[idx][0] <= e:
            e = newInter[idx][1]
        else:
            aggRange.append( ( b, e  ) )
            b, e = newInter[idx]

        idx +=1
    
    aggRange.append( (b,e ))

    return aggRange
            
            


def update( intervals, rec ):
    
    H, W = rec 
    mini = min( H, W )
    maxi = math.sqrt( H * H + W * W ) 

    newInter = []

    for inter in intervals:
        
        newInter.append( inter )
        newInter.append( ( inter[0] + mini, inter[1] + maxi ) )


    return agg( newInter )

def findBound( intervals, target ):
    
    #print intervals, target
    best = 0
    b = 0;
    e = 0;
    idx = 0

    while idx < len( intervals ):
        b, e = intervals[idx]
        if e <= target:
            best = e
        else:
            break
        idx +=1

    if e <= target:
        return e

    if b <= target :
        return target
    else:
        return best
            



def solve( rects, P  ):
    
    tot = 2* sum( [ r[0] + r[1] for r in rects ] )
    target = ( P - tot )/ 2.0

    intervals = [(0,0)]

    for rec in rects: 
        
        intervals = update( intervals, rec )

    #print intervals
    
    return findBound( intervals, target ) * 2  + tot 
    
    

def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for _ in range(n):
         N, P  = map(int, d.readline().strip().split() )
        
         rects = []
         for ni in range(N):
            rects.append(  map(int , d.readline().strip().split() ) )
         print "Case #%d: %f" % ( (_+1), solve(rects, P ) )

main()
