# File Name: Beta.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import beta

print("Beta Distribution")
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
while x < 0.0 or x > 1.0:
    x = float(input("Enter x: "))
print("")

pdf = beta.pdf(x, alpha1, alpha2)
cdf = beta.cdf(x, alpha1, alpha2)
ccdf = beta.sf(x, alpha1, alpha2)
mean = beta.mean(alpha1, alpha2)
med = beta.median(alpha1, alpha2)
mode = (alpha1 - 1.0) / (alpha1 + alpha2 - 2.0)
var = beta.var(alpha1, alpha2)
std_dev = beta.std(alpha1, alpha2)
skew = beta.stats(alpha1, alpha2, moments = "s")
kurt = beta.stats(alpha1, alpha2, moments = "k")
ent = beta.entropy(alpha1, alpha2)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
if alpha1 > 1.0 and alpha2 > 1.0:
    print("Mode(X) = " + str(mode))
elif alpha1 < 1.0 and alpha2 < 1.0:
    print("Mode(X) = 0.0, 1.0")
elif alpha1 <= 1.0 and alpha2 > 1.0:
    print("Mode(X) = 0.0")
elif alpha1 > 1.0 and alpha2 <= 1.0:
    print("Mode(X) = 1.0")
else:
    print("Mode(X) = N/A")
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
