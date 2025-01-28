
import cv2
import numpy as np
import matplotlib.pyplot as plt

def halftone(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Convert image to binary using dithering
    _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Display the original and halftone images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(binary_img, cmap='gray')
    plt.title('Halftone Image')

    plt.show()

    # Save the halftone image if needed
    cv2.imwrite('halftone_image.jpg', binary_img)

# Replace 'path/to/your/image.jpg' with the actual path to your image file
image_path = "food.jpg"
halftone(image_path)
