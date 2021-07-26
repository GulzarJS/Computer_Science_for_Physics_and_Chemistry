import numpy as np
from numpy import random
from scipy import stats
import matplotlib.pyplot as plt

N_Points = 1000

x = stats.norm.rvs(loc=1, scale=2, size=N_Points)
y = stats.uniform.rvs(loc=-1, scale=2, size=N_Points)
z = stats.expon.rvs(loc=4, size=N_Points)

sum = 0
for i in x :
    sum = sum + i

exp_x = sum / 1000

sum = 0
for i in y :
    sum = sum + i

exp_y = sum / 1000

sum = 0
for i in z :
    sum = sum + i

exp_z = sum / 1000
print(exp_x)
print(exp_y)
print(exp_z)

print(f"x: maen = {x.mean():.3f}, std = {x.std():.3f}")
print(f"y: maen = {y.mean():.3f}, std = {y.std():.3f}")
print(f"z: maen = {z.mean():.3f}, std = {z.std():.3f}")

_ , px =stats.shapiro(x)
_ , py =stats.shapiro(y)
_ , pz =stats.shapiro(z)


print("Shapiro-Wilk test resutl ")
print(f"x: {px: .2f}, y: {py: .2f}, z: {pz: .2f}")

fig, axs = plt.subplots(1,3,figsize=(3*5,5))
axs[0].hist(x,bins=50)
axs[1].hist(y,bins=50)
axs[2].hist(z,bins=50)

plt.show()
