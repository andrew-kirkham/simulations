#!/bin/python3
import random

def create_lattice(l, h, j, initial_lattice, 
        n_configs, n_usable_configs, t_tilde):
    
    lattice = [[[0 for i in range(l)] for j in range(l)] for k in range(n_configs)]

    for x in range(1, n_configs):
        for t in range(1, l**2):
            r = random.random() * l
            c = random.random() * l
            new_lattice = lattice
            new_lattice(r, c) = new_lattice(r,c) * -1
            #padded_new_lattice = mpad(new_lattice)
            #[accepted, accepted_prob] = gridtest(h, j, padded_new_lattice, r, c, t_tilde
            if accepted:
                lattice = new_lattice
        lattice_full(1, 1, x) = lattice
    lattice_full = lattice_full(1, 1, range(end-n_usable_configs))
    return lattice_full
