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
import math

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
    expected_counts = [ n * p[k] for k in range(bins) ]
    chi_squared, temp = scipy.stats.chisquare(count, expected_counts)
    return chi_squared 

def lcg():
    sample_size = get_sample_size(1/12)
    random = linear_congruential_generator.generate_scaled_data(100, sample_size)
    bins = math.floor(1.88 * sample_size ** (2/5))
    integrand = lambda x : 1

    actual_chi2 = calculate_chi2(random, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    uniform_stats(random)
    evaluate_results(expected_chi2, actual_chi2)

def get_sample_size(expected_std_dev):
    """
    Calculate the sample size necesary using z-score
    """
    sample_size = ((2.576 * expected_std_dev)/ 0.01) ** 2
    #sample_size = (expected_mean * (1-expected_mean))/((0.01/2.576)**2)
    return math.floor(sample_size)

def uniform_stats(rands):
    """
    print out the mean and var of the random distribution
    """
    expected_mean = 1/2
    actual_mean = numpy.mean(rands)
    expected_var = 1/12
    actual_var = numpy.var(rands)
    evaluate_stats(expected_mean, actual_mean, expected_var, actual_var)

def built_in_rand():
    sample_size = get_sample_size(1/12)
    rands = [random() for k in range(sample_size)]
    bins = math.floor(1.88 * sample_size ** (2/5))
    integrand = lambda x : 1
    
    actual_chi2 = calculate_chi2(rands, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    uniform_stats(rands)
    evaluate_results(expected_chi2, actual_chi2)
    
def box_mueller():
    sample_size = get_sample_size(math.sqrt(.1))
    bins = math.floor(1.88 * sample_size ** (2/5))
    rands=box_mueller_transform.main(sample_size)
    integrand = lambda x: scipy.stats.norm.pdf(x)

    actual_chi2 = calculate_chi2(rands, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    normal_stats(rands)
    evaluate_results(expected_chi2, actual_chi2)

def normal_stats(rands):
    expected_mean = scipy.stats.norm.mean()
    actual_mean = numpy.mean(rands)
    expected_var = 0.1 #given by homework
    actual_var = numpy.var(rands)
    evaluate_stats(expected_mean, actual_mean, expected_var, actual_var)

def cauchy():
    #TODO
    pass

def gamma():
    expected_mean = scipy.stats.gamma(5).mean()
    sample_size = get_sample_size(expected_mean)
    bins = math.floor(1.88 * sample_size ** (2/5))
    rands=scipy.stats.gamma(5).rvs(size=1000)
    integrand = lambda x: scipy.stats.gamma(5).pdf(x)

    actual_chi2 = calculate_chi2(rands, bins, integrand)
    expected_chi2 = chi2.ppf(.99, bins-1)
    
    gamma_stats(rands)
    evaluate_results(expected_chi2, actual_chi2)

def gamma_stats(rands):
    expected_mean = scipy.stats.gamma(5).mean()
    actual_mean = numpy.mean(rands)
    expected_var = scipy.stats.gamma(5).var() 
    actual_var = numpy.var(rands)
    evaluate_stats(expected_mean, actual_mean, expected_var, actual_var)

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
    print("\nGamma transform with shape 5 for random numbers")
    gamma()

if __name__=='__main__':
    main()
