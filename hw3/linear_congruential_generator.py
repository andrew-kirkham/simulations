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
    return array

def generate_data(seed, numbers_to_generate):
    #initialize array with x0 as the first element
    w = []
    w.append(seed)

    random_numbers = generate_random(w, numbers_to_generate)

    return random_numbers

def generate_scaled_data(seed, numbers_to_generate):
    """
    generate random numbers in the range (0,1)
    using a lcg
    """
    x = generate_data(seed, numbers_to_generate)

    #scale x by m to put in the range [0,1]
    scaled_x = [ x/2048 for x in x ]
    return scaled_x

if __name__ == '__main__':
    #100 is our seed value
    generate_scaled_data(100)
