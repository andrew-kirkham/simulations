#!/bin/python3
import numpy
import plotly
from random import random
from plotly.graph_objs import Histogram, Layout, Scatter

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
def lorentzian_distribution(x, a, c, x0):
    f_x = c / (1 + (numpy.power(x - x0, 2) / a))
    return f_x

def rejection_method(a, c, x0):
    accepted = []
    expected = []
    
    for i in range(10000):
        u=random()
        sample = numpy.random.gamma(5, 1)
        f_x = lorentzian_distribution(sample, a, c, x0)
        g_x = gamma_distribution(sample)
        if (u <= g_x / f_x):
            accepted.append(sample)
        
    print(len(accepted))
    lorentzian_values= [lorentzian_distribution(x, a, c, x0) for x in numpy.arange(0, 10, 0.01)]
    expected = [gamma_distribution(x) for x in numpy.arange(0,10,0.01)]
    plot_results(accepted, expected, lorentzian_values)

def plot_results(accepted, expected, lorentzian):
    distplot = plotly.tools.FigureFactory.create_distplot(
            [accepted], ['accepted vars'])
    #plotly.offline.plot(distplot, filename="q2-test.html")

    #design the traces
    accepted_trace = Histogram(x=accepted, name='accepted values', autobinx=False, 
            xbins= dict(
                start=0,
                end=10,
                size=0.1
                )
            )
    target_trace = Scatter(x=numpy.arange(0,10,.01), y=expected, name='gamma (target)')
    sampling_trace = Scatter(x=numpy.arange(0,10,.01), y=lorentzian, name='lorentzian (sampling)')
    
    #design the subplot look
    figure=plotly.tools.make_subplots(
            rows=2, 
            cols=2, 
            specs=[[{}, {}],[{'colspan': 2}, None]], 
            subplot_titles=('Accepted Samples', 'Expected Distribution', 'Sampling Distribution and Expected Distribution'))
    
    #append traces to the subplot
    figure.append_trace(accepted_trace, 1, 1)
    figure.append_trace(target_trace, 1, 2)
    figure.append_trace(target_trace, 2, 1)
    figure.append_trace(sampling_trace, 2, 1)
    
    #set up the layout
    figure['layout'].update(title='Rejection Method')
    figure['layout']['xaxis1'].update(range=[0,10])
    
    #save the figure
    plotly.offline.plot(figure, filename="q2.html")

def main():
    #previously chosen values for the lorentz equation
    a=2
    c=3
    x0=0
    #area under f(x) is not calculated here
    rejection_method(a,c,x0)

if __name__=="__main__":
    main()

