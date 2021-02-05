import scipy.stats as st
import math

avg = 3.3
n = 850
percentile = 0.52

sample = 170
stddev = avg
c = st.expon.ppf(percentile, loc=0, scale=avg)
newstddev = stddev/math.sqrt(sample)


print("average = ",avg)
print("distance = ",c)
print("newstddev = ",newstddev)

student = st.norm.ppf(percentile)*stddev/math.sqrt(sample)+avg
print("sample percentile = ",student)
