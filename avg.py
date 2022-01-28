#!/usr/bin/env python3
#UlInterference in dBm = 10*LOG(10^-3*(sumpmRadioRecInterferencePwrBrPrb/2^-44))

#*********** Initial variables***************#
path = '/home/shared/pszaraz/lteulInterference/'
#*********** Initial variables***************#

import math
import re

def ln(x):
    return(math.log(x, 10))

with open(path+'raw.txt', 'r') as raw:
   for line in re.findall('pmRadioRecInterferencePwrBrPrb*.*', raw.read()):
      with open(path+'raw2.txt', 'a') as raw2:
         var1, var2 = line.split()
         raw2.write(var2 + '\n')
         print(line)

n = 0
sumpmRadioRecInterferencePwrBrPrb = 0
with open(path+'raw2.txt', 'r') as raw:
   for line in raw:
      pmRadioRecInterferencePwrBrPrb = int(line)
      if pmRadioRecInterferencePwrBrPrb > 0:
         n = n + 1
         sumpmRadioRecInterferencePwrBrPrb += pmRadioRecInterferencePwrBrPrb
         avgpmRadioRecInterferencePwrBrPrbdBm = 10 * ln((sumpmRadioRecInterferencePwrBrPrb/n) * 2**-44)
      else:
         avgpmRadioRecInterferencePwrBrPrbdBm = 0

with open(path+'avg.txt', 'w') as avg:
   avg.write(str(avgpmRadioRecInterferencePwrBrPrbdBm))