import math
def f(x):
    return 2*x**4-math.sin(x)+24*x**6
l=-10
r=20
n=10
h=(r-l)/n
integral=0
for i in range(n):
    x=l+i*h
    integral+=f(x)*h

print(integral)

l=-10
r=20
n=10
h=(r-l)/n
integral1=0
for i in range(n):
    x=l+i*h
    integral1+=f(x+(h/2))*h

print(integral1)

l=-10
r=20
n=10
h=(r-l)/n
integral=0
for i in range(n):
    x_l=l+i*h
    x_r=l+(i+1)*h
    integral+=(f(x_l)+f(x_r))/2*h

print(integral)


l=-10
r=20
n=100
if n%2!=0:
    raise ValueError
h=(r-l)/n
integral=math.exp(l)+math.exp(r)
for i in range(1,n):
    x=l+i*h
    if i%2==0:
        integral+=2*math.exp(x)
    else:
        integral+=4*math.exp(x)

integral *= h/3


print(integral)
a=-10
b=20
n=10
    
integral=0
h=(b-a)/n
x=a
for i in range(n):
    x+=h
    integral+=(5*f(x-(h/2)*((3/5)**1/2))+5*f(x+(h/2)*((3/5)**1/2))+8*f(x))/18*h
print(integral)




