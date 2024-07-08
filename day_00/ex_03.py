import math

def f(x):
    return math.exp(x)

def Integral(l, r, n):    
    r=1
    l=0
    h=(r-l)/n
    integral=0
    for i in range(n):
        x_l=i*h
        x_r=(i+1)*h
        integral+=(f(x_l)+f(x_r))/2*h

    print(n,abs(integral-(f(1)-1)))

    
left=0
right=1
n=10

for _ in range (7):
    Integral(left, right, n)
    n *= 10
