import scipy.stats as st
import math

phat = 0.28
n = 518
alpha = 0.90
newmargin = 0.02

z = st.norm.ppf((1+alpha)/2)
interval = z*math.sqrt(phat*(1-phat)/n)
lowerbound = phat - interval
upperbound = phat + interval
#assume phat*(1-phat) will be maximum
noresearchdone = math.ceil((z*math.sqrt(0.25)/newmargin)**2)



print("population proportion = ",phat)
print("lowerbound = ",lowerbound)
print("upperbound = ",upperbound)
print("margin of error (percentage) = ", interval*100)
print("number of people with no research done = ",noresearchdone)