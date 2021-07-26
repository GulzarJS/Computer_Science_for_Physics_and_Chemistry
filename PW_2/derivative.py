from math import *
import random
import matplotlib.pyplot as plt

def function(value):
    return pow(value, 2)


def derivative(func, value, deltax):
    numerator = func(value + deltax) - func(value)
    denominator = deltax
    slope = numerator / denominator

    return float("%.3f" % slope)


expected = []
computed = []
numbers = []

for i in range(1, 102):
    numbers.append(random.uniform(1, 10))

# Here we can use deltax = 0.00001 and deltalx = 0.0000001
for k in range(len(numbers)):
    computed.append(derivative(function, numbers[k], 0.01))
    expected.append((2 * numbers[k]).__round__(3))

plt.plot(computed, expected)

plt.xlabel('Computed')
plt.ylabel('Expected')

plt.title('Error curve deltax = 0.01')

plt.show()


print(computed)
print(expected)
