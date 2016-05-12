#!/bin/python3
import numpy
from random import random


def growth(t_index, h, gamma, k, mu):
    l = h.shape[0]
    rho = 1 + (k * numpy.exp((gamma / 2) * 2 - mu))
    grid = numpy.zeros((l, l, t_index))

    for t in range(t_index - 1):
        r = numpy.random.randint(10)
        c = numpy.random.randint(10)

        south = (h[r][c] <= h[(r+1) % l][c])
        north = (h[r][c] <= h[(r - 1) % l][c])
        east = (h[r][c] <= h[r][(c+1) % l])
        west = (h[r][c] <= h[r][(c - 1) % l])

        s = int(south) + int(north) + int(east) + int(west)
        w = 1
        wde = k * numpy.exp(((gamma / 2) * (2 - s)) - mu)

        rj = w + wde
        if random() <= (rj / rho):
            prob = numpy.array((wde, w)) / rj
            ch = numpy.random.choice(a=(-1, 1),
                                     size=1,
                                     replace=True,
                                     p=prob)
            h[r][c] = h[r][c] + ch

        grid[:, :, t] = h

    return grid
