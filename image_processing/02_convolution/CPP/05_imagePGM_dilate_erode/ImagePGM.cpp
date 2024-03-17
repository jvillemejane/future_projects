
#include <iostream>
#include <string>
#include <vector>
#include <fstream> 
#include "ImagePGM.h"


// Constructor definition
ImagePGM::ImagePGM(void) {
	this->width = 0;
	this->height = 0;
	this->pixels.resize(this->height, std::vector<int>(this->width));
	this->max_gray_value = 255;
	this->magic_number = "P2";
	this->channels = 0;
}

// Constructor definition
ImagePGM::ImagePGM(const std::string& filename) {
    if(readImagePGM(filename)){
		std::cout << "Image opened" << std::endl;
	}
}

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

// Function to rotate an image
void ImagePGM::rotateImagePGM(void) {
	std::cout << "Width = " << this->width << std::endl;
	std::cout << "Pixel[0][W-1] = " << this->pixels[0][this->width-1] << std::endl;
	
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

// Set the size	
void ImagePGM::setSize(int t_width, int t_height){
	this->width = t_width;
	this->height = t_height;
	this->pixels.resize(this->height, std::vector<int>(this->width));	
}

// Set the max gray value		
void ImagePGM::setMaxGray(int t_max_gray_value){
	this->max_gray_value = t_max_gray_value;
}

// Set the max gray value		
void ImagePGM::setPixels(std::vector< std::vector<int> > t_pixels){
	this->setSize( t_pixels[0].size(), t_pixels.size());
	std::copy(t_pixels.begin(), t_pixels.end(), this->pixels.begin());
}

// Convolution
ImagePGM ImagePGM::convImagePGM(Kernel& ker){
	ImagePGM result;
	// Create a new matrix with the same size as image
    std::vector<std::vector<int> > result_pix(this->height, std::vector<int>(this->width));
	int ker_size = ker.getSize();
	
	std::vector<std::vector<double> >  ker_coeffs;
	ker_coeffs = ker.getCoeffs();
	
	// Iterate over each element of the input matrix
    for (int i = 0; i < this->height; ++i) {
        for (int j = 0; j < this->width; ++j) {
            // Apply the kernel to the current element and its neighbors
            for (int k = 0; k < ker_size; ++k) {
                for (int l = 0; l < ker_size; ++l) {
                    int ii = i + k - (ker_size / 2);
                    int jj = j + l - (ker_size / 2);
                    if (ii >= 0 && ii < this->height && jj >= 0 && jj < this->width) {
                        result_pix[i][j] += this->pixels[ii][jj] * ker_coeffs[k][l];
                    }
                }
            }
        }
    }	
	
	result.setPixels(result_pix);
	return result;	
}

// Dilatation
ImagePGM ImagePGM::dilateImagePGM(Kernel& ker){
	ImagePGM result;
	// Create a new matrix with the same size as image
    std::vector<std::vector<int> > result_pix(this->height, std::vector<int>(this->width));
	int ker_size = ker.getSize();
	int max_val = 0;
	
	std::vector<std::vector<double> >  ker_coeffs;
	ker_coeffs = ker.getCoeffs();
	
	// Iterate over each element of the input matrix
    for (int i = 0; i < this->height; ++i) {
        for (int j = 0; j < this->width; ++j) {
			max_val = 0;
            // Apply the kernel to the current element and its neighbors
            for (int k = 0; k < ker_size; ++k) {
                for (int l = 0; l < ker_size; ++l) {
					if(ker_coeffs[k][l] != 0){
						int ii = i + k - (ker_size / 2);
						int jj = j + l - (ker_size / 2);
						if (ii >= 0 && ii < this->height && jj >= 0 && jj < this->width) {
							if(this->pixels[ii][jj] > max_val){
								max_val = this->pixels[ii][jj];
							}
						}
						
					}
				}
            }
			result_pix[i][j] = max_val;
        }
    }	
	
	result.setPixels(result_pix);
	return result;	
}

// Erosion
ImagePGM ImagePGM::erodeImagePGM(Kernel& ker){
	ImagePGM result;
	// Create a new matrix with the same size as image
    std::vector<std::vector<int> > result_pix(this->height, std::vector<int>(this->width));
	int ker_size = ker.getSize();
	int min_val = 0;
	
	std::vector<std::vector<double> >  ker_coeffs;
	ker_coeffs = ker.getCoeffs();
	
	// Iterate over each element of the input matrix
    for (int i = 0; i < this->height; ++i) {
        for (int j = 0; j < this->width; ++j) {
			min_val = 255;
            // Apply the kernel to the current element and its neighbors
            for (int k = 0; k < ker_size; ++k) {
                for (int l = 0; l < ker_size; ++l) {
					if(ker_coeffs[k][l] != 0){
						int ii = i + k - (ker_size / 2);
						int jj = j + l - (ker_size / 2);
						if (ii >= 0 && ii < this->height && jj >= 0 && jj < this->width) {
							if(this->pixels[ii][jj] < min_val){
								min_val = this->pixels[ii][jj];
							}
						}
						
					}
				}
            }
			result_pix[i][j] = min_val;
        }
    }	
	
	result.setPixels(result_pix);
	return result;	
}

// Get the total number of pixels
int ImagePGM::getNbPixels(void){
	return this->width*this->height;
}

// Overloading the << operator to print information about the object
std::ostream& operator<<(std::ostream& os, const ImagePGM& img) {
	os << "Image PGM / Type : " << img.magic_number << ", (W,H) = (" << img.width << "," << img.height << ')' << std::endl;
	return os;
}
