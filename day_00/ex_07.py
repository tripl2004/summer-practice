import math
import matplotlib.pyplot as plt

def f(x):
    return math.exp(x)
def s(left, right, step):
    right=1
    left=0
    if step%2!=0:
        raise ValueError
    h=(right-left)/step
    s=math.exp(left)+math.exp()
    
    for i in range(1,step):
        x=i*h
        if i%2==0:
            s+=2*math.exp(x)
        else:
            s+=4*math.exp(x)

    s*= h/3
    return s

left = 0
right = 1
step = 10
steps = []
errors = []

for _ in range(8):
    integral_value = s(left, right, step)
    error = abs(integral_value - (math.exp(1) - 1))
    steps.append(step)
    errors.append(error)
    step *= 10

print("Step\tError")
for i in range(len(steps)):
    print(f"{steps[i]}\t{errors[i]}")

plt.plot(steps, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Количесвто разбиений')
plt.ylabel('Ошибка')
plt.title('Зависисмоть ошибки от количества разиений в методе левых Гаусса ')
plt.grid(True)
plt.show()
