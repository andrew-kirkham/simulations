#!/usr/bin/python3
import scipy
import scipy.stats
from scipy.stats import chi2
from scipy.integrate import quad
import numpy
import box_mueller_transform
import cauchy_distribution
import linear_congruential_generator
from random import random
import math

"""
Notes: sample size is determined by a z-score
number of bins is found using a formula relating sample size.
    the formula is what software uses to determine sample size
"""

def calculate_chi2(random, bins, integrand):
    #sort the random array to make binning faster
    sorted_random=numpy.sort(random)
    #create equal sized bins between 0 and 1
    bin_ends=numpy.linspace(0,1,bins+1)
    count=numpy.zeros(bins)
    p=numpy.zeros(bins)
    #count the number of elements that are in each bin
    for k in range(bins):
        temp= numpy.where(
                    (sorted_random > bin_ends[k]) &
                    (sorted_random < bin_ends[k+1])
                )
        count[k] = numpy.size(temp)
        #calculate the expected probability of the bin
        p[k], temp  = scipy.integrate.quad(integrand, bin_ends[k], bin_ends[k+1])
    #calculate the expected count in each bin using the probability
    n = len(random)
    expected_counts = [ n * p[k] for k in range(bins) ]
    #find the chisquared value for our count
    chi_squared, temp = scipy.stats.chisquare(count, expected_counts)
    return chi_squared 

def lcg():
    """
    Evaluate the LCG built in hw1. uniform [0,1)
    """
    #expected mean is 1/12 (from wikipedia)
    sample_size = get_sample_size(1/12)
    #get sample_size random values using 100 as the seed
    random = linear_congruential_generator.generate_scaled_data(100, sample_size)
    bins = math.floor(1.88 * sample_size ** (2/5))
    integrand = lambda x : 1

    actual_chi2 = calculate_chi2(random, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    uniform_stats(random)
    evaluate_results(expected_chi2, actual_chi2)

def get_sample_size(expected_std_dev):
    """
    Calculate the sample size necessary using z-score
    """
    sample_size = ((2.576 * expected_std_dev)/ 0.01) ** 2
    print("Sample size: ", sample_size)
    return math.floor(sample_size)

def uniform_stats(rands):
    """
    print out the mean and var of the uniform random distribution
    """
    expected_mean = 1/2
    actual_mean = numpy.mean(rands)
    expected_var = 1/12
    actual_var = numpy.var(rands)
    evaluate_stats(expected_mean, actual_mean, expected_var, actual_var)

def built_in_rand():
    """
    Evaluate the built in python RNG. uniform [0,1)
    """
    sample_size = get_sample_size(1/12)
    rands = [random() for k in range(sample_size)]
    bins = math.floor(1.88 * sample_size ** (2/5))
    integrand = lambda x : 1
    
    actual_chi2 = calculate_chi2(rands, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    uniform_stats(rands)
    evaluate_results(expected_chi2, actual_chi2)
    
def box_mueller():
    """
    Evaluate the box_mueller transformation as a normal RNG
    """
    sample_size = get_sample_size(math.sqrt(.1))
    bins = math.floor(1.88 * sample_size ** (2/5))
    rands=box_mueller_transform.main(sample_size)
    integrand = lambda x: scipy.stats.norm.pdf(x, scale=numpy.sqrt(0.1))

    actual_chi2 = calculate_chi2(rands, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    normal_stats(rands)
    evaluate_results(expected_chi2, actual_chi2)

def normal_stats(rands):
    """
    Print out the stats for a normal distribution of randoms
    """
    expected_mean = scipy.stats.norm.mean()
    actual_mean = numpy.mean(rands)
    expected_var = 0.1 #given by homework
    actual_var = numpy.var(rands)
    evaluate_stats(expected_mean, actual_mean, expected_var, actual_var)

def cauchy():
    sample_sizes=[1000, 10000]
    for sample_size in sample_sizes:
        rands=cauchy_distribution.rejection_method(sample_size)
        actual_mean = numpy.mean(rands)
        actual_var = numpy.var(rands)
        print("Actual mean for ", sample_size, ": ", actual_mean)
        print("Actual var for ", sample_size, ": ", actual_var)
        #compare cauchy to gamma - our target dist
        bins = math.floor(1.88 * sample_size ** (2/5))
        integrand = lambda x: scipy.stats.gamma(5).pdf(x)
        actual_chi2 = calculate_chi2(rands, bins, integrand)
        expected_chi2 = chi2.ppf(.99, bins-1)
        evaluate_results(expected_chi2, actual_chi2)

def gamma():
    """
    Evaluate the gamma distribution as a RNG
    """
    expected_var = scipy.stats.gamma(5).var()
    sample_size = get_sample_size(math.sqrt(expected_var))
    bins = math.floor(1.88 * sample_size ** (2/5))
    rands=scipy.stats.gamma(5).rvs(size=sample_size)
    integrand = lambda x: scipy.stats.gamma(5).pdf(x)

    actual_chi2 = calculate_chi2(rands, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    gamma_stats(rands)
    evaluate_results(expected_chi2, actual_chi2)

def gamma_stats(rands):
    """
    Print out Gamma distribution stats
    """
    expected_mean = scipy.stats.gamma(5).mean()
    actual_mean = numpy.mean(rands)
    expected_var = scipy.stats.gamma(5).var() 
    actual_var = numpy.var(rands)
    evaluate_stats(expected_mean, actual_mean, expected_var, actual_var)

def evaluate_stats(expected_mean, actual_mean, expected_var, actual_var):
    """
    Print out the means/variance
    """
    print("Expected mean: ", expected_mean, " Actual mean: ", actual_mean)
    print("Expected var: ", expected_var, " Actual var: ", actual_var)

def evaluate_results(expected, actual):
    """
    Print out interpretation of chi2
    """
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
    print("\nCauchy transform for normal random numbers")
    cauchy()
    print("\nGamma transform with shape 5 for random numbers")
    gamma()

if __name__=='__main__':
    main()
