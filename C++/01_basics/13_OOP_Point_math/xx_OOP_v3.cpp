#include <iostream>
#include <cstdlib>
#include "Point.h"

/**
 * @brief Main function of the program.
 */
int main(void){
	
	std::cout << "My program" << std::endl;
		
	Point p1;
	Point p2(1, 3);
	std::cout << "P1 " << p1 << std::endl;
	std::cout << "P2 " << p2 << std::endl;
	
	double dist = p1.getDistance(p2);
	
	std::cout << "Distance P1-P2 : " << dist << std::endl;	

	std::cout << "End of my program" << std::endl;

	return EXIT_SUCCESS;
}

