
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

// Function to rotate an image
void ImagePGM::rotateImagePGM(void) {
	std::cout << "Width = " << this->width << std::endl;
	std::cout << "Pixel[0][W-1] = " << this->pixels[0][this->width-1] << std::endl;
	
	//this->pixels.resize(this->height, std::vector<int>(this->width));
    // Create a transposed matrix with swapped dimensions
    std::vector<std::vector<int> > transposed(this->width, std::vector<int>(this->height));
		
    // Fill in the transposed matrix
    for (int i = 0; i < this->height; ++i) {
        for (int j = 0; j < this->pixels[i].size(); j++) {
            transposed[j][i] = this->pixels[i][j];
        }
    }
	this->pixels.resize(this->width, std::vector<int>(this->height));
	std::copy(transposed.begin(), transposed.end(), this->pixels.begin());
	std::swap(this->width, this->height);
    transposed.clear();
	
    // Reverse each row of the transposed matrix
    for (int i = 0; i < this->pixels.size(); ++i) {
        int left = 0, right = this->pixels[i].size() - 1;
        while (left < right) {
            std::swap(this->pixels[i][left], this->pixels[i][right]);
            ++left;
            --right;
        }
    }
	
	std::cout << "Rotate OK" << std::endl;
}


// Overloading the << operator to print information about the object
std::ostream& operator<<(std::ostream& os, const ImagePGM& img) {
	os << "Image PGM / Type : " << img.magic_number << ", (W,H) = (" << img.width << "," << img.height << ')' << std::endl;
	return os;
}
