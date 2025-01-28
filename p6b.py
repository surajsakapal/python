
import cv2 
import numpy as np 
  
# Reading the image 
image = cv2.imread('food.jpg') 
  
# Applying the filter 
gaussian = cv2.GaussianBlur(image, (3, 3), 0) 
  
# Showing the image 
cv2.imshow('Original', image) 
cv2.imshow('Gaussian blur', gaussian) 
  
cv2.waitKey() 
cv2.destroyAllWindows() 
