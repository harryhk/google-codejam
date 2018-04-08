import sys

def find_out_order( tmp ):
    i = -1
    flag = False
    for i in range( len(tmp) -1 ):
        if tmp[i] > tmp[i+1]:
            flag = True
            break
    return i if flag else -1

def get_no_equal( tmp, pos):
    while pos > 0 :
        if tmp[pos-1] == tmp[pos]:
            pos = pos -1
        else:
            break
    return pos

def getL(n):
    tmp = [ i for i in n ]
    pos = find_out_order( tmp )
    if pos != -1:

        pos = get_no_equal( tmp, pos)
        if pos < len(tmp) -1:
            for i in range( pos, len(tmp) ):
                if i == pos:
                    tmp[i] = str( int( tmp[i] ) - 1)
                else:
                    tmp[i] = '9'

    return int( ''.join(tmp) )
        

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    n =  fin.readline().strip() 
    print "Case #%d: %s" % ( i+1 , getL(n) )
