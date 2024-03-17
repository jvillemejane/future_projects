"""01_image_class file.

File containing :class::ImagePGM
Class to represent a PGM image.


.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

class ImagePGM:
    """
    Class to represent a PGM image.

    :param width: Width of the image.
    :type width: int
    :param height: Height of the image.
    :type height: int
    :param channels: Number of color values for each pixel of the image.
    :type channels: int
    :param max_gray_value: Value of the white color.
    :type max_gray_value: int
    :param magic_number: Type of the file.
    :type magic_number: str
    :param pixels: Value of each pixel.
    :type pixels: list
    """
    
    def __init__(self, filename):
        """
        Initialize the ImagePGM object.

        Parameters:
            filename (str): Name of the PGM file.
        """
        self.width = 0          # Width of the image
        self.height = 0         # Height of the image
        self.channels = 0       # Number of color values for each pixel of the image
        self.max_gray_value = 0 # Value of the white color
        self.magic_number = ""  # Type of the file
        self.pixels = []        # Value of each pixel
        self.readImagePGM(filename)
    
    def readImagePGM(self, filename):
        """
        Read a PGM image from a file and store its information.

        :param filename: Name of the PGM file.
        :type filename: str
        
        :return: True if the file was successfully read, False otherwise.
        :rtype: bool

        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.magic_number = lines[0].strip()
                self.width, self.height = map(int, lines[1].split())
                self.max_gray_value = int(lines[2])
                self.pixels = [[int(value) for value in line.split()] for line in lines[3:]]
        except FileNotFoundError:
            print(f"Error: Unable to open file {filename}")
            return False
        return True

    def __str__(self):
        """
        Return a string representation of the ImagePGM object.

        :return: A string with PGM image informations
        :rtype: str
        """
        return f"Image PGM / Type: {self.magic_number}, (W,H) = ({self.width}, {self.height})"


# Main function
if __name__ == "__main__":
    # Read the input PGM image
    image = ImagePGM("../../_data/robot.pgm")

    print("Infos")
    print(image)
