#!/usr/local/bin/python3
""" perceptron-trick.py
Author: Kevin Dick
Date: 2018-11-09
---
Computes the number of iterations required to correctly classify a point.
"""

def classify_point(pnt,wts,bias):
	return 1 if wts[0]*pnt[0] + wts[1]*pnt[1] + bias > 0 else 0

# Question Params
point   = (1,1)
weights = (3,4)
bias    = -10
lrng_r8 = 0.1

count = 0
while not classify_point(point, weights, bias):
	count += 1
	weights = (weights[0] + lrng_r8, weights[1] + lrng_r8)
	bias += lrng_r8
	print("Iterations: {}\nWeights: {}\nBias: {}".format(count, weights, bias))

# Result: 11, but off-by-one due to numerical precision. Correct answer is 10.
