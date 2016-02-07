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
    #initialize array and set x0 as the first element
    w = []
    w.append(x0)

    #generate 2000 values
    generate_random(w, length)

    #set x to be even elements, y to be odd elements, z to be even elements starting at 2
    x = w[::2]
    y = w[1::2]
    z = w[2::2]
    return x,y,z

def generate_scaled_data(x0):
    #l = the number of values we pick from
    l = 25
    #generate a large dataset to refresh numbers from
    x, y, z = generate_data(x0, 30000)
    T=[]
    w=[]
    #set T to be scaled values chosen from x and y
    for i in range(l):
        T.append(1/2048 * (x[i] + 1/2048 * y[i]))
    
    #pick 2000 random variables from T. each value chosen from T is then replaced using the same formula
    for k in range(2000):
        w.append(T[z[k+1] % l])
        T[z[k+1] % l] = 1/2048 * (x[k+l+1] + 1/2048 * y[k+l+1])

    #x is now even elements in w and y is odd elements in w
    x = w[::2]
    y = w[1::2]

    return x,y

def main(x0):
    [scaled_x, scaled_y] = generate_scaled_data(x0)

    #plot the scaled data and save it as a html file
    plotly.offline.plot({
        "data": [ Scatter(x=scaled_x, y=scaled_y, mode='markers') ],
        "layout": Layout(title="Second Question")
    }, filename="q2.html")

    #display the covariance
    print("Q2 Covariance Matrix")
    print(numpy.cov(scaled_x,scaled_y))

if __name__ == '__main__':
    main(100)
