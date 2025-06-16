import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

data=np.loadtxt('data.csv',delimiter=',',dtype='str')
data=data[1::]
data=np.array(data,np.float32)
print(data.shape)
plt.scatter(data[:,1] , data[:,2])
plt.show()
data50=data[0::50]
plt.scatter(data50[:,1] , data50[:,2])
plt.show()
print(np.min(data[:,1]),np.max(data[:,1]),np.mean(data[:,1]))
print(np.min(data[:,2]),np.max(data[:,2]),np.mean(data[:,2]))


indMen = (data[:,0] == 1)
indWomen = (data[:,0] == 0)



men=data[indMen]
print(np.min(men[:,1]),np.max(men[:,1]),np.mean(men[:,1]))
print(np.min(men[:,2]),np.max(men[:,2]),np.mean(men[:,2]))

women=data[indWomen]
print(np.min(women[:,1]),np.max(women[:,1]),np.mean(women[:,1]))
print(np.min(women[:,2]),np.max(women[:,2]),np.mean(women[:,2]))