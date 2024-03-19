import numpy as np
import cv2 as cv
import os
from image import Image

# Square-shaped kernel - size 3
square3 = np.array((
	[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1]), dtype=np.uint8)
# Square-shaped kernel - size 5
square5 = np.array((
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]), dtype=np.uint8)
# Cross-shaped kernel - size 3
cross3 = np.array((
	[0, 1, 0],
	[1, 1, 1],
	[0, 1, 0]), dtype=np.uint8)
# Cross-shaped kernel - size 5
cross5 = np.array((
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[1, 1, 1, 1, 1],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0]), dtype=np.uint8)
# Laplacian kernel used to detect edge-like regions of an image
laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")
# construct the Sobel x-axis kernel
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")
# construct the Sobel y-axis kernel
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")


kernels = {
	"laplacian": laplacian,
    "sobel_x": sobelX,
	"sobel_y": sobelY,
    "square3": square3,
    "square5": square5,
    "cross3": cross3,
    "cross5": cross5
}

class ImageProcess:
    """
    Class to represent a process for image.

    :param image: Image to process.
    :type image: Image
    
    """
    
    def __init__(self, image: Image) -> None:
        """
        Initialize the Image object.
        
        :param image: Image to process.
        :type image: Image
        
        """
        self.image = image      # Image to process

    def binarize(self, treshold:int) -> Image:
        """
        Binarize an image.
        
        :param treshold: Treshold for binarization of the image.
        :type treshold: int        
        
        """
        image = Image()
        im_gray = cv.cvtColor(self.image.getPixels(), cv.COLOR_BGR2GRAY)
        ret, temp_array = cv.threshold(im_gray, treshold, 255, cv.THRESH_BINARY)
        image.create(temp_array)
        return image
    
        

    def blur(self, size:int) -> Image:
        """
        Blur an image. Process a mean filter on the image.
        
        :param size: Size of the kernel to process the filter.
        :type size: int
        
        """
        image = Image()
        temp_array = cv.blur(self.image.getPixels(), (size, size));
        image.create(temp_array)
        return image
    
    def blur(self, size:int) -> Image:
        """
        Blur an image. Process a mean filter on the image.
        
        :param size: Size of the kernel to process the filter.
        :type size: int
        
        """
        image = Image()
        temp_array = cv.blur(self.image.getPixels(), (size, size));
        image.create(temp_array)
        return image
        
    def convolve(self, kernel: np.ndarray) -> Image:
        """
        Process a convolution on an image with a specific kernel.
        
        :param kernel: Kernel for process convolution.
        :type kernel: np.ndarray
        
        """
        image = Image()
        im_gray = cv.cvtColor(self.image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.filter2D(src=im_gray, ddepth=-1, kernel=kernel)
        image.create(temp_array)
        return image

    def erode(self, kernel: np.ndarray) -> Image:
        """
        Process an erosion on an image with a specific kernel.
        
        :param kernel: Kernel for process erosion.
        :type kernel: np.ndarray
        
        """        
        image = Image()
        im_gray = cv.cvtColor(self.image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.erode(im_gray, kernel, cv.BORDER_REFLECT)
        image.create(temp_array)
        return image

    def dilate(self, kernel: np.ndarray) -> Image:
        """
        Process a dilatation on an image with a specific kernel.
        
        :param kernel: Kernel for process dilatation.
        :type kernel: np.ndarray
        
        """        
        image = Image()
        im_gray = cv.cvtColor(self.image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.dilate(im_gray, kernel, cv.BORDER_REFLECT)
        image.create(temp_array)
        return image
        
    def opening(self, kernel: np.ndarray) -> Image:
        """
        Process an opening on an image with a specific kernel.
        
        :param kernel: Kernel for process dilatation.
        :type kernel: np.ndarray
        
        """        
        image = Image()
        im_gray = cv.cvtColor(self.image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.morphologyEx(im_gray, cv.MORPH_OPEN, kernel, cv.BORDER_REFLECT)
        image.create(temp_array)
        return image    

    def closing(self, kernel: np.ndarray) -> Image:
        """
        Process an opening on an image with a specific kernel.
        
        :param kernel: Kernel for process dilatation.
        :type kernel: np.ndarray
        
        """        
        image = Image()
        im_gray = cv.cvtColor(self.image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.morphologyEx(im_gray, cv.MORPH_CLOSE, kernel, cv.BORDER_REFLECT)
        image.create(temp_array)
        return image    

# Main function
if __name__ == "__main__":
    image = Image()
    image.open("../_data/robot.jpg")
    print(image)
    image.display()
    
    '''
    print('Binarize 100')
    image_binarize = Image()
    binarize_proc = ImageProcess(image)
    image_binarize = binarize_proc.binarize(100)
    image_binarize.display()
    
    print('Blur 5')
    image_blur = Image()
    blur_proc = ImageProcess(image)
    image_blur = blur_proc.blur(5)
    image_blur.display()
    
    print('Convolution with a Kernel')
    image_conv = Image()
    conv_proc = ImageProcess(image)
    image_conv = conv_proc.convolve(kernels['laplacian'])
    image_conv.display()
    '''
    
    print('Erosion with a Kernel')
    image_erode = Image()
    erode_proc = ImageProcess(image)
    image_erode = erode_proc.erode(kernels['cross5'])
    image_erode.display()   
    
    print('Dilatation with a Kernel')
    image_dilate = Image()
    dilate_proc = ImageProcess(image)
    image_dilate = dilate_proc.dilate(kernels['cross5'])
    image_dilate.display()  

    print('Opening with a Kernel')
    image_opening = Image()
    opening_proc = ImageProcess(image)
    image_opening = opening_proc.opening(kernels['square5'])
    image_opening.display()   

    print('Closing with a Kernel')
    image_closing = Image()
    closing_proc = ImageProcess(image)
    image_closing = closing_proc.closing(kernels['square5'])
    image_closing.display()  