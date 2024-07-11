import numpy as np

l = np.exp(1) - 1

def s(f, a, b, n):
    random_points = np.random.uniform(a, b, n)
    f_v = f(random_points)
    average_value = np.mean(f_v)
    integral = (b - a) * average_value
    return integral

def f(x):
    return np.exp(x)

a=0
b=1
n = [10, 100, 1000, 10000, 100000]

for n in n:
    e_l = s(f, a, b, n)
    error = abs(e_l - l)
    print(n,e_l,error)
