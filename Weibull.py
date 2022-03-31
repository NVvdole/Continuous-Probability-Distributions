# File Name: Weibull.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import weibull_min

print("Weibull Distribution")
print("")
print("\u03B1 = shape parameter")
print("\u03B2 = scale parameter")
print("x = continuous random variable")
print("")

alpha = float(input("Enter \u03B1: "))
while alpha <= 0.0:
    alpha = float(input("Enter \u03B1: "))
    
beta = float(input("Enter \u03B2: "))
while beta <= 0.0:
    beta = float(input("Enter \u03B2: "))
    
x = float(input("Enter x: "))
while x < 0.0:
    x = float(input("Enter x: "))
print("")

pdf = weibull_min.pdf(x, alpha, scale = beta)
cdf = weibull_min.cdf(x, alpha, scale = beta)
ccdf = weibull_min.sf(x, alpha, scale = beta)
mean = weibull_min.mean(alpha, scale = beta)
med = weibull_min.median(alpha, scale = beta)
mode = beta * pow((alpha - 1.0) / alpha, 1.0 / alpha)
var = weibull_min.var(alpha, scale = beta)
std_dev = weibull_min.std(alpha, scale = beta)
skew = weibull_min.stats(alpha, scale = beta, moments = "s")
kurt = weibull_min.stats(alpha, scale = beta, moments = "k")
ent = weibull_min.entropy(alpha, scale = beta)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
if alpha > 1.0:
    print("Mode(X) = " + str(mode))
else:
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
