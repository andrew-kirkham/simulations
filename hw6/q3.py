#!/bin/python3
import numpy
from create_lattice import create_lattice
from random import random

def main():
    l=15
    h=0.1
    j=1
    n_configs = 250
    n_usable_configs = 200

    temps = numpy.linspace(10,0.5,40)
    magnetism = numpy.zeros((len(temps),1))

    previous_lattice = [[round(random())*2 -1 for x in range(l)] for y in range(l)]
    previous_lattice = numpy.array(previous_lattice)

    for index, temp in enumerate(temps):
        print(temp)
        lattice = create_lattice(l,h,j,previous_lattice, n_configs, n_usable_configs, temp)
        mag = numpy.sum(lattice)/(l**2)
        magnetism[index] = mag/n_usable_configs
        
        #q4 below
        mag = numpy.mean(mag**2)
        susceptibility[index] = (mag - mean(mag)**2)/(temp**2)
        previous_lattice = lattice[:,:,-1]


if __name__=='__main__':
    main()
