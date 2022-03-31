# File Name: Chi.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import chi
import math

print("Chi Distribution")
print("")
print("df = degrees of freedom")
print("x = continuous random variable")
print("")

df = int(input("Enter df: "))
while df < 1:
    df = int(input("Enter df: "))
    
x = float(input("Enter x: "))
while x < 0.0:
    x = float(input("Enter x: "))
print("")

pdf = chi.pdf(x, df)
cdf = chi.cdf(x, df)
ccdf = chi.sf(x, df)
mean = chi.mean(df)
med = chi.median(df)
mode = math.sqrt(df - 1.0)
var = chi.var(df)
std_dev = chi.std(df)
skew = chi.stats(df, moments = "s")
kurt = chi.stats(df, moments = "k")
ent = chi.entropy(df)

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
