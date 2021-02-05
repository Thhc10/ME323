import scipy.stats as st
import statistics
import math

def pvaluecalc(zobs,alpha,testtype = "different"):
    if testtype == "bigger":
        pvalue = 1 - st.norm.cdf(zobs)
        criticalvalue = st.norm.ppf(1-alpha)
    elif testtype == "smaller":
        pvalue = st.norm.cdf(zobs)
        criticalvalue = st.norm.ppf(alpha)
    else:
        pvalue = 2*(1-st.norm.cdf(abs(zobs)))
        criticalvalue = st.norm.ppf(1-alpha/2)
    return pvalue, criticalvalue


mu0 = 680
mean = 677.5
var = 1824.5
n = 19
stderror = math.sqrt(var/n)
testtype = "different"
alpha = 0.01

zobs = (mean-mu0)/stderror
pvalue,criticalvalue = pvaluecalc(zobs,alpha,testtype)

print("z observed = ",zobs)
print("p-value = ",pvalue)
print("critical value = ",criticalvalue)

if(pvalue > alpha):
    print("Ho não pode ser rejeitada")
    print("não")
else:
    print("Ho foi rejeitada")
    print("sim")
