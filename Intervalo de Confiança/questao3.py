import scipy.stats as st
import math

a = 26
b = 32
expected = (b+a)/2
size = 169
numtimes = 500
print("expected value = ",expected)
sd = (b-a)/math.sqrt(12)
print("standard deviation of the r.v. = ", sd)
sdaftersample = sd/(math.sqrt(size))
print("standard deviation after sampling = ",sdaftersample)