'''
Created on Oct 9, 2014

@author: thainguyen
@email: nnthai94@gmail.com
'''
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = []
    product = 1
    zeros = 0
    for i in range(0,n):
        x = int(sys.stdin.readline())
        a.append(x)
        if x != 0:
            product *= a[len(a)-1]
        else:
            zeros += 1
    
    for num in a:
        if zeros > 1:
            print 0
        elif zeros == 1:
            if num == 0:
                print product
            else:
                print 0
        else:
            print product/num



