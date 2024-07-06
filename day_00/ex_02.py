import math
r=1
l=0
n=1000
h=(r-l)/n
integral=0
for i in range(n):
    x=i*h
    integral+=math.exp(x+(h/2))*h

print(integral)
