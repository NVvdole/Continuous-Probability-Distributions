# File Name: T.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import t

print("T-Distribution")
print("")
print("df = degrees of freedom")
print("x = continuous random variable")
print("")

df = float(input("Enter df: "))
while df <= 0.0:
    df = float(input("Enter df: "))
    
x = float(input("Enter x: "))
print("")

pdf = t.pdf(x, df)
cdf = t.cdf(x, df)
ccdf = t.sf(x, df)
mean = t.mean(df)
med = t.median(df)
var = t.var(df)
std_dev = t.std(df)
skew = t.stats(df, moments = "s")
kurt = t.stats(df, moments = "k")
ent = t.entropy(df)

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
