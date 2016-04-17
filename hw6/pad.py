#!/bin/python3
import numpy

def pad(m):
    print('shape: ', m.shape)
    #add first column to the end and last column to the front
    first_col = numpy.array([m[:,0]]).T
    last_col = numpy.array([m[:,-1]]).T
    temp = numpy.hstack((last_col, m, first_col))

    #flip top and bottom rows of original matrix, pad with 0's
    top_row = numpy.insert(m[-1,:], 0, 0)
    top_row = numpy.append(top_row, 0)
    bottom_row = numpy.insert(m[0,:], 0, 0)
    bottom_row = numpy.append(bottom_row,0)
    pad = numpy.vstack((top_row, temp, bottom_row))

    return pad
