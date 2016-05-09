#!/bin/python3
import numpy

def main():
    l = 10
    k = 1
    n = l**2
    mu = 0.5
    nu = 1
    t_max = 10
    h0 = numpy.zeros(l, l)
    h = h0
    gamma = 4
    rho = 1 + (k * numpy.exp((gamma/2)*2 - mu))

    #yes lambda is spelled wrong, but it is a reserved keyword in python
    lamda = 1/(n*rho)
    num_tests = 10

    t=0
    t_index = 0

    temps = numpy.zeros(10**5, 1)
    while (t<= 20):
        temps[t_index] = t
        t_index += 1
        temp = -numpy.log(random()/(1/lamda))
        t = t + temp

    avg_vs_gamma = numpy.zeros(t_index, num_tests, 1)

    for iGamma in range(1):
        
        for iTest in range(num_tests):
            grid = growth(t_index, h0, gamma, k, mu)
            h_pad = numpy.zeros(l+2, l+2, t+index)

            for i in range(t_index):
                h_pad[:][:][t_index] = pad(grid[:][:][t_index])

            #direction calcs from hw7
            
            rough[:][t_index] = numpy.sum((
                    numpy.abs(grid - north) +
                    numpy.abs(grid - south) +
                    numpy.abs(grid - earth) +
                    numpy.abs(grid - west) /
                    (2*l**2)))

            grid[grid < 0] = 0
            avg[:][t_index] = numpy.sum(grid)
            mod[:][t_index] = numpy.sum(grid) / l**2
            cover[:][t_index] = numpy.sum(grid >= nu) / l**2

        monolayer_vs_gamma[:][:][iGamma] = mod
        avg_vs_gamma[:][:][iGamma] = avg
        rough_vs_gamma[:][:][iGamma] = rough
        cover_vs_gamma[:][:][iGamma] = cover
    
    #plot stuff

if __name__=='__main__':
    main()
