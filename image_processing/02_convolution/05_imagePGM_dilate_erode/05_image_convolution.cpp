#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>		// need to be compiled with option :  -std=c++11
#include "ImagePGM.h"


int main(int argc, char** argv) {
		
    // Read the input PGM image
    ImagePGM image("../../_data/black_white.pgm");
    ImagePGM image_dil;
	
	// Time measurement
	std::chrono::duration<double, std::micro> duration;
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	
	
	// Test of a dilatation
	std::string struct_m = "0, 1, 0; 1, 1, 1; 0, 1, 0";
	Kernel ker_struct(3, struct_m);
	
	std::cout << ker_struct << std::endl;
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_dil = image.dilateImagePGM(ker_struct);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of dilatation: " << duration.count() << " microseconds" << std::endl;
	std::cout << "Execution time of dilatation / pixel: " << duration.count() / image.getNbPixels() << " microseconds/pixel" << std::endl;


	if(image_dil.writeImagePGM("black_white_dilatation.pgm")){
		std::cout << "Image written" << std::endl;
	}

	// Test of a erosion
		
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_dil = image.erodeImagePGM(ker_struct);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of erosion: " << duration.count() << " microseconds" << std::endl;
	std::cout << "Execution time of erosion / pixel: " << duration.count() / image.getNbPixels() << " microseconds/pixel" << std::endl;


	if(image_dil.writeImagePGM("black_white_erosion.pgm")){
		std::cout << "Image written" << std::endl;
	}	

    return 0;
}
