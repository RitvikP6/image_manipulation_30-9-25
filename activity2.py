import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Coding.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rotate the image by 45 degrees
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))

rotated_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image by 45 degrees")
plt.show()

#Increase brightness
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brightened_image = cv2.add(image, brightness_matrix)
brightened_rgb = cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB)
plt.imshow(brightened_rgb)
plt.title("Brightened Image")
plt.show()
