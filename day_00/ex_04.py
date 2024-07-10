import math
def f(x):
    return math.exp(x)

def Integral(l, r, n):
    r=1
    l=0
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


    print(n,abs(integral-(f(1)-1)))

    
left=0
right=1
n=10

for _ in range (7):
    Integral(left, right, n)
    n *= 10
