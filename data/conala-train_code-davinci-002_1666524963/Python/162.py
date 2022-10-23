import numpy as np
import matplotlib.pyplot as plt

# Generate random numbers with a given distribution
#
# Input:
#   dist: a string specifying the distribution
#   n: number of random numbers to generate
#   params: a list of parameters for the distribution
#
# Output:
#   x: a list of random numbers
#
# Example:
#   x = rand_dist('normal', 100, [0, 1])
#   x = rand_dist('uniform', 100, [0, 1])
#   x = rand_dist('exponential', 100, [1])
#   x = rand_dist('gamma', 100, [1, 1])
#   x = rand_dist('beta', 100, [1, 1])
#   x = rand_dist('binomial', 100, [10, 0.5])
#   x = rand_dist('poisson', 100, [1])
#   x = rand_dist('geometric', 100, [0.5])
#   x = rand_dist('negative_binomial', 100, [10, 0.5])
#   x = rand_dist('hypergeometric', 100, [10, 5, 3])
#   x = rand_dist('logistic', 100, [0, 1])
#   x = rand_dist('lognormal', 100, [0, 1])
#   x = rand_dist('rayleigh', 100, [1])
#   x = rand_dist('wald', 100, [1, 1])
#   x = rand_dist('pareto', 100, [1])
#   x = rand_dist('weibull', 100, [1])
#   x = rand_dist('gumbel', 100, [0, 1])
#   x = rand_dist('triangular', 100, [0, 1, 0.5])
#   x = rand_dist('vonmises', 100, [0, 1])
#   x = rand_dist('laplace', 100, [0, 1])
#   x = rand_dist('chi2', 100, [1])
#   x = rand_dist