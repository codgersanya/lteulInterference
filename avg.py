#!/usr/bin/env python3
#avgpmRadioRecInterferencePwrBrPrbdBm = 10 * ln((sumpmRadioRecInterferencePwrBrPrb/n) * .00000000000005684341886080801486968994140625 / (900000 / 40))

#******************************************************#
#                                                      #
#                 I N I T I A L                        #
#               V A R I A B L E S                      #
#              Edit before running!                    #
#                                                      #
#******************************************************#

path = '/home/shared/pszaraz/lteulInterference'

#*********** Initial variables ends *******************#

import math
import re

def ln(x):
    return(math.log(x, 10))

with open(path+'/raw.txt', 'r') as raw:
   for line in re.findall('pmRadioRecInterferencePwrBrPrb*.*', raw.read()):
      with open(path+'/raw2.txt', 'a') as raw2:
         try:
            var1, var2 = line.split()
         except:
            var1 = line
         else:
            raw2.write(var2 + '\n')

n = 0
sumpmRadioRecInterferencePwrBrPrb = 0
with open(path+'/raw2.txt', 'r') as raw:
   for line in raw:
      pmRadioRecInterferencePwrBrPrb = int(line)
      if pmRadioRecInterferencePwrBrPrb > 0:
         n = n + 1
         sumpmRadioRecInterferencePwrBrPrb += pmRadioRecInterferencePwrBrPrb
      if sumpmRadioRecInterferencePwrBrPrb > 0:
         avgpmRadioRecInterferencePwrBrPrbdBm = 10 * ln((sumpmRadioRecInterferencePwrBrPrb/n) * .00000000000005684341886080801486968994140625 / (900000 / 40))
      else:
         avgpmRadioRecInterferencePwrBrPrbdBm = 0

with open(path+'/avg.txt', 'w') as avg:
   avg.write(str(avgpmRadioRecInterferencePwrBrPrbdBm))

print('n:', n)
print('sumpmRadioRecInterferencePwrBrPrb:', sumpmRadioRecInterferencePwrBrPrb)
print('avgpmRadioRecInterferencePwrBrPrbdBm:', avgpmRadioRecInterferencePwrBrPrbdBm)