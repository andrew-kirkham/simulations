#!/bin/python3
import numpy

def pad(m):
    
    temp = m[:, m.shape[0]]
    temp.append(m)
    temp.append(m[:, 0])
    pad = numpy.array([0, m[m.shape[0], :], 0], 
            [temp], 
            [0, m[0, :], 0])
    return pad
