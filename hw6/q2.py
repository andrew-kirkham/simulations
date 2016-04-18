#!/bin/python3
import numpy
from random import random
from create_lattice import create_lattice
from pad import pad

def main():
    l = 15
    h = 0.1
    j = 1
    n_configs = 250
    n_usable_configs = 200
    temps = numpy.linspace(10, .5, 20) 
    specific_heat = numpy.zeros((len(temps), 1))

    previous_lattice = [[round(random()) * 2 -1 for x in range(l)] for y in range(l)]
    previous_lattice = numpy.array(previous_lattice)

    for index, temp in enumerate(temps):
        print(temp)
        lattice = create_lattice(l,h,j, previous_lattice, n_configs, n_usable_configs, temp)
        lattice_pad = numpy.zeros((l+2, l+2, n_usable_configs))

        for config in range(n_usable_configs):
            lattice_pad[:,:,config] = pad(lattice[:,:,config])
        
        end_x = lattice_pad.shape[0]-1
        end_y = lattice_pad.shape[1]-1
        north = lattice_pad[0:end_x-1,1:end_y,:]
        south = lattice_pad[2:end_x+1,1:end_y,:]
        east = lattice_pad[1:end_x,2:end_y+1,:]
        west = lattice_pad[1:end_x,0:end_y-1,:]

        f = -1 * h * numpy.sum(lattice)
        s = -1 * j/2 * numpy.sum(lattice * 
                (north + south + east + west))
        energy = (f+s)/n_usable_configs
        heat = (energy**2/n_usable_configs - energy**2)/(temp**2) 
        print(heat)
        specific_heat[index] = heat 
        previous_lattice = lattice[:,:,-1]



if __name__=='__main__':
    main()
