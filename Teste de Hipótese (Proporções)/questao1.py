import scipy.stats as st
import math


def pvaluecalc(zobs, testtype="different"):
    if testtype == "bigger":
        pvalue = 1 - st.norm.cdf(zobs)
    elif testtype == "smaller":
        pvalue = st.norm.cdf(zobs)
    else:
        pvalue = 2 * (1 - st.norm.cdf(abs(zobs)))
    return pvalue


n = 24
yes = 18
p0 = 0.73
phat = yes / n
zobs = (phat - p0) / math.sqrt(p0 * (1 - p0) / n)
print("test statistic (zobs) = ", zobs)
print("pvalue : ", pvaluecalc(zobs))
