#!/bin/python3
import random
import numpy

def test_grid(h, j, lattice, r, c, temp_tilde):
    r = r+1
    c = c+1
    sigma = lattice[r][c]
    d_u = -((2*h*sigma) + 
            (2*j*sigma*(lattice[r+1][c] + lattice[r-1][c]) + 
                lattice[r][c+1] + lattice[r][c-1]))
    q = numpy.exp(-d_u/temp_tilde)
    probability = numpy.min(1, q)

    outcome = (random.random() <= probability)
    return [outcome, probability]
