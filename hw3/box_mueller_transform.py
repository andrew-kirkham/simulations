#!/bin/python3
import numpy
from random import random

def generate_uniform_variables():
    u1 = [random() for i in range(10000)]
    u2 = [random() for i in range(10000)]
    return u1, u2

#u1 and u2 are uniform random variables
def box_muller_transformation(u1, u2):
    z1 = numpy.sqrt(-2*numpy.log(u1))*numpy.cos(2*numpy.pi*u2)
    z2 = numpy.sqrt(-2*numpy.log(u1))*numpy.sin(2*numpy.pi*u2)
    return z1, z2

def main():
    z = []
    u1, u2 = generate_uniform_variables()
    for iRandom in range(10000):
        z1, z2 = box_muller_transformation(u1[iRandom-1], u2[iRandom-1])
        z.append(z1)
        z.append(z2)
    return z
    
if __name__=="__main__":
    main()

