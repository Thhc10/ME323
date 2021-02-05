import scipy.stats as st
import math

phat = 0.34
n = 706
alpha = 0.95
value = 0.38


z = st.norm.ppf((1+alpha)/2)
interval = z*math.sqrt(phat*(1-phat)/n)
lowerbound = phat - interval
upperbound = phat + interval

print("population proportion = ",phat)
print("lowerbound = ",lowerbound)
print("upperbound = ",upperbound)
print("margin of error (percentage) = ", interval*100)
if(value >= lowerbound and value <= upperbound):
    print(1)
else:
    print(0)