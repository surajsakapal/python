
import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply histogram equalization
    equalized_img = cv2.equalizeHist(img)

    # Display the original and equalized images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_img, cmap='gray')
    plt.title('Equalized Image')

    plt.show()

    # Save the equalized image if needed
    cv2.imwrite('equalized_image.jpg', equalized_img)

# Replace 'path/to/your/image.jpg' with the actual path to your image file
image_path = "food.jpg"
histogram_equalization(image_path)
