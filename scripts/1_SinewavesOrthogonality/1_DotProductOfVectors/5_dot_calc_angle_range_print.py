from lib import rotate_vector
import numpy as np
green_vector = [0, 1]
blue_vector = [0, 1]
dot_product = np.dot(green_vector, blue_vector)
for i in range(0, 370, 10):
    blue_vector = rotate_vector(green_vector, i)
    dot_product = np.dot(green_vector, blue_vector)
    print(f'{i:03d}: {dot_product:+0.3f}')
