#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>		// need to be compiled with option :  -std=c++11
#include "ImagePGM.h"


int main(int argc, char** argv) {
		
    // Read the input PGM image
    ImagePGM image("../../_data/robot.pgm");
    ImagePGM image_conv;
	
	// Time measurement
	std::chrono::duration<double, std::milli> duration;
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	
	
	// Test of a kernel
	std::string matrix = "1, 1, 0; 1, 0, 1; 0, 1, 0";
	Kernel ker1(3, matrix);
	
	std::cout << ker1 << std::endl;
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_conv = image.convImagePGM(ker1);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of conv: " << duration.count() << " milliseconds" << std::endl;
	std::cout << "Execution time of conv / pixel: " << duration.count() / image.getNbPixels() * 1000 << " microseconds/pixel" << std::endl;


	if(image_conv.writeImagePGM("robot_conv.pgm")){
		std::cout << "Image written" << std::endl;
	}


	// Test of a Sodel kernel
	std::string sodel_v = "-1, 0, 1; -2, 0, 2; -1, 0, 1";
	Kernel ker_sodel_v(3, sodel_v);
	
	std::cout << ker_sodel_v << std::endl;
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_conv = image.convImagePGM(ker_sodel_v);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of Sodel conv: " << duration.count() << " milliseconds" << std::endl;
	std::cout << "Execution time of Sodel conv / pixel: " << duration.count() / image.getNbPixels() * 1000 << " microseconds/pixel" << std::endl;


	if(image_conv.writeImagePGM("robot_conv_sodel.pgm")){
		std::cout << "Image written" << std::endl;
	}

	// Test of a 3*3 mean filters
	std::string mean3 = "1, 1, 1; 1, 1, 1; 1, 1, 1"; // 1/9
	Kernel ker_mean3(3, mean3, 1./9.);
	
	std::cout << ker_mean3 << std::endl;
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_conv = image.convImagePGM(ker_mean3);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of 3*3 mean filters: " << duration.count() << " milliseconds" << std::endl;
	std::cout << "Execution time of 3*3 mean filters / pixel: " << duration.count() / image.getNbPixels() * 1000 << " microseconds/pixel" << std::endl;


	if(image_conv.writeImagePGM("robot_conv_mean3.pgm")){
		std::cout << "Image written" << std::endl;
	}

	// Test of a 5*5 mean filters
	std::string mean5 = "1, 1, 1, 1, 1; 1, 1, 1, 1, 1; 1, 1, 1, 1, 1; 1, 1, 1, 1, 1; 1, 1, 1, 1, 1"; // 1/25
	Kernel ker_mean5(5, mean5, 1.0/25.);
	
	std::cout << ker_mean5 << std::endl;
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image_conv = image.convImagePGM(ker_mean5);
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of 5*5 mean filters: " << duration.count() << " milliseconds" << std::endl;
	std::cout << "Execution time of 5*5 mean filters / pixel: " << duration.count() / image.getNbPixels() * 1000 << " microseconds/pixel" << std::endl;


	if(image_conv.writeImagePGM("robot_conv_mean5.pgm")){
		std::cout << "Image written" << std::endl;
	}

    return 0;
}
