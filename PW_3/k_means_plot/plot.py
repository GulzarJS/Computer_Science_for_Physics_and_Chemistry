import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset= pd.read_csv("cluster.data_4")

plt.scatter(dataset[:,0],dataset[:,1],dataset[:,2],dataset[:,3], c=dataset, cmap='rainbow')

