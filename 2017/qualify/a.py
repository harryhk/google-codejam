import sys

def flip(s, pos, k):
    tmp = [ i for i in s ]
    for i in range( pos, pos+k):
        if tmp[i] == '-':
            tmp[i] = '+'
        else:
            tmp[i] = '-'

    return ''.join(tmp)


def flips( s, k ):
    k = int(k)
    pos = 0
    count =0
    while True:
        pos = s.find( '-', pos )
        if pos == -1 or pos > len(s) -k:
            break
        s = flip(s, pos, k)
        count +=1
        pos +=1

    for i in s:
        if i == '-':
            return "IMPOSSIBLE"

    return count

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    s,k =  fin.readline().strip().split()
    print "Case #%d: %s" % ( i+1 , flips(s, k) )
