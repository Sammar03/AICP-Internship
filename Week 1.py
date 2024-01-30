# AICP Internship Week 1

import numpy as np;

# Generating an Array of All Even Integers from 30 to 70 (Task 1)
rang = np.arange(30,71,1)
print("All Even Numbers between 30 and 70:")
print(rang)

# Generating an Array of 15 Random Numbers from Standard Normal Distribution (Task 2)
rand = np.random.default_rng()
rand1 = rand.random(15)
print("15 Randomly  Generated Numbers:")
print(rand1)

# Calculating the Cross Product of two Matrices (Task 3)
a = [1,2,3]
b = [3,5,7]
cr = np.cross(a,b)
print(cr)

# Calculating the Determinant of an Array (Task 4)
c = [[1,2,3],[4,6,7],[3,4,8]]
det = np.linalg.det(c)
print(det)

# Generating a 3x3x3 Array with Random Values (Task 5)
low = 1
high = 13
three = np.random.randint(low, high, size =(3,3,3))
print(three)

# Generating a 5x5 eith Random Values and Calculating its Maximum and Minimum Values (Task 6)
five = np.random.randint(low, high, size =(5,5))
min = five.min()
max = five.max()
print(five)
print(min)
print(max)

# Computing the Mean, Standard Deviation and the Variance of an Array along its Second Axis (Task 7)
std = five.std(axis = 1)
var = five.var(axis = 1)
mean = five.mean(axis = 1)
print(mean)
print(var)
print(std)



