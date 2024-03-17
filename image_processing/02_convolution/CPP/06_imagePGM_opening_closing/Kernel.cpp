
#include <iostream>
#include <string>
#include <vector>
#include <fstream> 
#include <sstream>
#include "Kernel.h"


Kernel::Kernel(int t_size, const std::string& t_matrix, double t_gain){
	this->size = t_size;
	this->gain = t_gain;
	if(this->size % 2 == 0){
		std::cerr << "The size of the kernel must be an odd number !" << std::endl;
		return;
	}
	else{
		this->coeffs.resize(this->size, std::vector<double>(this->size));
		this->setMatrix(t_matrix);
	}
	std::cout << "G = " << this->gain << std::endl;
}

// Create a 2D vector from a Matrix string
// 		matrix = "1, 2, 3; 3, 1, 5; 5, 6, 7; 5, 9, 0" is a 4 rows and 3 cols matrix
void Kernel::setMatrix(const std::string& t_matrix) {
	std::vector< std::vector<double> > result;
    std::istringstream iss(t_matrix);
    std::string rowStr;

    // Split the matrix string by ';'
    while (std::getline(iss, rowStr, ';')) {
        std::vector<double> row;
        std::istringstream rowIss(rowStr);
        std::string valueStr;

        // Split each row string by ','
        while (std::getline(rowIss, valueStr, ',')) {
            // Convert the substring to integer
            double value = this->gain * std::stod(valueStr);
            row.push_back(value);
        }
        // Add the row to the result
        result.push_back(row);
    }
	
	std::copy(result.begin(), result.end(), this->coeffs.begin());
    result.clear();
}

// Get the size of the kernel.
int Kernel::getSize(void){
	return this->size;
}

// Get the coefficients of the kernel.
std::vector< std::vector<double> >& Kernel::getCoeffs(void){
	return this->coeffs;
}

// Overloading the << operator to print information about the object.
std::ostream& operator<<(std::ostream& os, Kernel& ker) {
	os << "Kernel" << std::endl;
	int size = ker.getSize();
	os << size << std::endl;
	std::vector< std::vector<double> > coefs = ker.getCoeffs();
	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){
			os << coefs[i][j] << ' ';
		}
		os << std::endl;
	}
	os << std::endl;
	return os;
}
