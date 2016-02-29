#!/usr/bin/python3
import scipy
import scipy.stats
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
    random = linear_congruential_generator.generate_scaled_data(100, 2000)
    bins = 128
    integrand = lambda x : 1

    actual_chi2 = calculate_chi2(random, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    uniform_stats(random)
    evaluate_results(expected_chi2, actual_chi2)

def uniform_stats(rands):
    expected_mean = (1-0)/2
    actual_mean = numpy.mean(rands)
    expected_var = (((1-0+1) ** 2) - 1)/12
    actual_var = numpy.var(rands)
    evaluate_stats(expected_mean, actual_mean, expected_var, actual_var)

def built_in_rand():
    rands = [random() for k in range(10000)]
    bins = 1000
    integrand = lambda x : 1
    
    actual_chi2 = calculate_chi2(rands, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    uniform_stats(rands)
    evaluate_results(expected_chi2, actual_chi2)
    
def box_mueller():
    #TODO
    rands=box_mueller_transform.main()
    bins = 1000
    integrand = lambda x: scipy.stats.norm.pdf(x)

    actual_chi2 = calculate_chi2(rands, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    normal_stats(rands)
    evaluate_results(expected_chi2, actual_chi2)

def normal_stats(rands):
    expected_mean = scipy.stats.norm.mean()
    actual_mean = numpy.mean(rands)
    expected_var = scipy.stats.norm.var()
    actual_var = numpy.var(rands)
    evaluate_stats(expected_mean, actual_mean, expected_var, actual_var)

def cauchy():
    #TODO
    pass

def gamma():
    #TODO
    pass

def evaluate_stats(expected_mean, actual_mean, expected_var, actual_var):
    print("Expected mean: ", expected_mean, " Actual mean: ", actual_mean)
    print("Expected var: ", expected_var, " Actual var: ", actual_var)

def evaluate_results(expected, actual):
    print("Expected chi2: ", expected, "Actual chi2: ", actual)
    if (actual > expected):
        print("Reject the null hypothesis! RNG poorly fits target")
    else:
        print("Fail to reject!")
    

def main():
    print("\nLCG from HW1 for uniform random numbers")
    lcg()
    print("\nPython random library for uniform random numbers")
    built_in_rand()
    print("\nBox Mueller transform for normal random numbers")
    box_mueller()
    cauchy()
    gamma()

if __name__=='__main__':
    main()
