import matplotlib.pyplot as plt
import numpy as np
import math

kb = 1
E = np.array([-8,-7,-6,-5,-4,-3,-2,-1,0], dtype='f')
u = np.array([4.8339106025e-08,1.2867577564e-05,1.6934162970e-04,1.4184372355e-03,8.9941168113e-03,3.8388776611e-02,1.2563952456e-01,3.3120684961e-01,4.9417003763e-01], dtype='f')
T = Z = np.linspace(1,5,10)
Ztot = 0

for j in range(len(T)):
    print("T= ",T[j])
    for i in range(len(E)):
        Zsem = u[i]*(math.exp(-E[i]/(kb*T[j])))
        Ztot = Ztot+Zsem
        print("Zsem= ",Zsem)
    Z[j] = Ztot
    print("Z= ", Ztot)
    Ztot = 0
print("Z=", Z)





