#!/bin/python3
import numpy
import plotly
from random import random
from plotly.graph_objs import Histogram, Layout

def generate_uniform_variables():
    u1 = [random() for i in range(10000)]
    u2 = [random() for i in range(10000)]
    return u1, u2

#u1 and u2 are uniform random variables
def box_muller_transformation(u1, u2):
    z1 = numpy.sqrt(-2*numpy.log(u1))*numpy.cos(2*numpy.pi*u2)
    z2 = numpy.sqrt(-2*numpy.log(u1))*numpy.sin(2*numpy.pi*u2)
    return z1, z2

def calculate_stats(z_cos, z_sin):
    z = z_sin + z_cos
    #calculate mean
    mean = numpy.mean(z)
    print('Mean: ' + str(mean))
    #calculate variance
    variance = numpy.var(z)
    print('Variance: ' + str(variance))
   

#plot the distributions of each random variable
def plot_results(u1, u2, z_cos, z_sin):
    trace1 = Histogram(x=u1, name='Uniform Variable 1')
    trace2 = Histogram(x=u2, name='Uniform Variable 2')
    trace3 = Histogram(x=z_cos, name='Normal Variable z-cos')
    trace4 = Histogram(x=z_sin, name='Normal Variable z-sin')
    figure = plotly.tools.make_subplots(rows=2, cols=2)
    figure.append_trace(trace1, 1, 1)
    figure.append_trace(trace2, 1, 2)
    figure.append_trace(trace3, 2, 1)
    figure.append_trace(trace4, 2, 2)
    figure['layout'].update(title='Box Muller Transform')

    plotly.offline.plot(figure, filename="q1.html")

def main():
    z_cos = []
    z_sin = []
    u1, u2 = generate_uniform_variables()
    for iRandom in range(10000):
        z1, z2 = box_muller_transformation(u1[iRandom-1], u2[iRandom-1])
        z_cos.append(z1)
        z_sin.append(z2)
    
    calculate_stats(z_sin, z_cos)
    plot_results(u1, u2, z_cos, z_sin)

if __name__=="__main__":
    main()

