# File Name: Gamma.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import gamma

print("Gamma Distribution")
print("")
print("\u03B1 = shape parameter")
print("\u03BB = rate parameter")
print("x = continuous random variable")
print("")

alpha = float(input("Enter \u03B1: "))
while alpha <= 0.0:
    alpha = float(input("Enter \u03B1: "))
    
lamb = float(input("Enter \u03BB: "))
while lamb <= 0.0:
    lamb = float(input("Enter \u03BB: "))
    
x = float(input("Enter x: "))
while x < 0.0:
    x = float(input("Enter x: "))
print("")

pdf = gamma.pdf(x, alpha, scale = 1.0 / lamb)
cdf = gamma.cdf(x, alpha, scale = 1.0 / lamb)
ccdf = gamma.sf(x, alpha, scale = 1.0 / lamb)
mean = gamma.mean(alpha, scale = 1.0 / lamb)
med = gamma.median(alpha, scale = 1.0 / lamb)
mode = (alpha - 1.0) / lamb
var = gamma.var(alpha, scale = 1.0 / lamb)
std_dev = gamma.std(alpha, scale = 1.0 / lamb)
skew = gamma.stats(alpha, scale = 1.0 / lamb, moments = "s")
kurt = gamma.stats(alpha, scale = 1.0 / lamb, moments = "k")
ent = gamma.entropy(alpha, scale = 1.0 / lamb)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
if alpha >= 1.0:
    print("Mode(X) = " + str(mode))
else:
    print("Mode(X) = inf")
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
