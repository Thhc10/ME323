import scipy.stats as st
import math

avg = 1110
sd = 75
percentile = .35
n = 81

xper = st.norm.ppf(percentile)#*sd+avg
print("x percentile =", xper)
sample = st.norm.ppf(percentile)*sd/math.sqrt(n)+avg
print("adult sample percentile =", sample)
