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
        with open(filename, 'rb') as f:
            # Read the magic number (P2 or P5)
            self.magic_number = f.readline().decode().strip()
            
            # Read the comment lines (if any)
            while True:
                line = f.readline().decode().strip()
                if not line.startswith('#'):
                    break
            
            # Read the width and height
            self.width, self.height = map(int, line.split())
            
            # Read the max gray value
            self.max_gray_value = int(f.readline().decode().strip())
            
            # Read the pixel data
            if self.magic_number == 'P2':
                # ASCII mode
                self.pixels = [list(map(int, line.split())) for line in f.readlines()]
            elif self.magic_number == 'P5':
                # Binary mode
                self.pixels = []
                for _ in range(height):
                    row = []
                    for _ in range(width):
                        row.append(ord(f.read(1)))
                    self.pixels.append(row)
            else:
                raise ValueError("Invalid magic number. Supported types: P2 (ASCII) and P5 (binary)")
                return False
            return True

    def writeImagePGM(self, filename):
        """
        Write a PGM image to a file.

        :param filename: Name of the PGM file to write.
        :type filename: str
        
        :return: True if the file was successfully read, False otherwise.
        :rtype: bool
        
        """
        with open(filename, 'w') as f:
            # Write the magic number
            f.write('P2\n')
            
            # Write the width and height
            f.write(f"{self.width} {self.height}\n")
            
            # Write the max gray value
            f.write(f"{self.max_gray_value}\n")
            
            # Write the pixel data
            for row in self.pixels:
                f.write(' '.join(map(str, row)) + '\n')
        
        
    def __str__(self):
        """
        Return a string representation of the ImagePGM object.

        :return: A string with PGM image informations
        :rtype: str
        """
        return f"Image PGM / Type: {self.magic_number}, (W,H) = ({self.width}, {self.height})"
