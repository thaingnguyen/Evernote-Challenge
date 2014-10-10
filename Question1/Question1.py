'''
Created on Oct 9, 2014

@author: thainguyen
@email: nnthai94@gmail.com
'''

import sys

if __name__ == '__main__':
    size = int(sys.stdin.readline())
    current_size = 0
    queue = []
    for i in range(0,size):
        queue.append(None)
    begin_queue = 0
    end_queue = -1
    while True:
        line = sys.stdin.readline().rstrip('\n').split(" ")
        cmd = line[0]
        if cmd == 'A':
            n = int(line[1])
            current_size += n
            if current_size > size:
                begin_queue = (begin_queue + (current_size-size)) % size
                current_size = size
            for i in range(0,n):
                word = sys.stdin.readline().rstrip('\n')
                end_queue = (end_queue + 1) % size
                queue[end_queue] = word
        elif cmd == 'R':
            n = int(line[1])
            current_size -= n
            begin_queue = (begin_queue + n) % size
        elif cmd == 'L':
            idx = begin_queue
            while (idx != end_queue):
                print queue[idx]
                idx = (idx + 1) % size
            print queue[idx]
        elif cmd == 'Q':
            break

