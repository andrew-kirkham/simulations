#!/bin/python3
import numpy
import plotly
from plotly.graph_objs import Scatter, Layout

def main():
    delta_t = [2**-3, 2**-4, 2**-5, 2**-6]
    for index, t in enumerate(delta_t):
        euler = []
        exact = []
        huen = []
        euler=euler_marn(t)
        exact=exact_soln(t)
        huen=huen_soln(t)
        x_data = numpy.linspace(0,1,1/t)
        exact_plot = Scatter(x=x_data, y=exact, name="Exact Soln")
        euler_plot = Scatter(x=x_data, y=euler, name="Euler Soln")
        huen_plot = Scatter(x=x_data, y=huen, name="Huen Soln")

        figure = dict(
                data=[exact_plot, euler_plot, huen_plot], 
                layout = Layout(title="2^{0}".format((index+3)*-1))
                )
        filename="q2_{0}.html".format(index)
        plotly.offline.plot(figure, filename=filename)


def euler_marn(delta_t):
    time = numpy.linspace(0, 1, 1/delta_t)
    sdt = numpy.sqrt(delta_t)
    x = []
    x.append(1) #x0
    for i in range(1, int(1/delta_t)):
        x_t = x[i-1]+(1.5*x[i-1])* delta_t + (.1*x[i-1]) * numpy.random.normal(0, delta_t)*sdt
        x.append(x_t)
    return x

def huen_soln(delta_t):
    time = numpy.linspace(0, 1, 1/delta_t)
    sdt = numpy.sqrt(delta_t)
    x = []
    x.append(1) #x0
    for i in range(1, int(1/delta_t)):
        x_tilde = x[i-1]+(1.5*x[i-1])* delta_t + (.1*x[i-1]) * numpy.random.normal(0, delta_t)*sdt
        x_t=x[i-1]+(1/2)*((1.5*x[i-1])+(1.5*x_tilde))*delta_t + (
                (1/2)*((.1*x[i-1])+(.1*x_tilde))
                ) * numpy.random.normal(0, delta_t)*sdt
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
