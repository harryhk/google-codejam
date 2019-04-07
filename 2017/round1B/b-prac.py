import fileinput 
from collections import Counter

def solveRYB( data ):
    
    key = [ i[0] for i in  sorted( data.items(), key=lambda x: -x[1] ) ]
    
    k1, k2 , k3 = key
    total = sum( data.values() )

    if data[k1] > total / 2 :
        return "IMPOSSIBLE"

    rlt = [ '*' for i in range(total) ]
    idx = 0
    count = total  
    keyIdx=0

    while count > 0:
        
        if idx >= total:
            idx = 1
        
        if data[key[keyIdx]] == 0 :
            keyIdx +=1

        rlt[idx] = key[keyIdx]

        idx +=2
        count -=1
        data[key[keyIdx]] -= 1

    return rlt 


def solve( data, data1 ):
    
    return ''.join(solveRYB( data ) )

    

def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for case in range(n):
        N, R, O, Y, G, B, V  =  map(int,  d.readline().strip().split() )

        data ={}
        data1 ={}

        data['R'] = R 
        data1['O'] = O 
        data['Y'] = Y 
        data1['G'] = G 
        data['B'] = B 
        data1['V'] = V 

        print "Case #%d: %s" % ( (case+1), solve(data, data1 ) )

main()
