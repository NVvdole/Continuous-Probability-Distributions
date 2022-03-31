# File Name: Dirichlet.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import dirichlet
from scipy.stats import beta

print("Dirichlet Distribution")
print("")
print("\u03B11 = first shape parameter")
print("\u03B12 = second shape parameter")
print("\u03B13 = third shape parameter")
print("x1 = first continuous random variable")
print("x2 = second continuous random variable")
print("x3 = third continuous random variable")
print("")
    
alpha = []
temp = float(input("Enter \u03B11: "))
while temp <= 0.0:
    temp = float(input("Enter \u03B11: "))
alpha.append(temp)
temp = float(input("Enter \u03B12: "))
while temp <= 0.0:
    temp = float(input("Enter \u03B12: "))
alpha.append(temp)
temp = float(input("Enter \u03B12: "))
while temp <= 0.0:
    temp = float(input("Enter \u03B12: "))
alpha.append(temp)

x = []
temp = float(input("Enter x1: "))
while temp < 0.0 or temp > 1.0:
    temp = float(input("Enter x1: "))
x.append(temp)
temp = float(input("Enter x2: "))
while temp < 0.0 or temp > 1.0 - x[0]:
    temp = float(input("Enter x2: "))
x.append(temp)
temp = float(input("Enter x3: "))
while temp < 0.0 or temp > 1.0 - x[0] - x[1]:
    temp = float(input("Enter x3: "))
x.append(temp)
print("")

jpdf = dirichlet.pdf(x, alpha)
mpdf1 = beta.pdf(x[0], alpha[0], sum(alpha) - alpha[0])
mpdf2 = beta.pdf(x[1], alpha[1], sum(alpha) - alpha[1])
mpdf3 = beta.pdf(x[2], alpha[2], sum(alpha) - alpha[2])

mcdf1 = beta.cdf(x[0], alpha[0], sum(alpha) - alpha[0])
mcdf2 = beta.cdf(x[1], alpha[1], sum(alpha) - alpha[1])
mcdf3 = beta.cdf(x[2], alpha[2], sum(alpha) - alpha[2])

mccdf1 = beta.sf(x[0], alpha[0], sum(alpha) - alpha[0])
mccdf2 = beta.sf(x[1], alpha[1], sum(alpha) - alpha[1])
mccdf3 = beta.sf(x[2], alpha[2], sum(alpha) - alpha[2])

mean1 = beta.mean(alpha[0], sum(alpha) - alpha[0])
mean2 = beta.mean(alpha[1], sum(alpha) - alpha[1])
mean3 = beta.mean(alpha[2], sum(alpha) - alpha[2])

med1 = beta.median(alpha[0], sum(alpha) - alpha[0])
med2 = beta.median(alpha[1], sum(alpha) - alpha[1])
med3 = beta.median(alpha[2], sum(alpha) - alpha[2])

mode1 = (alpha[0] - 1.0) / (sum(alpha) - 3.0)
mode2 = (alpha[1] - 1.0) / (sum(alpha) - 3.0)
mode3 = (alpha[2] - 1.0) / (sum(alpha) - 3.0)

var1 = beta.var(alpha[0], sum(alpha) - alpha[0])
var2 = beta.var(alpha[1], sum(alpha) - alpha[1])
var3 = beta.var(alpha[2], sum(alpha) - alpha[2])

std_dev1 = beta.std(alpha[0], sum(alpha) - alpha[0])
std_dev2 = beta.std(alpha[1], sum(alpha) - alpha[1])
std_dev3 = beta.std(alpha[2], sum(alpha) - alpha[2])

skew1 = beta.stats(alpha[0], sum(alpha) - alpha[0], moments = "s")
skew2 = beta.stats(alpha[1], sum(alpha) - alpha[1], moments = "s")
skew3 = beta.stats(alpha[2], sum(alpha) - alpha[2], moments = "s")

kurt1 = beta.stats(alpha[0], sum(alpha) - alpha[0], moments = "k")
kurt2 = beta.stats(alpha[1], sum(alpha) - alpha[1], moments = "k")
kurt3 = beta.stats(alpha[2], sum(alpha) - alpha[2], moments = "k")

ent1 = beta.entropy(alpha[0], sum(alpha) - alpha[0])
ent2 = beta.entropy(alpha[1], sum(alpha) - alpha[1])
ent3 = beta.entropy(alpha[2], sum(alpha) - alpha[2])

cov1 = (-(alpha[0] * alpha[1])) / (pow(sum(alpha), 2) * (sum(alpha) + 1.0))
cov2 = (-(alpha[0] * alpha[2])) / (pow(sum(alpha), 2) * (sum(alpha) + 1.0)) 
cov3 = (-(alpha[1] * alpha[2])) / (pow(sum(alpha), 2) * (sum(alpha) + 1.0))

corr1 = cov1 / (std_dev1 * std_dev2)
corr2 = cov2 / (std_dev1 * std_dev3)
corr3 = cov3 / (std_dev2 * std_dev3)

print("PDFs")
print("fX1,X2,X3(" + str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ") = " + str(jpdf))
print("fX1(" + str(x[0]) + ") = " + str(mpdf1))
print("fX2(" + str(x[1]) + ") = " + str(mpdf2))
print("fX3(" + str(x[2]) + ") = " + str(mpdf3))
print("")

print("CDFs")
print("FX1(" + str(x[0]) + ") = " + str(mcdf1))
print("FX2(" + str(x[1]) + ") = " + str(mcdf2))
print("FX3(" + str(x[2]) + ") = " + str(mcdf3))
print("")

print("CCDFs")
print("FX1c(" + str(x[0]) + ") = " + str(mccdf1))
print("FX2c(" + str(x[1]) + ") = " + str(mccdf2))
print("FX3c(" + str(x[2]) + ") = " + str(mccdf3))
print("")

print("Means")
print("E(X1) = " + str(mean1))
print("E(X2) = " + str(mean2))
print("E(X3) = " + str(mean3))
print("")

print("Medians")
print("Med(X1) = " + str(med1))
print("Med(X2) = " + str(med2))
print("Med(X3) = " + str(med3))
print("")

print("Modes")
if alpha[0] > 1.0 and sum(alpha) - alpha[0] > 1.0:
    print("Mode(X1) = " + str(mode1))
elif alpha[0] < 1.0 and sum(alpha) - alpha[0] < 1.0:
    print("Mode(X1) = 0.0, 1.0")
elif alpha[0] <= 1.0 and sum(alpha) - alpha[0] > 1.0:
    print("Mode(X1) = 0.0")
elif alpha[0] > 1.0 and sum(alpha) - alpha[0] <= 1.0:
    print("Mode(X1) = 1.0")
else:
    print("Mode(X1) = N/A")
if alpha[1] > 1.0 and sum(alpha) - alpha[1] > 1.0:
    print("Mode(X2) = " + str(mode2))
elif alpha[1] < 1.0 and sum(alpha) - alpha[1] < 1.0:
    print("Mode(X2) = 0.0, 1.0")
elif alpha[1] <= 1.0 and sum(alpha) - alpha[1] > 1.0:
    print("Mode(X2) = 0.0")
elif alpha[1] > 1.0 and sum(alpha) - alpha[1] <= 1.0:
    print("Mode(X2) = 1.0")
else:
    print("Mode(X2) = N/A")
if alpha[2] > 1.0 and sum(alpha) - alpha[2] > 1.0:
    print("Mode(X3) = " + str(mode3))
elif alpha[2] < 1.0 and sum(alpha) - alpha[2] < 1.0:
    print("Mode(X3) = 0.0, 1.0")
elif alpha[2] <= 1.0 and sum(alpha) - alpha[2] > 1.0:
    print("Mode(X3) = 0.0")
elif alpha[2] > 1.0 and sum(alpha) - alpha[2] <= 1.0:
    print("Mode(X3) = 1.0")
else:
    print("Mode(X3) = N/A")
print("")

print("Variances")
print("Var(X1) = " + str(var1))
print("Var(X2) = " + str(var2))
print("Var(X3) = " + str(var3))
print("")

print("Standard Deviations")
print("SD(X1) = " + str(std_dev1))
print("SD(X2) = " + str(std_dev2))
print("SD(X3) = " + str(std_dev3))
print("")

print("Skewnesses")
print("Skew(X1) = " + str(skew1))
print("Skew(X2) = " + str(skew2))
print("Skew(X3) = " + str(skew3))
print("")

print("Kurtoses")
print("Kurt(X1) = " + str(kurt1))
print("Kurt(X2) = " + str(kurt2))
print("Kurt(X3) = " + str(kurt3))
print("")

print("Entropies")
print("H(X1) = " + str(ent1))
print("H(X2) = " + str(ent2))
print("H(X3) = " + str(ent3))
print("")

print("Covariances")
print("Cov(X1, X2) = " + str(cov1))
print("Cov(X1, X3) = " + str(cov2))
print("Cov(X2, X3) = " + str(cov3))
print("")

print("Correlation Coefficients")
print("Corr(X1, X2) = " + str(corr1))
print("Corr(X1, X3) = " + str(corr2))
print("Corr(X2, X3) = " + str(corr3))
