import pickle
import LogisiticRegression as LR
import time
import matplotlib.pyplot as plt
import numpy as np
nx= np.empty([1], dtype=float)

ms = pickle.load(open("trainingms1000lambda0ns1.dat","rb"))
a=[]
for item in ms.weightVector:
    a.append(item)
    print(item)
np.append(nx, a)
plt.plot(nx)
