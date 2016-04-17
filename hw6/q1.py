#!/bin/python3
import numpy
from create_lattice import create_lattice
from pad import pad

def main():
    l = 15
    h = 0.1
    j = 1
    n_configs = 250
    n_usable_configs = 200
    temp_range = range(1, 20)
    temp_range = [x/2 for x in temp_range]
    energy = numpy.zeros((len(temp_range), 1))
    initial_energy = numpy.ones((l, l))
    last_lattice = initial_energy
    
    for iTemp in reversed(range(len(temp_range))):
        print(temp_range[iTemp])
        lattice = create_lattice(l, h, j, last_lattice, n_configs, n_usable_configs, temp_range[iTemp])
        lattice_pad = numpy.zeros((l+2, l+2, n_usable_configs))
        for config in range(n_usable_configs):
            lattice_pad[:,:,config] = pad(lattice[:,:,config])
        
        end_x = lattice_pad.shape[0]-1
        end_y = lattice_pad.shape[1]-1
        north = lattice_pad[0:end_x-1,1:end_y,:]
        south = lattice_pad[2:end_x+1,1:end_y,:]
        east = lattice_pad[1:end_x,2:end_y+1,:]
        west = lattice_pad[1:end_x,0:end_y-1,:]
        
        f = -1 * h * numpy.sum(numpy.sum(lattice))
        s = -1 * j/2 * numpy.sum(numpy.sum(lattice * 
            (north + south + east + west)))
        energy_temp = f + s
        energy_temp = numpy.sum(energy_temp)/n_usable_configs
        energy[iTemp] = energy_temp
        print('energy for ', temp_range[iTemp], ' = ', energy_temp)
        last_lattice = lattice[:,:,-1]
    print(energy)

if __name__=='__main__':
    main()
