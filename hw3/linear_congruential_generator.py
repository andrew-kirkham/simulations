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
    #while we haven't hit the max, generate rv using the lcg
    while (len(array) < max):
        previous = array[len(array)-1]
        random_number = lcg(previous)
        array.append(random_number)

def generate_data(x0, length):
    #initialize array with x0 as the first element
    w = []
    w.append(x0)

    #generate 2000 values
    generate_random(w, 2000)

    #set x to be even elements and y to be odd elements
    x = w[::2]
    y = w[1::2]
    return x,y

def generate_scaled_data(x0):
    x, y = generate_data(x0, 1000)

    #scale x and y by m to put them in the range [0,1]
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
    #100 is our seed value
    main(100)
