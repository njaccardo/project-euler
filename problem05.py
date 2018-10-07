# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# in retrospect some published solutions used the definition of greatest common divisor:
# (from wikipedia) greatest common divsior of two or more integers
# is the largest positive integer that divides each of the integers
# i.e. for 8 and 12 it is 4

from datetime import datetime
startTime = datetime.now()

# define a function to figure out if a number is divisible by the values of 1:20
def isDivisible(val):
	for i in range(2,21):
		if val % i != 0:
			return False
	return True


# loop to find the number
val = 20 # start there bc it has to be divisible by 20
while True:
	if isDivisible(val):
		break

	val += 20

print(val)
print(datetime.now() - startTime)


# published much quicker version ... 
startTime = datetime.now()
def gcd(x,y): 
	return y and gcd(y, x % y) or x
def lcm(x,y): 
	return x * y / gcd(x,y)

n = 1
for i in range(1, 21):
     n = lcm(n, i)
print(n)
print(datetime.now() - startTime)
