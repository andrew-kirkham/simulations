#!/usr/bin/python3
import plotly
import numpy
from plotly.graph_objs import Scatter, Layout

def lcg(previous):
    a=1229
    c=1
    m=2048
    #linear congruential generator formula
    return (a * previous + c) % m

def generate_random(array, max):
    #while we haven't hit the max (1000), generate rv
    while (len(array) < max):
        previous = array[len(array)-1]
        random_number = lcg(previous)
        array.append(random_number)

def generate_data(x0, length):
    #initialize arrays
    x = []
    y = []

    #seed the initial values
    x.append(x0)
    y.append(lcg(x0))

    #generate 1000 values
    generate_random(x, length)
    generate_random(y, length)
    return x,y

def generate_scaled_data(x0):
    x, y = generate_data(x0, 1000)

    #scale it by M
    scaled_x = [ x/2048 for x in x ] 
    scaled_y = [ y/2048 for y in y ]
    return scaled_x, scaled_y

def main(x0):
    [scaled_x, scaled_y] = generate_scaled_data(x0)

    #plot the scaled data and save it as a html file
    plotly.offline.plot({
        "data": [ Scatter(x=scaled_x, y=scaled_y, mode='markers') ],
        "layout": Layout(title="First Question")
    }, filename="q1.html")

    #display the covariance
    print("Q1 Covariance Matrix")
    print(numpy.cov(scaled_x,scaled_y))

if __name__ == '__main__':
    main(100)
