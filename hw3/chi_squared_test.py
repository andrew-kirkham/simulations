#!/usr/bin/python3
import scipy
from scipy.stats import chi2
from scipy.integrate import quad
import numpy
import box_mueller_transform
import built_in_random
import cauchy_distribution
import linear_congruential_generator
from random import random

####
#TODO: calculate the necessary samples for each rng
####

def calculate_chi2(random, bins, integrand):
    sorted_random=numpy.sort(random)
    bin_ends=numpy.linspace(0,1,bins+1)
    count=numpy.zeros(bins)
    p=numpy.zeros(bins)
    for k in range(bins):
        temp= numpy.where(
                    (sorted_random > bin_ends[k]) &
                    (sorted_random < bin_ends[k+1])
                )
        count[k] = numpy.size(temp)
        p[k], temp  = scipy.integrate.quad(integrand, bin_ends[k], bin_ends[k+1])
    n = len(random)
    chi_squared = [(count[k] - n/bins) ** 2 for k in range(1, bins)]
    return bins/n * sum(chi_squared)

def lcg():
    print("\nLCG from HW1 for uniform random numbers")
    random = linear_congruential_generator.generate_scaled_data(100, 2000)
    bins = 128
    integrand = lambda x : 1
    actual = calculate_chi2(random, bins, integrand)
    expected = chi2.ppf(.99, bins-1)
    evaluate_results(actual, expected)

def built_in_rand():
    print("\nPython random library for uniform random numbers")
    rands = [random() for k in range(10000)]
    bins = 1000
    integrand = lambda x : 1
    actual = calculate_chi2(rands, bins, integrand)
    expected = chi2.ppf(.99, bins-1)
    evaluate_results(actual, expected)
    
def box_mueller():
    #TODO
    pass

def cauchy():
    #TODO
    pass

def gamma():
    #TODO
    pass

def evaluate_results(actual, expected):
    print("Actual: ", actual, " Expected: ", expected)
    if (actual > expected):
        print("Reject the null hypothesis! RNG poorly fits target")
    else:
        print("Fail to reject!")
    

def main():
    lcg()
    built_in_rand()
    box_mueller()
    cauchy()
    gamma()

if __name__=='__main__':
    main()
