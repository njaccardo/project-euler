# A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import pdb
import math
# import numpy as np

ival2 = []
count = 1
for i in range(100,999):
	for j in range(100,999):

		if i == j:
			continue

		sum0 = i*j
		sum1 = str(sum0)
		if len(sum1) == 5:
			if sum1[:2] == sum1[4]+sum1[3]:
				ival2.append(sum0)
				# print(sum1)
		elif len(sum1) == 6:
			if sum1[:3] == sum1[5]+sum1[4]+sum1[3]:
				ival2.append(sum0)
				# print(sum1)
# pdb.set_trace()


print(max(ival2))