#!/bin/python3
import numpy
import plotly
from plotly.graph_objs import Scatter, Layout

def main():
    #different time intervals that we are comparing
    delta_t = [2**-3, 2**-4, 2**-5, 2**-6]
    for index, t in enumerate(delta_t):
        euler = []
        exact = []
        huen = []
        for iSim in range(100):
            #calculate each solution type
            euler.append(euler_marn(t))
            exact.append(exact_soln(t))
            huen.append(huen_soln(t))

        euler_avg = numpy.mean(euler)
        exact_avg = numpy.mean(exact)
        huen_avg = numpy.mean(huen)
        
        #plot each solution against each other
        x_data = numpy.linspace(0,1,1/t)
        exact_plot = Scatter(x=x_data, y=exact_avg, name="Exact Soln")
        euler_plot = Scatter(x=x_data, y=euler_avg, name="Euler Soln")
        huen_plot = Scatter(x=x_data, y=huen_avg, name="Huen Soln")
        
        #we are expecting huen to converge to exact faster
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
    a = 1.5
    b = 0.1
    x.append(1) #x0
    for i in range(1, int(1/delta_t)):
        x_n = x[i-1]
        w_t = numpy.random.normal(0, delta_t)*sdt
        x_t = x_n+(a*x_n)* delta_t + (b*x_n) * w_t
        x.append(x_t)
    return x

def huen_soln(delta_t):
    time = numpy.linspace(0, 1, 1/delta_t)
    sdt = numpy.sqrt(delta_t)
    x = []
    x.append(1) #x0
    a=1.5
    b=0.1
    for i in range(1, int(1/delta_t)):
        x_n = x[i-1]
        w_t = numpy.random.normal(0, delta_t)*sdt
        x_tilde = x_n+(a*x_n)* delta_t + (b*x_n) * w_t
        #huen expands on euler soln
        x_t=x_n+(1/2)*((a*x_n)+(a*x_tilde)) * delta_t + (
                (1/2)*((b*x_n)+(b*x_tilde))) * w_t
        x.append(x_t)
    return x

def exact_soln(delta_t):
    time = numpy.linspace(0, 1, 1/delta_t)
    sdt = numpy.sqrt(delta_t)
    x = []
    b_t = []
    a=1.5
    b=0.1
    b_t.append(0)
    x.append(1) #x0
    for i in range(1,int(1/delta_t)):
        b_t.append(b_t[i-1]+numpy.sqrt(delta_t)*numpy.random.normal(0, delta_t))
        x_t = x[0] * numpy.exp((a-(1/2)*b**2)*time[i] + b*b_t[i-1])
        x.append(x_t)
    return x

if __name__=='__main__':
    main()
