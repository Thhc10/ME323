import scipy.stats as st
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


mu0 = 7
mean = 5.97
stderror = 0.147
testtype = "bigger"
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