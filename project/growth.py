#!/bin/python3
import numpy
from random import random

def growth(t_index, h, gamma, k, mu):
    l = numpy.size(h, 1)
    rho = 1 + (k * numpy.exp((gamma/2)*2 - mu))
    grid = numpy.zeros(l, l, t-index-1)

    for t in range(t_index-1):
        r = random() * 10
        c = random() * 10

        south = (h[r][c] <= h[r % l + 1][c])
        north = (h[r][c] <= h[(r-2) % l + 1][c])
        east = (h[r][c] <= h[r][c % l + 1])
        west = (h[r][c] <= h[r][(c-2) % l + 1])

        s = south + north + east + west
        w = 1
        wde = k * numpy.exp(((gamma/2) * (2-s)) - mu)
        
        rj = w + wde
        if random() <= rj/rho:
            c = numpy.random.choice(a=(-1,1),
                    size=1,
                    replace=True,
                    p=numpy.array((wde, w))/rj)
            h[r][c] = h[r][c] = c
        grid[:][:][t_index]=h

    return grid
