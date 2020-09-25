import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('summary')
plt.plot(data[:,0],data[:,1],'-x')
plt.xlabel('k-points')
plt.ylabel('Total Energy')
plt.savefig('kpoints.png')
plt.show()

