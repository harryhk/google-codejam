#!/usr/bin/env python
import sys
from itertools import product
from bisect import bisect_left

def getPrimeTable():
    table = []
    for line in  open('prime10000.txt'):
        table.extend( map(int, line.strip().split() ) )

    return table

def find_divisor(num):
    for i in primetable:
        if i < num and num % i == 0:
            return i


def jam(n, j):
    rlt = []
    count =0
    for case in product( ('0', '1') , repeat=n-2):
        num = ('1',) + case + ('1',)
        num = ''.join(num)
        divisor=[]
        flag=True
        for base in range(2, 11):
            num_base = int( num, base)
            print bisect_left(primetable,num_base)
            
            if num_base == primetable[bisect_left(primetable,num_base)]:
                flag = False
                break 
            else:
                d = find_divisor(num_base)
                print num, base, num_base, d
                divisor.append( d ) 

        if flag:
            rlt.append( [num, divisor]  )
            count +=1
        if count >=j:
            break

    for i, j in rlt:
        sys.stdout.write('%s ' % i )
        for jj in j:
            sys.stdout.write('%d '% jj )
        print

        
    
primetable = getPrimeTable()
print len(primetable)

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    n, j  = map( int , fin.readline().strip().split() )
    print "Case #%d:" % ( i+1 ) 
    jam(n, j)
