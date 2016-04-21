#!/bin/python3
import numpy

def part1():
    accept_a = []
    accept_b = []
    for i in range(10000):
        x = []
        for i in range(3):
            x.append(numpy.random.exponential())
        c = x[0]+2*x[1] +3*x[2]
        if (c > 15):
            accept_a.append(c)
        if (c < 1):
            accept_b.append(c)
    print('mean part a = ', numpy.mean(accept_a))
    print('mean part b = ', numpy.mean(accept_b))

if __name__=='__main__':
    part1()
