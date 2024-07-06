import math
r=1
l=0
n=1000
h=(r-l)/n
integral=0
for i in range(n):
    x_l=i*h
    x_r=(i+1)*h
    integral+=(math.exp(x_l)+math.exp(x_r))/2*h

print(integral)
