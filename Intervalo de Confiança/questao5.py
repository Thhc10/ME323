import scipy.stats as st
import math

avg = 19.70
sd = 1.53256
alpha = .90
n = 110

z = st.norm.ppf(alpha)
lowerbound = avg - z*sd/math.sqrt(n)
upperbound = avg + z*sd/math.sqrt(n)
print("standard error = ",sd/math.sqrt(n))
print("interval = ",z)
print("lowerbound = ",lowerbound)
print("upperbound = ",upperbound)