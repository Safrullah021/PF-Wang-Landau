import matplotlib.pyplot as plt
import numpy as np
import math

# Menghitung Fungsi Partisi Z(T)
kb = 1
data = np.loadtxt('dos-reversed.txt')
E = -data[:,0]
u = data[:,1]
T = Z = np.linspace(1,5,10)
Ztot = 0

# Menghitung Z untuk semua nilai T yang diambil
for j in range(len(T)):
    print("T= ",T[j])
    # Menghitung Z untuk satu nilai T tertentu
    for i in range(len(E)):
        Zsem = u[i]*(math.exp(-E[i]/(kb*T[j])))
        Ztot = Ztot+Zsem
        print("Zsem= ",Zsem)
    Z[j] = Ztot
    print("Z= ", Ztot)
    Ztot = 0
print("Z=", Z)