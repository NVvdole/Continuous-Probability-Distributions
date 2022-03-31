# File Name: Lognormal.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import lognorm
import math

print("Lognormal Distribution")
print("")
print("\u03BC = location parameter")
print("\u03C3 = scale parameter")
print("x = continuous random variable")
print("")

mu = float(input("Enter \u03BC: "))

sig = float(input("Enter \u03C3: "))
while sig <= 0.0:
    sig = float(input("Enter \u03C3: "))
    
x = float(input("Enter x: "))
while x <= 0.0:
    x = float(input("Enter x: "))
print("")

pdf = lognorm.pdf(x, sig, loc = mu)
cdf = lognorm.cdf(x, sig, loc = mu)
ccdf = lognorm.sf(x, sig, loc = mu)
mean = lognorm.mean(sig, loc = mu)
med = lognorm.median(sig, loc = mu)
mode = math.exp(mu - pow(sig, 2))
var = lognorm.var(sig, loc = mu)
std_dev = lognorm.std(sig, loc = mu)
skew = lognorm.stats(sig, loc = mu, moments = "s")
kurt = lognorm.stats(sig, loc = mu, moments = "k")
ent = lognorm.entropy(sig, loc = mu)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
print("Mode(X) = " + str(mode))
print("")

print("Variance and Standard Deviation")
print("Var(X) = " + str(var))
print("SD(X) = " + str(std_dev))
print("")

print("Skewness and Kurtosis")
print("Skew(X) = " + str(skew))
print("Kurt(X) = " + str(kurt))
print("")

print("Entropy")
print("H(X) = " + str(ent))
