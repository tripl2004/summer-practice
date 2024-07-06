import math
r=1
l=0
n=1000
if n%2!=0:
    raise ValueError
h=(r-l)/n
integral=math.exp(l)+math.exp(r)
for i in range(1,n):
    x=i*h
    if i%2==0:
        integral+=2*math.exp(x)
    else:
        integral+=4*math.exp(x)

integral *= h/3


print(integral)
