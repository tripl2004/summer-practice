import math

def right_difference_derivative(f, x, h):
  return (f(x + h) - f(x)) / h


def y(x):
  return math.exp(x)

x = 0
h = 0.001

derivative = right_difference_derivative(y, x, h)


print(f"Производная функции y = e^x в точке x = {x} равна: {derivative}")
