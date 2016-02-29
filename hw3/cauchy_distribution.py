#!/bin/python3
import numpy
import plotly
from random import random
from plotly.graph_objs import Histogram, Layout, Scatter

####
#items in the homework not done here:
#   calculating a, c, x0
#   area under f(x) for the above parameters
####

#evaluate a given gamma distribution at x
#we are given the shape is 5 and scale is 1
#the equation was simplified using wolfram alpha
def gamma_distribution(x):
    if (x <= 0):
        return 0
    else:
        p_x= 1/24 * numpy.exp(-x) * numpy.power(x,4)
        return p_x

#evaluate lorentz at x
def lorentzian_distribution(x):
    #previously chosen values for the lorentz equation
    #these values were chosen by plotting lorentz vs gamma and choosing values
    #such that lorentz > gamma for [0,10]
    a=2
    c=3
    x0=0
    f_x = c / (1 + (numpy.power(x - x0, 2) / a))
    return f_x

#generate 10000 rv from the sample distribution(gamma) and reject those that
#do not match the target distribution (cauchy)
def rejection_method(target_sample_size):
    accepted = []
    while (len(accepted) < target_sample_size):
        #choose a u from a normal distribution
        u=random()
        #sample a value from g(x) - a gamma distribution
        sample = numpy.random.gamma(5, 1)

        #calculate f(sample) * M
        f_x = lorentzian_distribution(sample)
        #calculate g(sample)
        g_x = gamma_distribution(sample)
        #check for rejection
        if (u <= g_x / f_x):
            accepted.append(sample)

    return accepted

if __name__=="__main__":
    rejection_method(1000)

