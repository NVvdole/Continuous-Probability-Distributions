# File Name: ContinuousUniform.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

import math

print("Continuous Uniform Distribution")
print("")
print("a = lower bound")
print("b = upper bound")
print("x = continuous random variable")
print("")

a = float(input("Enter a: "))

b = float(input("Enter b: "))
while b <= a:
    b = float(input("Enter b: "))
    
x = float(input("Enter x: "))
while x < a or x > b:
    x = float(input("Enter x: "))
print("")

pdf = 1.0 / (b - a)
cdf = (x - a) / (b - a)
ccdf = 1.0 - cdf
mean = (a + b) / 2.0
med = (a + b) / 2.0
var = pow(b - a, 2) / 12.0
std_dev = math.sqrt(var)
kurt = -6.0 / 5.0
ent = math.log(b - a)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
print("Mode(X) = N/A")
print("")

print("Variance and Standard Deviation")
print("Var(X) = " + str(var))
print("SD(X) = " + str(std_dev))
print("")

print("Skewness and Kurtosis")
print("Skew(X) = 0.0")
print("Kurt(X) = " + str(kurt))
print("")

print("Entropy")
print("H(X) = " + str(ent))
