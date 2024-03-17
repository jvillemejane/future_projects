#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include "ImagePGM.h"


int main(int argc, char** argv) {
    // Read the input PGM image
    ImagePGM image("../../_data/robot.pgm");

	std::cout << "Infos" << std::endl;
	std::cout << image << std::endl;

	if(image.writeImagePGM("robot2.pgm")){
		std::cout << "Image written" << std::endl;
	}

    return 0;
}
