import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('image.jpg')

if img.ndim == 3:
    img = img.mean(axis=2) 

def blur(img):
    top  = img[:-2 , 1:-1]
    bottom = img[2: , 1:-1]
    left = img[1:-1 , :-2]
    right = img[1:-1, 2:]
    center = img[1:-1 , 1:-1]

    blurred = (top+bottom+right+left+center)/5

    return blurred

res = 0
i = 1
while i<50:
    if i<=1:
        res = blur(img)
        i+=1
    else:
        res = blur(res)
        i+=1

plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.figure()
plt.imshow(res, cmap='gray')
plt.title('Blurred')
plt.axis('off')
plt.show()