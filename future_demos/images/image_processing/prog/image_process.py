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

    @classmethod
    def binarize(self, image:Image, params_dict:dict) -> Image:
        """
        Binarize an image.
        
        :param image: Image to process.
        :type image: Image
        :param params_dict: Dictionary of parameters. 'threshold' entry is required.
        :type params_dict: dict
        
        :return: New image.
        :rtype: Image
        
        """
        threshold = params_dict["threshold"]
        result = Image()
        im_gray = cv.cvtColor(image.getPixels(), cv.COLOR_BGR2GRAY)
        ret, temp_array = cv.threshold(im_gray, threshold, 255, cv.THRESH_BINARY)
        result.create(temp_array)
        return result
    
    @classmethod
    def blur(self, image:Image, params_dict:dict) -> Image:
        """
        Blur an image. Process a mean filter on the image.
        
        :param image: Image to process.
        :type image: Image
        :param params_dict: Dictionary of parameters. 'size' entry is required.
        :type params_dict: dict
        
        :return: New image.
        :rtype: Image
        
        """
        size = params_dict['size']
        result = Image()
        temp_array = cv.blur(image.getPixels(), (size, size));
        result.create(temp_array)
        return result
      
    @classmethod  
    def convolve(self, image:Image, params_dict:dict) -> Image:
        """
        Process a convolution on an image with a specific kernel.
        
        :param image: Image to process.
        :type image: Image
        :param params_dict: Dictionary of parameters. 'kernel' entry is required.
        :type params_dict: dict
        
        :return: New image.
        :rtype: Image
        
        """
        result = Image()
        kernel = params_dict['kernel']
        im_gray = cv.cvtColor(image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.filter2D(src=im_gray, ddepth=-1, kernel=kernel)
        result.create(temp_array)
        return result

    @classmethod 
    def erode(self, image:Image, params_dict:dict) -> Image:
        """
        Process an erosion on an image with a specific kernel.
        
        :param image: Image to process.
        :type image: Image
        :param params_dict: Dictionary of parameters. 'kernel' entry is required.
        :type params_dict: dict
        
        :return: New image.
        :rtype: Image
        
        """        
        result = Image()
        kernel = params_dict['kernel']
        im_gray = cv.cvtColor(image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.erode(im_gray, kernel, cv.BORDER_REFLECT)
        result.create(temp_array)
        return result

    @classmethod 
    def dilate(self, image:Image, params_dict:dict) -> Image:
        """
        Process a dilatation on an image with a specific kernel.
        
        :param image: Image to process.
        :type image: Image
        :param params_dict: Dictionary of parameters. 'kernel' entry is required.
        :type params_dict: dict
        
        :return: New image.
        :rtype: Image
        
        """        
        result = Image()
        kernel = params_dict['kernel']
        im_gray = cv.cvtColor(image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.dilate(im_gray, kernel, cv.BORDER_REFLECT)
        result.create(temp_array)
        return result
       
    @classmethod  
    def opening(self, image:Image, params_dict:dict) -> Image:
        """
        Process an opening on an image with a specific kernel.
        
        :param image: Image to process.
        :type image: Image
        :param params_dict: Dictionary of parameters. 'kernel' entry is required.
        :type params_dict: dict

        :return: New image.
        :rtype: Image
        
        """        
        result = Image()
        kernel = params_dict['kernel']
        im_gray = cv.cvtColor(image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.morphologyEx(im_gray, cv.MORPH_OPEN, kernel, cv.BORDER_REFLECT)
        result.create(temp_array)
        return result    

    @classmethod 
    def closing(self, image:Image, params_dict:dict) -> Image:
        """
        Process an opening on an image with a specific kernel.
        
        :param image: Image to process.
        :type image: Image
        :param params_dict: Dictionary of parameters. 'kernel' entry is required.
        :type params_dict: dict
                
        :return: New image.
        :rtype: Image
        
        """        
        result = Image()
        kernel = params_dict['kernel']
        im_gray = cv.cvtColor(image.getPixels(), cv.COLOR_BGR2GRAY)
        temp_array = cv.morphologyEx(im_gray, cv.MORPH_CLOSE, kernel, cv.BORDER_REFLECT)
        result.create(temp_array)
        return result    

# Main function
if __name__ == "__main__":
    image = Image()
    image.open("../_data/robot.jpg")
    print(image)
    image.display()
    
    params = {}
    
    print('Binarize 100')
    image_binarize = Image()
    params['threshold'] = 100
    image_binarize = ImageProcess.binarize(image, params)
    image_binarize.display()
    
    '''
    print('Blur 5')
    image_blur = Image()
    image_blur = ImageProcess.blur(image, 5)
    image_blur.display()
    
    print('Convolution with a Kernel')
    image_conv = Image()
    image_conv = ImageProcess.convolve(image, kernels['laplacian'])
    image_conv.display()
    '''
    
    print('Erosion with a Kernel')
    image_erode = Image()
    params['kernel'] = kernels['cross5']
    image_erode = ImageProcess.erode(image, params)
    image_erode.display()   
    
    print('Dilatation with a Kernel')
    image_dilate = Image()
    params['kernel'] = kernels['cross5']
    image_dilate = ImageProcess.dilate(image, params)
    image_dilate.display()  
    
    '''
    print('Opening with a Kernel')
    image_opening = Image()
    image_opening = ImageProcess.opening(image, kernels['square5'])
    image_opening.display()   

    print('Closing with a Kernel')
    image_closing = Image()
    image_closing = ImageProcess.closing(image, kernels['square5'])
    image_closing.display() 
    '''
    