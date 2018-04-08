import sys
    


def solv(N , data , data1):


    d = sorted( [ list(j) for j in data.items() ], key = lambda x: -x[1]  )
    
    rlt=[]

    
    if d[0][1] > N/2:
        return "IMPOSSIBLE"
    
    for i in range( d[2][1] ):
        for ii in range(3):
            rlt.append( d[ii][0] )
    
    for tmp in range(3):
        d[tmp][1] -= d[2][1]

    for i in  range( d[1][1] ):
        for ii in range(2):
            rlt.append( d[ii][0] )

    for tmp in range(2):
        d[tmp][1] -= d[1][1]
     
    # last insert
    idx =2  
    for i in range( d[0][1] ):
        rlt.insert(  idx , d[0][0] )
        idx +=4
    
    rlt = ''.join(rlt)
    rlt.replace( 'B', 'BOB', data1['O'] )
    rlt.replace( 'R', 'RGR', data1['G'] )
    rlt.replace( 'Y', 'YVY', data1['V'] )


    return ''.join(rlt)

        

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    N, R, O, Y, G, B, V  =  map(int,  fin.readline().strip().split() )
    data ={}
    data1 ={}

    data['R'] = R 
    data1['O'] = O 
    data['Y'] = Y 
    data1['G'] = G 
    data['B'] = B 
    data1['V'] = V 
    
    if data1['O'] > data['B'] or data1['G'] > data['R'] or data1['V'] > data['Y']:
        print "Case #%d: IMPOSSIBLE" % ( i+1 ) 
        continue

    data['B'] -= data1['O']
    data['R'] -= data1['G']
    data['Y'] -= data1['V']

    print "Case #%d: %s" % ( i+1 , solv(N, data, data1) )
