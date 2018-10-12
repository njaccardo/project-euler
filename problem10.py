# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import pdb
import numpy as np
# First find all the prime numbers less than 2 million
def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			return False
	return True


# loop to find all primes
primes = [2,3]
val = 3
while val < 1999998:
	val += 2
	if isPrime(val):
		primes.append(val)
		print(val)
	else:
		continue

print(sum(primes))
pdb.set_trace()


# a faster way if you know about the 
# seive fo Eratosthenes

from math import sqrt
def sum_primes(maxprime):
    sieve = np.arange(maxprime+1)
    sieve[1] = 0
    for n in range(2, int(sqrt(maxprime))+1):

        if sieve[n] > 0:
            for i in range(n*n, maxprime+1, n): 
            	sieve[i] = 0
    return sum(sieve)

print(sum_primes(2000000))