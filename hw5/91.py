#!/usr/bin/python3
import numpy
from random import random

def main():
    trials = 1000
    var_control = []
    var_anti = []
    var_star = []
    estimator = lambda u: numpy.exp(u**2) * (1+numpy.exp(1-(2*u)))/2

    for i in range(trials):
        rands = [random() for i in range(100)]
        x=numpy.exp([r**2 for r in rands])
        covxy = numpy.cov(x,rands)
        cstar = -covxy[1,0]/numpy.var(rands)
        estimate = x + cstar*(rands - numpy.mean(rands))
        var_control.append(numpy.var(estimate))
        var_anti.append(numpy.var([estimator(r) for r in rands]))
        var_star.append(cstar)

    print('star: ', numpy.mean(cstar))
    print('anti: ', numpy.mean(var_anti))
    print('control: ', numpy.mean(var_control))

if __name__=='__main__':
    main()
