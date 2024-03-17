
#include <iostream>
#include <string>
#include <vector>
#include <fstream> 
#include "ImagePGM.h"

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

// Function to write a PGM image to a file
bool ImagePGM::writeImagePGM(const std::string& filename) {
    std::ofstream file(filename.c_str());

    if (file.is_open()) {
        file << this->magic_number << std::endl;
        file << this->width << " " << this->height << std::endl;
        file << this->max_gray_value << std::endl;

        for (int i = 0; i < this->height; ++i) {
            for (int j = 0; j < this->width; ++j) {
                file << this->pixels[i][j] << " ";
            }
            file << std::endl;
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
    if(readImagePGM(filename)){
		std::cout << "Image opened" << std::endl;
	}
}


// Overloading the << operator to print information about the object
std::ostream& operator<<(std::ostream& os, const ImagePGM& img) {
	os << "Image PGM / Type : " << img.magic_number << ", (W,H) = (" << img.width << "," << img.height << ')' << std::endl;
	return os;
}
