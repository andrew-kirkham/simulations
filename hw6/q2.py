#!/bin/python3
import numpy
import plotly
from plotly.graph_objs import Scatter, Layout
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
    stable_spins = numpy.zeros((len(temps),1))

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
        specific_heat[index] = heat 
        
        #q5
        spin = (lattice==north) & (lattice==south) & (lattice==east) & (lattice==west)
        stable_spins[index] = numpy.sum(spin)/n_usable_configs
        
        previous_lattice = lattice[:,:,-1]
    
    plotly.offline.plot({
        "data": [ Scatter(x=temps, y=specific_heat, mode="markers") ],
        "layout": Layout(title="Specific Heat")
        }, filename="q2.html")
    plotly.offline.plot({
        "data": [ Scatter(x=temps, y=stable_spins, mode="markers")],
        "layout": Layout(title="Stable Spins")
        }, filename="q5.html")
    
if __name__=="__main__":
    main()
