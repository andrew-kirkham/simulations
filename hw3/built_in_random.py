#!/usr/bin/python3
import plotly
import numpy
from plotly.graph_objs import Scatter, Layout
from random import random

def generate_scaled_data():
    #generate 1000 random numbers using mersene twister
    x = [random() for x in range(1000)]
    y = [random() for y in range(1000)]
    return x, y

def main():
    [scaled_x, scaled_y] = generate_scaled_data()

if __name__ == '__main__':
    main()
