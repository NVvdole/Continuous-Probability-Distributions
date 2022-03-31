# File Name: Exponential.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import expon

print("Exponential Distribution")
print("")
print("\u03BB = rate parameter")
print("x = continuous random variable")
print("")

lamb = float(input("Enter \u03BB: "))
while lamb <= 0.0:
    lamb = float(input("Enter \u03BB: "))
    
x = float(input("Enter x: "))
while x < 0.0:
    x = float(input("Enter x: "))
print("")

pdf = expon.pdf(x, scale = 1.0 / lamb)
cdf = expon.cdf(x, scale = 1.0 / lamb)
ccdf = expon.sf(x, scale = 1.0 / lamb)
mean = expon.mean(scale = 1.0 / lamb)
med = expon.median(scale = 1.0 / lamb)
var = expon.var(scale = 1.0 / lamb)
std_dev = expon.std(scale = 1.0 / lamb)
skew = expon.stats(scale = 1.0 / lamb, moments = "s")
kurt = expon.stats(scale = 1.0 / lamb, moments = "k")
ent = expon.entropy(scale = 1.0 / lamb)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
print("Mode(X) = 0.0")
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
