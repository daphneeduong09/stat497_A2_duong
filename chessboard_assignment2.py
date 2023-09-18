
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.colors import LogNorm 

#we first generate row and column spacing
row = np.arange(-5.0, 5.0, 0.001) 
col = np.arange(-5.0, 5.0, 0.05) 

#now we construct the board using numpy (matrices)
X, Y = np.meshgrid(row,col)  
res = np.add.outer(range(8), range(8))%2 

#using matplotlib to display our vector as an image
plt.imshow(res, cmap="binary_r")
plt.xticks([])
plt.yticks([])
plt.show()


