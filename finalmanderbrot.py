import numpy as np
import matplotlib.pyplot as plt

xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0
width, height = 500, 500

x = np.linspace (xmin, xmax, width)
y = np.linspace (ymin, ymax, height)
result = np.zeros ((width, height))

def mandelbrot(c, max_iter):
	z = 0
	for i in range(max_iter):
		z = z*z + c
		if abs(z) > 2:
			return i
	return max_iter
	
max_iter = 100
	
for i in range(width):
	for j in range(height):
		c = complex(x[i], y[j])
		result[i, j] = mandelbrot(c, max_iter)
				
plt.imshow(result.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.xlabel('Re')
plt.ylabel('Im')
plt.title('Mandelbrot Set')
plt.show()