import scipy.stats as st
import math

def pvaluecalc(zobs,testtype = "different"):
    if testtype == "bigger":
        pvalue = 1 - st.norm.cdf(zobs)
    elif testtype == "smaller":
        pvalue = st.norm.cdf(zobs)
    else:
        pvalue = 2*(1-st.norm.cdf(abs(zobs)))
    return pvalue


n = 219
yes = 109
p0 = 0.43
phat = yes/n
zobs = (phat - p0)/math.sqrt(p0*(1-p0)/n)
print(zobs)
print(pvaluecalc(zobs, "bigger"))
