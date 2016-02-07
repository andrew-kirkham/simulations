#!/usr/bin/python3
import q1
import q2
import q3
import sys

def main():
    #redirect all output to a file 
    sys.stdout = open('Covariance Matrices.txt', 'w') 
    #run through each question in the homework
    q1.main(100)
    q2.main(100)
    q3.main()

if __name__=='__main__':
    main()
