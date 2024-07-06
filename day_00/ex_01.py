import math
r=1
l=0
n=10
h=(r-l)/n
integral=0
for i in range(n):
    x=i*h
    integral+=math.exp(x)*h;

print(integral)


