import fileinput 


def solve( N, K, table ):
    print table
    

def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for case in range(n):
         N, K = map(int, d.readline().strip().split() )
         table = []
         for _ in range(N):
            table.append( map(int, d.readline().strip().split() ))
         print "Case #%d: %s" % ( (case+1), solve(N,K, table ) )

main()
