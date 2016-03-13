#!/usr/bin/python3
from random import random

def main():
    #100 samples per run
    n=100
    #our modified p value of 0.85 s.t. E[walk] = 70
    p=0.85
    #target final steps
    m=70
    
    total = 0
    for i in range(1000):
        seq = []
        for j in range(n):
            r = random()
            x = 1 if r < p else -1
            seq.append(x)
        total_sum = sum(seq)
        likelihood = calculate_likelihood(seq, total_sum, p)
        total += likelihood
    print("P(m>= 70): ",total/1000)

def calculate_likelihood(seq, total_sum, p):
    #these equations are given in the homework
    #these are the likelihood ratios for a single step
    f_z_pos = (1/(2*p))
    f_z_neg = (1/(2*(1-p)))
    
    #calcuate the overall likelihood ratio
    f_y = 1
    for i in seq:
        if i == 1:
            f_y = f_y * f_z_pos
        else:
            f_y = f_y * f_z_neg

    #if g(y) < 70; our likelihood is 0
    #otherwise it is f_y/f_tilde_y, calculated above
    return 0 if total_sum < 70 else f_y

if __name__=="__main__":
    main()
