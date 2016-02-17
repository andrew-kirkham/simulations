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
def rejection_method():
    accepted = []
    
    for i in range(10000):
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
        
    print('Count of accepted values: ', len(accepted))
    #calculate the rejection percentage and display it out of 100%
    print('Rejection percentage: ', (10000-len(accepted)) / 100, '%')
    plot_results(accepted)

#plot the results of the rejection method.
#Creates a plot that shows a histogram of expected values, the expected distribution
#and the sampling distribution on top of the expected distribution
def plot_results(accepted):
    #create arrays for the expected/target distributions to graph them
    lorentzian= [lorentzian_distribution(x) for x in numpy.arange(0, 10, 0.01)]
    expected = [gamma_distribution(x) for x in numpy.arange(0,10,0.01)]
    
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

if __name__=="__main__":
    rejection_method()

