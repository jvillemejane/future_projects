#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>		// need to be compiled with option :  -std=c++11
#include "ImagePGM.h"


int main(int argc, char** argv) {
	
	// Time measurement
	std::chrono::duration<double, std::milli> duration;
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	
    // Read the input PGM image
	start = std::chrono::high_resolution_clock::now();	// time starts
    ImagePGM image("../../_data/robot.pgm");
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of read image: " << duration.count() << " milliseconds" << std::endl;


	std::cout << "Infos" << std::endl;
	std::cout << image << std::endl;
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	image.rotateImagePGM();
	end = std::chrono::high_resolution_clock::now();	// time stops

	duration = end - start;
    std::cout << "Execution time of rotate: " << duration.count() << " milliseconds" << std::endl;
	
	std::cout << "Infos" << std::endl;
	std::cout << image << std::endl;

	if(image.writeImagePGM("robot2.pgm")){
		std::cout << "Image written" << std::endl;
	}

    return 0;
}
