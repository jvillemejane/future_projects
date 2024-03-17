#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>		// need to be compiled with option :  -std=c++11
#include "ImagePGM.h"


int main(int argc, char** argv) {
		
    // Read the input PGM image
    ImagePGM image("../../_data/black_white.pgm");
    ImagePGM image_opening;
	
	// Time measurement
	std::chrono::duration<double, std::micro> duration;
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	
	
	// Test of an opening
	std::string struct_m = "0, 0, 1, 0, 0; 0, 0, 1, 0, 0; 1, 1, 1, 1, 1; 0, 0, 1, 0, 0; 0, 0, 1, 0, 0";
	Kernel ker_struct(5, struct_m);
	
	std::cout << ker_struct << std::endl;
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_opening = image.openingImagePGM(ker_struct);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of opening transform: " << duration.count() << " microseconds" << std::endl;
	std::cout << "Execution time of opening transform / pixel: " << duration.count() / image.getNbPixels() << " microseconds/pixel" << std::endl;

	if(image_opening.writeImagePGM("black_white_opening.pgm")){
		std::cout << "Image written" << std::endl;
	}

	// Test of an opening
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_opening = image.closingImagePGM(ker_struct);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of closing transform: " << duration.count() << " microseconds" << std::endl;
	std::cout << "Execution time of closing transform / pixel: " << duration.count() / image.getNbPixels() << " microseconds/pixel" << std::endl;

	if(image_opening.writeImagePGM("black_white_closing.pgm")){
		std::cout << "Image written" << std::endl;
	}

	// Test of an opening
    ImagePGM robot("../../_data/robot.pgm");
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_opening = robot.closingImagePGM(ker_struct);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of closing transform: " << duration.count() << " microseconds" << std::endl;
	std::cout << "Execution time of closing transform / pixel: " << duration.count() / image.getNbPixels() << " microseconds/pixel" << std::endl;

	if(image_opening.writeImagePGM("robot_closing.pgm")){
		std::cout << "Image written" << std::endl;
	}
	
	// Test of an opening and closing
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_opening = image_opening.openingImagePGM(ker_struct);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of closing transform: " << duration.count() << " microseconds" << std::endl;
	std::cout << "Execution time of closing transform / pixel: " << duration.count() / image.getNbPixels() << " microseconds/pixel" << std::endl;

	if(image_opening.writeImagePGM("robot_closing_opening.pgm")){
		std::cout << "Image written" << std::endl;
	}
	
    return 0;
}
