import numpy as np
import matplotlib.pyplot as plt

a=np.array([1,2,3,3,1])
b=np.array([1,2,2,1,1])

plt.plot(a, b, 'b', linewidth=10, marker=".", markersize=5)
plt.axis([0,4,0,4])
plt.xlabel('x os')
plt.ylabel('y os')
plt.title('Primjer')
plt.show()