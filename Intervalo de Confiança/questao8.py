import scipy.stats as st
import math

avg = 4
sd = 2
percentile = .94
n = 141

xper = st.norm.ppf(percentile)*sd+avg
print("c percentile = ",xper)
sample = st.norm.ppf(percentile)*sd/math.sqrt(n)+avg
print("sample percentile = ",sample)