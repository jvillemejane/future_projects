import cv2
import numpy as np

# Load the input image
image = cv2.imread('robot.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (3, 3), 0)

# Compute gradients in the x and y directions using Sobel operator
gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)

# Compute magnitude of gradient (edge strength)
edge_strength = np.sqrt(gradient_x**2 + gradient_y**2)

# Normalize edge strength to 0-255 range
edge_strength_normalized = cv2.normalize(edge_strength, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Threshold edge strength to obtain binary edge map
threshold = 50
edges_binary = cv2.threshold(edge_strength_normalized, threshold, 255, cv2.THRESH_BINARY)[1]

# Display the input image and the detected edges
cv2.imshow('Input Image', image)
cv2.imshow('Detected Edges', edges_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
