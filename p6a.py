
import cv2 
import numpy as np 
  
# Reading the image 
image = cv2.imread('food.jpg') 
  
# Applying the filter
 
medianblur = cv2.medianBlur(image, 5) 
  
# Showing the image 
cv2.imshow('Original', image) 
cv2.imshow('Median blur', medianblur) 
  
cv2.waitKey() 
cv2.destroyAllWindows() 
