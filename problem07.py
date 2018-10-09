# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import pdb

# define a function that determines if the number is prime
def isPrime(n):
    # reduce the number by values of 2 first
    while n % 2 == 0:
        n = n/2

    # next figure out the odd factors
    o = 3
    count = 0

    while n != 1:
        while n % o == 0:
            count += 1
            n = n/o
        o += 2
    # break only if there's only one factor
    if count == 1:
    	return True
    else:
    	return False


iprime = 2 # start at 2 
count = 1
val = 3 # first number to check

# loop until we get to the prime number 
while count < 10001:
    if isPrime(val):
        iprime = val
        count += 1
    val += 2 # only need to check odd numbers

print(iprime)




