
import cv2
import numpy as np
from matplotlib import pyplot as plt

def unsharp_masking(image_path, sigma=1.5, strength=1.5):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(grayscale_image, (0, 0), sigma)

    # Create a sharpening kernel
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])

    # Apply the sharpening kernel
    sharpened_image = cv2.filter2D(blurred_image, -1, kernel)

    # Enhance the edges with the unsharp mask
    sharpened_image = grayscale_image + strength * (grayscale_image - sharpened_image)

    # Clip values to the valid range [0, 255]
    sharpened_image = np.clip(sharpened_image, 0, 255)

    # Display the original, blurred, and sharpened images
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title('Blurred Image')

    plt.subplot(1, 3, 3)
    plt.imshow(sharpened_image, cmap='gray')
    plt.title('Sharpened Image')
    plt.show()
    return sharpened_image
image_path = "food.jpg"
sharpened_image = unsharp_masking(image_path, sigma=1.5, strength=1.5)
