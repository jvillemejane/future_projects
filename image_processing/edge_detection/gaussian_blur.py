import cv2

# Load the input image
image = cv2.imread('robot.jpg')

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # Kernel size (5x5) can be adjusted as needed

# Display the input image and the blurred image
cv2.imshow('Input Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
