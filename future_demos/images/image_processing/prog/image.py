import numpy as np
import cv2 as cv
import os

class Image:
    """
    Class to represent an image.

    :param width: Width of the image.
    :type width: int
    :param height: Height of the image.
    :type height: int
    :param channels: Number of color values for each pixel of the image.
    :type channels: int
    :param type: Type of image (PNG, JPG, PGM...).
    :type type: str
    :param pixels: Value of each pixel.
    :type pixels: numpy.ndarray
    
    """
    
    def __init__(self) -> None:
        """
        Initialize the Image object.
        
        """
        self.width = 0              # Width of the image
        self.height = 0             # Height of the image
        self.channels = 0           # Number of color values for each pixel
        self.type = None            # Type of image (PNG, JPG, PGM...)
        self.pixels = np.array([])  # Value of each pixel
        
    def open(self, filename: str = '') -> bool:
        """
        Open an image file.

        :param filename: Name of the file.
        :type filename: str
        
        :return: True if the file was successfully read, False otherwise.
        :rtype: bool

        """
        self.pixels = cv.imread(filename);
        if self.pixels is None:
            return False
        temp_str = os.path.splitext(filename)[1]        
        self.type = temp_str[1:].upper()        
        self.height = self.pixels.shape[0];	
        self.width = self.pixels.shape[1];
        if len(self.pixels.shape) > 2:
            self.channels = self.pixels.shape[2]
        else:
            self.channels = 1
        return True
        
    def write(self, filename: str) -> bool:
        """
        Open an image file.

        :param filename: Name/Path of the file to write.
        :type filename: str
        
        :return: True if the file was successfully written, False otherwise.
        :rtype: bool

        """
        if self.width == 0 or self.height == 0:
            return False
        success = cv.imwrite(filename, self.pixels)
        return success
    
    def create(self, pixels: np.ndarray) -> None:
        """
        Create an image from an array.
        
        :param pixels: Array of pixels.
        :type pixels: np.ndarray
        
        """
        self.pixels = pixels        
        self.height = self.pixels.shape[0];	
        self.width = self.pixels.shape[1];
        if len(self.pixels.shape) > 2:
            self.channels = self.pixels.shape[2]
        else:
            self.channels = 1
        
    
    def display(self, width:int = 0, height:int = 0) -> None:
        """
        Display an image in a window.

        :param width: Width of the window. Default 0, width of the image.
        :type width: int
        :param height: Height of the window. Default 0, height of the image.
        :type height: int

        """  
        print("Press a key to close the window")
        if width == 0 and height == 0:
            cv.imshow("Image", self.pixels)
        else:
            resized_img = cv.resize(self.pixels, (width, height), interpolation=cv.INTER_LINEAR)
            cv.imshow("Image", resized_img)
        # Wait for a key press and close the window
        cv.waitKey(0)
        cv.destroyAllWindows()
    
    def getPixels(self) -> np.ndarray:
        """
        Return the array of pixels.
        
        :return: Return the array or pixels.
        :rtype: np.ndarray
        
        """
        return self.pixels

    def getSize(self) -> tuple[int, int]:
        """
        Return the size of the image.
        
        :return: Return the size of the image. Height, width.
        :rtype: tuple[int, int]
        
        """
        return self.height, self.width

    def getChannels(self) -> int:
        """
        Return the number of color channels of the image.
        
        :return: Return the number of color channels of the image.
        :rtype: int
        
        """
        return self.channels
        
    def changeContrast(self, contrast:float) -> None:
        """
        Change the contrast of the image.

        :param contrast: Contrast, between 0 to 10.
        :type contrast: float

        """
        if contrast < 0:
            contrast = 1.0
        self.pixels = cv.convertScaleAbs(self.pixels, alpha=contrast)

    def changeBrightness(self, brightness:int) -> None:
        """
        Change the brightness of the image.

        :param brightness: Brightness in percent, between -100 to 100.
        :type brightness: int

        """
        if brightness > 100:
            brightness = 100
        elif brightness < -100:
            brightness = -100
        brightness = brightness * 127 / 100
        self.pixels = cv.convertScaleAbs(self.pixels, beta=brightness)

    
    def resize_image_ratio(self, new_height: int, new_width: int) -> None:
        """
        Create a new image at a different size, with the same aspect ratio.

        :param new_height: New height of the image.
        :type new_height: int
        :param new_width: New width of the image.
        :type new_width: int
        
        :return: A resized image.
        :rtype: Image       

        """
        aspect_ratio = self.width / self.height
        
        # Calculate new size with same aspect_ratio
        n_width = new_width
        n_height = int(n_width / aspect_ratio)
        if n_height > new_height:
            n_height = new_height
            n_width = int(n_height * aspect_ratio)
        else:
            n_width = new_width
            n_height = int(n_width / aspect_ratio)
        
        resized_array = cv.resize(self.pixels, (n_width, n_height))
        # Generate a new image
        resized_image = Image()
        resized_image.create(resized_array)
        return resized_image

    def __str__(self) -> str:
        """
        Return a string representation of the ImagePGM object.

        :return: A string with PGM image informations
        :rtype: str
        """
        return f"Image / Type: {self.type} / (W,H) = ({self.width}, {self.height}) / C = {self.channels}"
        

# Main function
if __name__ == "__main__":
    image = Image()
    image.open("../_data/robot.jpg")
    print(image)
    image.write("robot2.png")
    image.display()
    # image.display(100, 60)
    
    image.changeContrast(0.7)
    image.display()
    
    image.changeBrightness(-20)
    image.display()