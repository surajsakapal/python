
import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_gradient_laplacian(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply the Sobel operator to calculate gradients
    gradient_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate magnitude and direction of the gradients
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_direction = np.arctan2(gradient_y, gradient_x)

    # Apply Laplacian operator
    laplacian = cv2.Laplacian(img, cv2.CV_64F)

    # Display the original, gradient, and Laplacian images
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(gradient_magnitude, cmap='viridis')
    plt.title('Gradient Magnitude')

    plt.subplot(1, 3, 3)
    plt.imshow(laplacian, cmap='coolwarm')
    plt.title('Laplacian Image')
    plt.show()

    # Save the gradient magnitude and Laplacian images if needed
    cv2.imwrite('gradient_magnitude.jpg', gradient_magnitude)
    cv2.imwrite('laplacian_image.jpg', laplacian)

image_path = "food.jpg"
apply_gradient_laplacian(image_path)
