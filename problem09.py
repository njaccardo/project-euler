# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math
import pdb 


def calcultateSUM(i):
	j = 1
	while True:
		c = (i**2 + j**2)**0.5
		if c > 1000 or j > 1000:
			j = 0
			# pdb.set_trace()
			return j
			break
		if i + j + c != 1000:
			j +=1
			continue
		else:
			# pdb.set_trace()
			return j



ii = 1 
while True:
	j = calcultateSUM(ii)
	# j = int(j)
	if j == 0:
		ii +=1
		continue
	else:
		# pdb.set_trace()
		c = (ii**2+j**2)**0.5
		print(ii+j+c)
		break

print(ii*j*c)
