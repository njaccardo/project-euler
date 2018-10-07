# Project Euler problem #3
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import pdb
import math

n0 = 600851475143
n = n0
i = 3
ival = []
for i in range(3,int(math.sqrt(n0)),2):
	if n % i == 0:
		n = n/i
		ival.append(i)

print(max(ival))


# # print(n)


  