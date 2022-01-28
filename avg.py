#!/usr/bin/env python3
#=10*LOG(10^-3*(sumpmRadioRecInterferencePwrBrPrb/2^-44))
import math
import re

with open('/home/shared/pszaraz/lteulInterference/raw.txt', 'r') as raw:
   for line in re.findall('pmRadioRecInterferencePwrBrPrb*.*', raw.read()):
      with open('/home/shared/pszaraz/lteulInterference/raw2.txt', 'a') as raw2:
         var1, var2 = line.split()
         raw2.write(var2 + '\n')
         print(line)

n = 0
sumpmRadioRecInterferencePwrBrPrb = 0
with open('/home/shared/pszaraz/lteulInterference/raw2.txt', 'r') as raw:
   for line in raw:
      pmRadioRecInterferencePwrBrPrb = int(line)
      if pmRadioRecInterferencePwrBrPrb > 0:
         n = n + 1
         print(pmRadioRecInterferencePwrBrPrb)
         sumpmRadioRecInterferencePwrBrPrb += pmRadioRecInterferencePwrBrPrb
         avgpmRadioRecInterferencePwrBrPrb = (sumpmRadioRecInterferencePwrBrPrb/n)
         avgpmRadioRecInterferencePwrBrPrbmWatt = avgpmRadioRecInterferencePwrBrPrb * (2**-44)
         avgpmRadioRecInterferencePwrBrPrbdBm = 10 * math.log(avgpmRadioRecInterferencePwrBrPrbmWatt)
      else:
         avgpmRadioRecInterferencePwrBrPrbdBm = 0

with open('/home/shared/pszaraz/lteulInterference/avg.txt', 'w') as avg:
   avg.write(str(avgpmRadioRecInterferencePwrBrPrbdBm))

print('The avg is:', avgpmRadioRecInterferencePwrBrPrbdBm)
print('Number of lines is:', n)