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
	
	p1.setPosition(2, 5);
	std::cout << "P1 new " << p1 << std::endl;
	
	int x1, y1;
	p1.getPosition(x1, y1);
	std::cout << "x1, y1 = " << x1 << ", " << y1 << std::endl;
	

	std::cout << "End of my program" << std::endl;

	return EXIT_SUCCESS;
}

