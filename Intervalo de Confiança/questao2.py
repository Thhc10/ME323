import scipy
import scipy.stats

import math

avg = 15
sd = 10
n = 79
xmin = 16
xmax = 17

ans = scipy.stats.norm.cdf((xmax-avg)/(sd/math.sqrt(n))) - scipy.stats.norm.cdf((xmin-avg)/(sd/math.sqrt(n)))
print(ans)