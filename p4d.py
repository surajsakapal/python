
import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_threshold(image_path, threshold_value):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply thresholding
    _, thresholded_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the original and thresholded images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(thresholded_img, cmap='gray')
    plt.title('Thresholded Image')

    plt.show()

    # Save the thresholded image if needed
    cv2.imwrite('thresholded_image.jpg', thresholded_img)

# Replace 'path/to/your/image.jpg' with the actual path to your image file
image_path = "food.jpg"
threshold_value = 127  # Adjust this value as needed
apply_threshold(image_path, threshold_value)
