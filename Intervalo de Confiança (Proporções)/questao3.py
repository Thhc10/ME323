import scipy.stats as st
import math

n = 137
yes = 14
alpha = 0.99
newmargin = 0.04

phat = yes/n
z = st.norm.ppf((1+alpha)/2)
interval = z*math.sqrt(phat*(1-phat)/n)
lowerbound = phat - interval
upperbound = phat + interval

preresearchdone = math.ceil((z*math.sqrt(phat*(1-phat))/newmargin)**2)
#assume phat*(1-phat) will be maximum
noresearchdone = math.ceil((z*math.sqrt(0.25)/newmargin)**2)

print("population proportion = ",phat)
print("lowerbound = ",lowerbound)
print("upperbound = ",upperbound)
print("margin of error (percentage) = ", interval*100)
print("number of people with previous research = ", preresearchdone)
print("number of people with no research done = ",noresearchdone)