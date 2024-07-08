import math

def f(x):
    return math.exp(x)

def Integral(a, b, n):
    integral=0
    h=(b-a)/n
    x=a
    for i in range(n):
        x+=h
        integral+=(5*f(x-(h/2)*((3/5)**1/2))+5*f(x+(h/2)*((3/5)**1/2))+8*f(x))/18*h
    print(n,abs(integral-(f(1)-1)))

    
left=0
right=1
n=10

for _ in range (7):
    Integral(left, right, n)
    n *= 10


