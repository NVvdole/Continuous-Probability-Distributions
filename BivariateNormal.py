# File Name: BivariateNormal.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import multivariate_normal
from scipy.stats import norm

print("Bivariate Normal Distribution")
print("")
print("\u03BCx = first location parameter")
print("\u03BCy = second location parameter")
print("\u03C3x = first scale parameter")
print("\u03C3y = second scale parameter")
print("\u03C1 = correlation coefficient")
print("x = first continuous random variable")
print("y = second continuous random variable")
print("")

mu1 = float(input("Enter \u03BCx: "))
mu2 = float(input("Enter \u03BCy: "))

sig1 = float(input("Enter \u03C3x: "))
while sig1 <= 0.0:
    sig1 = float(input("Enter \u03C3x: "))
sig2 = float(input("Enter \u03C3y: "))
while sig2 <= 0.0:
    sig2 = float(input("Enter \u03C3y: "))

rho = float(input("Enter \u03C1: "))
while rho < -1.0 or rho > 1.0:
    rho = float(input("Enter \u03C1: "))
    
x = float(input("Enter x: "))
y = float(input("Enter y: "))
print("")

var1 = norm.var(loc = mu1, scale = sig1)
var2 = norm.var(loc = mu2, scale = sig2)
cov = rho * sig1 * sig2

jpdf = multivariate_normal.pdf([x, y], mean = [mu1, mu2], cov = [[var1, cov], [cov, var2]])
mpdf1 = norm.pdf(x, loc = mu1, scale = sig1)
mpdf2 = norm.pdf(y, loc = mu2, scale = sig2)

jcdf = multivariate_normal.cdf([x, y], mean = [mu1, mu2], cov = [[var1, cov], [cov, var2]])
mcdf1 = norm.cdf(x, loc = mu1, scale = sig1)
mcdf2 = norm.cdf(y, loc = mu2, scale = sig2)

jccdf = 1.0 - jcdf
mccdf1 = norm.sf(x, loc = mu1, scale = sig1)
mccdf2 = norm.sf(y, loc = mu2, scale = sig2)

mean1 = norm.mean(loc = mu1, scale = sig1)
mean2 = norm.mean(loc = mu2, scale = sig2)

med1 = norm.median(loc = mu1, scale = sig1)
med2 = norm.median(loc = mu2, scale = sig2)

std_dev1 = norm.std(loc = mu1, scale = sig1)
std_dev2 = norm.std(loc = mu2, scale = sig2)

skew1 = norm.stats(loc = mu1, scale = sig1, moments = "s")
skew2 = norm.stats(loc = mu2, scale = sig2, moments = "s")

kurt1 = norm.stats(loc = mu1, scale = sig1, moments = "k")
kurt2 = norm.stats(loc = mu2, scale = sig2, moments = "k")

ent1 = norm.entropy(loc = mu1, scale = sig1)
ent2 = norm.entropy(loc = mu2, scale = sig2)

print("PDFs")
print("fX,Y(" + str(x) + ", " + str(y) + ") = " + str(jpdf))
print("fX(" + str(x) + ") = " + str(mpdf1))
print("fY(" + str(y) + ") = " + str(mpdf2))
print("")

print("CDFs")
print("FX,Y(" + str(x) + ", " + str(y) + ") = " + str(jcdf))
print("FX(" + str(x) + ") = " + str(mcdf1))
print("FY(" + str(y) + ") = " + str(mcdf2))
print("")

print("CCDFs")
print("FX,Yc(" + str(x) + ", " + str(y) + ") = " + str(jccdf))
print("FXc(" + str(x) + ") = " + str(mccdf1))
print("FYc(" + str(y) + ") = " + str(mccdf2))
print("")

print("Means")
print("E(X) = " + str(mean1))
print("E(Y) = " + str(mean2))
print("")

print("Medians")
print("Med(X) = " + str(med1))
print("Med(Y) = " + str(med2))
print("")

print("Modes")
print("Mode(X) = " + str(mu1))
print("Mode(Y) = " + str(mu2))
print("")

print("Variances")
print("Var(X) = " + str(var1))
print("Var(Y) = " + str(var2))
print("")

print("Standard Deviations")
print("SD(X) = " + str(std_dev1))
print("SD(Y) = " + str(std_dev2))
print("")

print("Skewnesses")
print("Skew(X) = " + str(skew1))
print("Skew(Y) = " + str(skew2))
print("")

print("Kurtoses")
print("Kurt(X) = " + str(kurt1))
print("Kurt(Y) = " + str(kurt2))
print("")

print("Entropies")
print("H(X) = " + str(ent1))
print("H(Y) = " + str(ent2))
print("")

print("Covariance")
print("Cov(X, Y) = " + str(cov))
