#!/usr/bin/python3
import numpy
import random

def main():
    #given data set
    data = [5,4,9,21,17,11,20,7,10,21,15,13,16,8]
    num_trials=10000
    #initialize list
    trial = []
    var_data = numpy.var(data)
    for iTrial in range(num_trials): 
        #randomly grab len(data) items from our data set
        bootstrap = [data[random.randint(0, len(data)-1)] for i in range(len(data))]
        bootstrap_var=numpy.var(bootstrap)
        #calculate the mean squared error for this run
        trial.append((bootstrap_var-var_data)**2)

    #calculate and print the average error
    avg_error = numpy.mean(trial)
    print(avg_error)

if __name__=='__main__':
    main()
