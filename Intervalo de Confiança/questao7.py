import scipy.stats as st
import statistics
import math

var = 13
alpha = .95
newmargin = 2
sd = math.sqrt(var)
data = [17.84,11.47,10.83,18.54,11.52,15.97,15.94,10.71,11.6,17.74,23.91,20.01]

avg = statistics.mean(data)
confidenceinterval = st.norm.interval(alpha,loc=avg,scale=sd/math.sqrt(len(data)))
lowerbound = confidenceinterval[0]
upperbound = confidenceinterval[1]
interval = upperbound - avg
z = st.norm.ppf((1+alpha)/2)
newn = math.ceil((z*sd/newmargin)**2)

unknownconf = st.t.interval(alpha,len(data)-1,loc=avg,scale=st.sem(data))

print("average = ",avg)
print(confidenceinterval)
print("interval = ",interval)
print("number of people = ",newn)

print("\n\nUnknown variance interval: ")
print(unknownconf)