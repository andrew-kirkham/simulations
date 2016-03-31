#!/usr/bin/python3
import numpy
import random
from collections import Counter

def main():
    data = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    mean=numpy.mean(data)
    a=-5
    b=5
    num_trials=1000
    trial=[]
    
    for iTrial in range(num_trials): 
        bootstrap = [data[random.randint(0, len(data)-1)] for i in range(len(data))]
        trial.append(numpy.mean(bootstrap))
    
    difference=[(x-mean) for x in trial]
    prob=[a < x < b for x in difference]
    print('total probability: ', prob.count(True)/len(prob))

if __name__=='__main__':
    main()
