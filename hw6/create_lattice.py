#!/bin/python3
import random
import numpy
from test_grid import test_grid
from pad import pad

def create_lattice(l, h, j, initial_lattice, 
        n_configs, n_usable_configs, t_tilde):
    
    lattice = numpy.zeros((l, l, n_configs))

    for x in range(1, n_configs):
        for t in range(1, l**2):
            r = random.random() * l
            c = random.random() * l
            new_lattice = lattice
            new_lattice[r, c] = new_lattice[r,c] * -1
            padded_new_lattice = pad(new_lattice)
            [accepted, accepted_prob] = test_grid(h, j, padded_new_lattice, r, c, t_tilde)
            if accepted:
                lattice = new_lattice
        lattice_full[1, 1, x] = lattice
    lattice_full = lattice_full(1, 1, range(end-n_usable_configs))
    return lattice_full
