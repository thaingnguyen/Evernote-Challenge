'''
Created on Oct 9, 2014

@author: thainguyen
@email: nnthai94@gmail.com
'''
import sys 
from operator import itemgetter

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    words = {}
    for i in range(0,n):
        word = sys.stdin.readline().rstrip("\n")
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    k = int(sys.stdin.readline())
    res = []
    for word in words:
        res.append((words[word],word))
    res  = sorted(res, key=itemgetter(1))
    res  = sorted(res, key=itemgetter(0), reverse=True)
    for i in range(0, k):
        (freq, word) = res[i]
        print word