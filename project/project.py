#!/bin/python3
import numpy
from random import random
from growth import growth
from pad import pad

def main():
    l = 10
    k = 1
    n = l**2
    mu = 0.5
    nu = 1
    t_max = 10
    h0 = numpy.zeros((l, l))
    gamma = 4
    rho = 1 + (k * numpy.exp((gamma/2)*2 - mu))

    #yes lambda is spelled wrong, but it is a reserved keyword in python
    lamda = 1/(n*rho)
    num_tests = 10

    t=0
    t_index = 0

    temps = numpy.zeros((10**5, 1))
    while (t<= 20):
        temps[t_index] = t
        t_index += 1
        temp = -numpy.log(random()/(1/lamda))
        t = t + temp

    avg_list = numpy.zeros((t_index, num_tests))
    avg_vs_gamma = numpy.zeros((t_index, num_tests, 1))
    rough_list = numpy.zeros((t_index, num_tests))
    rough_vs_gamma = numpy.zeros((t_index, num_tests, 1))
    mono_layer_list = numpy.zeros((t_index, num_tests))
    mono_layer_vs_gamma = numpy.zeros((t_index, num_tests, 1))
    coverage_list = numpy.zeros((t_index, num_tests))
    coverage_vs_gamma = numpy.zeros((t_index, num_tests, 1))

    for iGamma in range(1):
        
        for iTest in range(num_tests):
            grid = growth(t_index, h0, gamma, k, mu)
            h_pad = numpy.zeros((l+2, l+2, t_index))

            for i in range(t_index-1):
                h_pad[:, :, i] = pad(grid[:, :, i])

            end_x = h_pad.shape[0]-1
            end_y = h_pad.shape[1]-1
            north = h_pad[0:end_x-1, 1:end_y, :]
            south = h_pad[2:end_x+1, 1:end_y, :]
            east  = h_pad[1:end_x, 2:end_y+1, :]
            west  = h_pad[1:end_x, 0:end_y-1, :]

            rough_list[:, t_index] = numpy.sum((
                    numpy.abs(grid - north) +
                    numpy.abs(grid - south) +
                    numpy.abs(grid - east) +
                    numpy.abs(grid - west) /
                    (2*l**2)))

            grid[grid < 0] = 0
            avg_list[:, t_index] = numpy.sum(grid)
            mono_layer_list[:, t_index] = numpy.sum(grid) / l**2
            coverage_list[:, t_index] = numpy.sum(grid >= nu) / l**2

        mono_layer_vs_gamma[:, :, iGamma] = mono_layer_list
        avg_vs_gamma[:, :, iGamma] = avg_list
        rough_vs_gamma[:, :, iGamma] = rough_list
        coverage_vs_gamma[:, :, iGamma] = coverage_list
    
    #plot stuff

if __name__=='__main__':
    main()
