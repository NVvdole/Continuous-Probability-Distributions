# File Name: Laplace.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import laplace

print("Laplace Distribution")
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
print("")

pdf = laplace.pdf(x, loc = mu, scale = sig)
cdf = laplace.cdf(x, loc = mu, scale = sig)
ccdf = laplace.sf(x, loc = mu, scale = sig)
mean = laplace.mean(loc = mu, scale = sig)
med = laplace.median(loc = mu, scale = sig)
var = laplace.var(loc = mu, scale = sig)
std_dev = laplace.std(loc = mu, scale = sig)
skew = laplace.stats(loc = mu, scale = sig, moments = "s")
kurt = laplace.stats(loc = mu, scale = sig, moments = "k")
ent = laplace.entropy(loc = mu, scale = sig)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
print("Mode(X) = " + str(mu))
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
