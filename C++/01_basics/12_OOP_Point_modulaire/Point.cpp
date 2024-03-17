#include <iostream>
#include <cstdlib>
#include "Point.h"


Point::Point(): x(0), y(0){}

Point::Point(int x0, int y0): x(x0), y(y0){}

void Point::setPosition(int x, int y) {
	this->x = x;
	this->y = y;
}

int Point::getCoordX() {
	return this->x;
}
		
int Point::getCoordY() {
	return this->y;
}

void Point::getPosition(int& x, int& y){
	x = this->x;
	y = this->y;
}

// Overloading the << operator to print information about the object
std::ostream& operator<<(std::ostream& os, const Point& point) {
	os << "Point (" << point.x << ", " << point.y << ")" << std::endl;
	return os;
}
		