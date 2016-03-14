#!/bin/python3
import numpy
import scipy
import scipy.stats
import scipy.integrate
import math
import plotly
from random import random
from plotly.graph_objs import Histogram, Layout

def main():
    part_a()
    part_b()

def part_a():
    sample_size = 35000
    rands = [random() for i in range(sample_size)]

    f_x=[(-1) * numpy.log(1-r) for r in rands]
    g_x = [numpy.cos(x) for x in f_x]
    print_results(g_x)

def part_b():    
    sample_size = 10000
    rands = [scipy.stats.norm().rvs() for i in range(sample_size)]
    
    f_x = [numpy.arccos(2*pi * (1-r)-1) for r in rands]
    #f_x = [(1/(2*math.pi) * (1+numpy.cos(r))) for r in rands]
    g_x = [((2*math.pi) * (1+numpy.cos(x))**(-2/3)) for x in f_x]
    print_results(g_x)

def print_results(g_x):
    mean = numpy.mean(g_x)
    var = numpy.var(g_x)
    print("mean: ", mean, " var: ", var)

if __name__=="__main__":
    main()

