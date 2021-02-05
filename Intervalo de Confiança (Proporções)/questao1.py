import scipy.stats as st
import math

n = 594
yes = 137
alpha = 0.95



phat = yes/n
z = st.norm.ppf((1+alpha)/2)
interval = z*math.sqrt(phat*(1-phat)/n)
lowerbound = phat - interval
upperbound = phat + interval

print("population proportion = ",phat)
print("lowerbound = ",lowerbound)
print("upperbound = ",upperbound)
print("margin of error (percentage) = ", interval*100)
