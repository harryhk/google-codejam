import fileinput 
import sys
import math


def checkLeft( table, i , j ):
    
    return table[i][j-1] == 'T' and \
           table[i+1][j-1] == 'T' and \
           table[i-1][j-1] == 'T'

def calcNew( table, i, j ):
    if any(  [ table[i+d][j] == 'x' for d in [-1,0,1] ] ):
        return (i, j+1)

    if any(  [ table[i+d][j+1] == 'x' for d in [-1,0,1] ] ):
        return (i, j+2)

    return (i, j+3)

def solve( a, inputd ):
    row = [ 'x' for i in range(200) ] 
    table= [ row[:] for i in range(10 ) ] 
    
    i, j = (2,2)

    jMax = int( math.ceil(a / 3.0 ) ) -1 

    while True:
        print "%s %s" % ( i, j )
        sys.stdout.flush()

        ii, jj = map(int,  inputd.readline().split() )


        if (ii, jj ) == (-1, -1 ):
            sys.exit(1)
        elif ( ii, jj ) == (0, 0):
            return 
        else:
            table[ii][jj] = 'T'

        if  checkLeft( table, i, j ):
            i, j = calcNew( table, i, j )
            j = min( j, jMax)

def main():
    #d =  fileinput.input()
    d =  sys.stdin 
    n = int( d.readline() )


    for _ in range(n):
         
        a = int( d.readline() )
        solve(a, d)

main()
