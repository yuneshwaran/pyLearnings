import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('image.jpg')

if img.ndim == 3:
    img = img.mean(axis=2) 

top  = img[:-2 , 1:-1]
bottom = img[2: , 1:-1]
left = img[1:-1 , :-2]
right = img[1:-1, 2:]
center = img[1:-1 , 1:-1]

blurred = (top+bottom+right+left+center)/5

plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.figure()
plt.imshow(blurred, cmap='gray')
plt.title('Blurred')
plt.axis('off')
plt.show()