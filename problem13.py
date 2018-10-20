# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import pdb

# First read in the number and calculate the sum

file = 'number_problem13.txt'
fid = open(file,"r")

count = 0
num = 0
line = fid.readlines()

for i in range(0,len(line)):
	num = num+int(line[i].rstrip())

print(str(num)[:10])
