# File Name: BetaPrime.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import betaprime

print("Beta Prime Distribution")
print("")
print("\u03B11 = first shape parameter")
print("\u03B12 = second shape parameter")
print("x = continuous random variable")
print("")

alpha1 = float(input("Enter \u03B11: "))
while alpha1 <= 0.0:
    alpha1 = float(input("Enter \u03B11: "))
    
alpha2 = float(input("Enter \u03B12: "))
while alpha2 <= 0.0:
    alpha2 = float(input("Enter \u03B12: "))
    
x = float(input("Enter x: "))
while x < 0.0:
    x = float(input("Enter x: "))
print("")

pdf = betaprime.pdf(x, alpha1, alpha2)
cdf = betaprime.cdf(x, alpha1, alpha2)
ccdf = betaprime.sf(x, alpha1, alpha2)
mean = betaprime.mean(alpha1, alpha2)
med = betaprime.median(alpha1, alpha2)
mode = (alpha1 - 1.0) / (alpha2 + 1.0)
var = betaprime.var(alpha1, alpha2)
std_dev = betaprime.std(alpha1, alpha2)
skew = betaprime.stats(alpha1, alpha2, moments = "s")
kurt = betaprime.stats(alpha1, alpha2, moments = "k")
ent = betaprime.entropy(alpha1, alpha2)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
if alpha1 >= 1.0:
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
