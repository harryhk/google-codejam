import fileinput 

def getCount( interval, left ):
    
    interval = sorted( interval )
    i = 0 
    while i < len( interval ):
        if left >= interval[i]:
            left -= interval[i]
        else:
            break
        i+=1

    return len(interval) - i

def solve( clist, jlist ):
    
    tot = [ c +[1] for c in clist ] + [ j+[2] for j in jlist ]

    tot = sorted( tot, key=lambda x: x[0] )
    tot.append( [ tot[0][0] +1440 , tot[0][1] +1440, tot[0][2] ] )

    cleft = 720 - sum( [ (j-i) for i, j in  clist ] )
    jleft = 720 - sum( [ (j-i) for i, j in  jlist ] )
    
    #print tot, cleft, jleft

    cinterval = []
    jinterval = []

    count=0

    for i in range( len(tot) -1 ):
        j = i+1
        ib, ie, iv = tot[i]
        jb, je, jv = tot[j]

        if ie == jb:
            if iv != jv:
                count +=1 

        else:
            if iv != jv:
                count +=1 

            else:
                if iv == 1:
                    cinterval.append( jb-ie  )
                else:
                    jinterval.append( jb-ie  )

    #print cinterval, jinterval
    
    

    return count + getCount( cinterval, cleft ) * 2 + getCount( jinterval, jleft ) * 2
                
                
        



def main():
    d =  fileinput.input()
    n = int( d.readline() )

    for case in range(n):
         Ac, Aj = map(int, d.readline().strip().split() )
         clist = []
         jlist = []      
         for _ in range(Ac):
            clist.append( map(int, d.readline().strip().split() ))
         for _ in range(Aj):
            jlist.append( map(int, d.readline().strip().split() ))
         print "Case #%d: %s" % ( (case+1), solve(clist, jlist) )

main()
