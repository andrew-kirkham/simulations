#!/usr/bin/python3
import numpy
import random

def main():
    #given data set
    data = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    mean=numpy.mean(data)
    #given range for probability
    a=-5
    b=5
    num_trials=1000
    trial=[]
    
    for iTrial in range(num_trials): 
        #randomly grab len(data) items from our data set
        bootstrap = [data[random.randint(0, len(data)-1)] for i in range(len(data))]
        #calculate the mean of the bootstrap
        trial.append(numpy.mean(bootstrap))
    
    #calculate the difference in means for each trial
    difference=[(x-mean) for x in trial]
    #calculate the probability of being within our given margin
    prob=[a < x < b for x in difference]
    print('total probability: ', prob.count(True)/len(prob))

if __name__=='__main__':
    main()
