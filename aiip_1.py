import numpy as np
from matplotlib import pyplot as plt


# PART 1: IMAGES CREATION
# Exercice 1: binary images
dimension = 100
triangle = np.zeros((dimension, dimension), dtype=np.uint8)
for i in range(dimension):
    triangle[i, 0:i] = 1
plt.figure("1.1: triangle")
plt.imshow(triangle, cmap="gray")

# Exercice 2: more triangles
tritop = np.zeros((dimension, dimension), dtype=np.uint8)
for i in range(dimension):
    tritop[i, i+1:dimension-i-1] = 1
plt.figure("1.2.a: tritop")
plt.imshow(tritop, cmap="gray")

tribot = np.zeros((dimension, dimension), dtype=np.uint8)
for i in range(dimension):
    tribot[i, dimension-i:i] = 1
plt.figure("1.2.b: tribot")
plt.imshow(tribot, cmap="gray")

# Exercice 3: grid
grid = np.zeros((dimension, dimension))
grid[0:dimension:2, 0:dimension:2] = 1
grid[1:dimension:2, 1:dimension:2] = 1
plt.figure("1.3: grid")
plt.imshow(grid, cmap="gray")

# Exercice 4: gradient
dimension_y = 10
dimension_x = 8
gradient = np.zeros((dimension_y, dimension_x))
for i in range(dimension_y):
    gradient[i] = i
gradient /= gradient.max()
plt.figure("1.4: gradient")
plt.imshow(gradient, cmap="gray")

# DISPLAY ONLY IF CALLED DIRECTLY OR IF DEBUG MODE ON
if __name__ == "__main__" or DEBUG:
    plt.show()
