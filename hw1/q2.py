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
    w = []
    w.append(x0)

    #generate 2000 values
    generate_random(w, length)

    x = w[::2]
    y = w[1::2]
    z = w[2::2]
    return x,y,z

def generate_scaled_data(x0):
    l = 25
    x, y, z = generate_data(x0, 30000)
    T=[]
    w=[]
    for i in range(l):
        T.append(1/2048 * (x[i] + 1/2048 * y[i]))
    
    for k in range(2000):
        w.append(T[z[k+1] % l])
        T[z[k+1] % l] = 1/2048 * (x[k+l+1] + 1/2048 * y[k+l+1])

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
