#!/bin/python3
import random
import numpy
from test_grid import test_grid
from pad import pad

def create_lattice(l, h, j, initial_lattice, 
        n_configs, n_usable_configs, t_tilde):
    
    config = numpy.zeros((l, l, n_configs))
    lattice = initial_lattice

    for x in range(0, n_configs):
        for t in range(0, l**2):
            r = random.random() * l
            c = random.random() * l
            new_lattice = lattice
            new_lattice[r, c] = new_lattice[r,c] * -1
            padded_new_lattice = pad(new_lattice)
            [accepted, accepted_prob] = test_grid(h, j, padded_new_lattice, r, c, t_tilde)
            if accepted:
                lattice = new_lattice
        lattice_full[:, :, x] = lattice
 
    size_z = lattice_full.shape[2]-1
    lattice_full = lattice_full[0][0][size_z-n_usable_configs+1:size_z]
    return lattice_full
