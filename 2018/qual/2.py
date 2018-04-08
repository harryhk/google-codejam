import fileinput 

def solve( D ):
    
    D1 = sorted(D[::2] )
    D2 = sorted(D[1::2])
    
    for i in range( len(D) -1 ):
        if i % 2 == 0 :
            n1 = D1[i/2]
            n2 = D2[i/2]
            if n1 > n2:
                return i
        else:
            n1 = D2[i/2]
            n2 = D1[i/2+1]
            if n1 > n2:
                return i
            
    return "OK"


def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for _ in range(n):
         d.readline()
         D = map(int, d.readline().split() )
         print "Case #%d: %s" % ( (_+1), solve( D ) )

main()
