# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:08:06 2020

@author: Mohammadali
"""
from math import sqrt
from math import factorial

def get_mean(N,M):
    n = N-1
    p = 1/M
    return n*p

def get_std(N,M):
    n = N-1
    p = 1/M
    q = 1-p
    return sqrt(n*p*q)

def get_combination(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def get_probability_function(n,k,p):
    q = 1-p
    return get_combination(n,k)*p**k*q**(n-k)

def get_pdf(N,M,x):
    n = N-1
    p = 1/M
    pdf = 0
    for k in range(x+1):
        pdf =+ get_probability_function(n,k,p)
    return pdf

#q1-part1
print('answer of part 1: {}'.format(get_mean(26,2)))

#q1-part2
print('answer of part 2: {}'.format(get_std(26,2)))

#q1-part3
print('answer of part 3: {}'.format(get_mean(52,4)))

#q1-part4
print('answer of part 4: {}'.format(get_std(52,4)))

#q1-part5
a = 1-get_pdf(26,2,12) # probability of p>12
b = 1-get_pdf(26,2,6) # probability of p>6
print('answer of part 5: {}'.format(a/b))

#q1-part6
a = 1-get_pdf(52,4,12) # probability of p>12
b = 1-get_pdf(52,4,6) # probability of p>6
print('answer of part 6: {}'.format(a/b))