# File Name: ChiSquare.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import chi2

print("Chi-Square Distribution")
print("")
print("df = degrees of freedom")
print("x = continuous random variable")
print("")

df = int(input("Enter df: "))
while df < 1:
    df = int(input("Enter df: "))
    
x = float(input("Enter x: "))
if df == 1:
    while x <= 0.0:
        x = float(input("Enter x: "))
else:
    while x < 0.0:
        x = float(input("Enter x: "))
print("")

pdf = chi2.pdf(x, df)
cdf = chi2.cdf(x, df)
ccdf = chi2.sf(x, df)
mean = chi2.mean(df)
med = chi2.median(df)
mode = max(df - 2.0, 0.0)
var = chi2.var(df)
std_dev = chi2.std(df)
skew = chi2.stats(df, moments = "s")
kurt = chi2.stats(df, moments = "k")
ent = chi2.entropy(df)

print("PDF, CDF, and CCDF")
print("fX(" + str(x) + ") = " + str(pdf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))\
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
