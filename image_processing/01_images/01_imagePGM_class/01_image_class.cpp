#include <iostream>
#include <string>
#include <vector>
#include <fstream> // Include <fstream> for file operations

class ImagePGM {
	public:
		/**
		 * @brief Construct a new ImagePGM object from a filename.
		 * @param filename Name of the file name of the image (constant).
		 */
		ImagePGM(const std::string& filename);
		
		/**
		 * @brief Open an image file.
		 * @param filename Name of the file of the image (constant).
		 * @return true if the file exists.
		 */
		bool readImagePGM(const std::string& filename);
		
		// Declaration of operator<< as a friend function
		friend std::ostream& operator<<(std::ostream& os, const ImagePGM& img);

	private:
		int width;             /**< Width of the image. */
		int height;            /**< Height of the image. */
		int channels;          /**< Number of color value for each pixel of the image. */
		int max_gray_value;    /**< Value of the white color. */
		std::string magic_number;  /**< Type of the file. */

		std::vector< std::vector<int> > pixels; /**< Value of each pixels. */

};

// Function to read a PGM image from a file
bool ImagePGM::readImagePGM(const std::string& filename) {
    std::ifstream file(filename.c_str());

    if (file.is_open()) {
        file >> this->magic_number >> this->width >> this->height >> this->max_gray_value;

        this->pixels.resize(this->height, std::vector<int>(this->width));

        for (int i = 0; i < this->height; ++i) {
            for (int j = 0; j < this->width; ++j) {
                file >> this->pixels[i][j];
            }
        }

        file.close();
    } else {
        std::cerr << "Error: Unable to open file " << filename << std::endl;
        return false;
    }

    return true;
}

// Constructor definition
ImagePGM::ImagePGM(const std::string& filename) {
    readImagePGM(filename);
}

// Overloading the << operator to print information about the object
std::ostream& operator<<(std::ostream& os, const ImagePGM& img) {
	os << "Image PGM / Type : " << img.magic_number << ", (W,H) = (" << img.width << "," << img.height << ')' << std::endl;
	return os;
}


int main(int argc, char** argv) {
    // Read the input PGM image
    ImagePGM image("../../_data/robot.pgm");
	
	std::cout << "Infos" << std::endl;
	std::cout << image << std::endl;

    return 0;
}
