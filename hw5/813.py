#!/usr/bin/python3
import numpy
import random

def main():
    data = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    mean=numpy.mean(data)
    a=-5
    b=5
    num_trials=10
    trial=[0 for x in range(num_trials)]
    var_data = numpy.var(data)
    for iTrial in range(num_trials): 
        bootstrap = [data[random.randint(0, len(data)-1)] for i in range(len(data))]
        bootstrap_var=numpy.var(bootstrap)
        trial[iTrial]=numpy.mean(bootstrap)
    print([(x-mean) for x in trial])
if __name__=='__main__':
    main()
