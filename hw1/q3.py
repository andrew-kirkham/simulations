#!/usr/bin/python3
import plotly
import numpy
from plotly.graph_objs import Scatter, Layout
from random import random

def generate_scaled_data():
    x = [random() for x in range(1000)]
    y = [random() for y in range(1000)]
    return x, y

def main():
    [scaled_x, scaled_y] = generate_scaled_data()

    #plot the scaled data and save it as a html file
    plotly.offline.plot({
        "data": [ Scatter(x=scaled_x, y=scaled_y, mode='markers') ],
        "layout": Layout(title="Third Question")
    }, filename="q3.html")

    #display the covariance
    print("Q3 Covariance Matrix")
    print(numpy.cov(scaled_x,scaled_y))

if __name__ == '__main__':
    main()
