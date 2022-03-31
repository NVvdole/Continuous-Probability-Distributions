# File Name: F.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import f

print("F-Distribution")
print("")
print("df1 = numerator degrees of freedom")
print("df2 = denominator degrees of freedom")
print("x = continuous random variable")
print("")

df1 = int(input("Enter df1: "))
while df1 < 1:
    df1 = int(input("Enter df1: "))
    
df2 = int(input("Enter df2: "))
while df2 < 1:
    df2 = int(input("Enter df2: "))
    
x = float(input("Enter x: "))
if df1 == 1:
    while x <= 0.0:
        x = float(input("Enter x: "))
else:
    while x < 0.0:
        x = float(input("Enter x: "))
print("")

pdf = f.pdf(x, df1, df2)
cdf = f.cdf(x, df1, df2)
ccdf = f.sf(x, df1, df2)
mean = f.mean(df1, df2)
med = f.median(df1, df2)
mode = ((df1 - 2.0) / df1) * (df2 / (df2 + 2.0))
var = f.var(df1, df2)
std_dev = f.std(df1, df2)
skew = f.stats(df1, df2, moments = "s")
kurt = f.stats(df1, df2, moments = "k")
ent = f.entropy(df1, df2)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
if df1 > 2:
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
