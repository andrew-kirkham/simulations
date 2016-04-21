#!/bin/python3
import numpy
import plotly
from plotly.graph_objs import Scatter, Layout

def main():
    delta_t = 2**-3
    euler = []
    exact = []
    euler.append(euler_marn(delta_t))
    exact.append(exact_soln(delta_t))

    exact_plot = Scatter(x=numpy.linspace(0,1,1/delta_t), y=exact)
    euler_plot = Scatter(x=numpy.linspace(0,1,1/delta_t), y=euler)
    figure = dict(data=[exact_plot, euler_plot], layout = Layout(title="bullshit"))
    plotly.offline.plot(figure, filename="q2.html")


def euler_marn(delta_t):
    time = numpy.linspace(0, 1, 1/delta_t)
    sdt = numpy.sqrt(delta_t)
    x = []
    x.append(1) #x0
    for i in range(1, int(1/delta_t)):
        x_t = x[i-1]+(1.5*x[i-1])* delta_t + (.1*x[i-1]) * numpy.random.normal(0, delta_t)*sdt
        x.append(x_t)
    return x

def exact_soln(delta_t):
    time = numpy.linspace(0, 1, 1/delta_t)
    sdt = numpy.sqrt(delta_t)
    x = []
    b_t = []
    b_t.append(0)
    x.append(1) #x0
    for i in range(1,int(1/delta_t)):
        b_t.append(b_t[i-1]+numpy.sqrt(delta_t)*numpy.random.normal(0, delta_t))
        a=1.5
        b=0.1
        x_t = x[0] * numpy.exp((a-(1/2)*b**2)*time[i] + b*b_t[i-1])
        x.append(x_t)
    return x

if __name__=='__main__':
    main()
