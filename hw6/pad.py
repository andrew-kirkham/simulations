#!/bin/python3
import numpy

def pad(m):
    
    temp =numpy.array([[m[:, m.shape[0]-1]], m, m[:,0]])
    pad = numpy.array([[0, m[m.shape[0]-1, :], 0], 
            [temp], 
            [0, m[0, :], 0]])
    return pad
