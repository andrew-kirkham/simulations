#!/usr/bin/python3
import numpy
from random import random

def main():
    trials = 1000
    var_control = []
    var_anti = []
    var_star = []
    #equation for our given antithetic estimator
    antithetic_estimator = lambda u: numpy.exp(u**2) * (1+numpy.exp(1-(2*u)))/2

    for i in range(trials):
        rands = [random() for i in range(100)]
        x=numpy.exp([r**2 for r in rands])
        cov_xy = numpy.cov(x,rands)
        c_star = -cov_xy[1,0]/numpy.var(rands)
        control_estimate = x + c_star*(rands - numpy.mean(rands))
        #variance of our control variate
        var_control.append(numpy.var(control_estimate))
        #variance of our antithetic variate
        var_anti.append(numpy.var([antithetic_estimator(r) for r in rands]))
        var_star.append(c_star)

    print('cstar: ', numpy.mean(c_star))
    print('var(x,y): ', numpy.mean(var_anti))
    print('var(z): ', numpy.mean(var_control))
    antithetic_better = [var_anti[x] < var_control[x] for x in range(trials)]
    print('Percentage when antitethic variable had smaller variance: ',
            antithetic_better.count(True)/len(antithetic_better))

if __name__=='__main__':
    main()
