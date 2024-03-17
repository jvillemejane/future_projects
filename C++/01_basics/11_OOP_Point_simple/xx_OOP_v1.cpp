#include <iostream>
#include <cstdlib>

/**
 * @brief Class to describe a point in a 2D plan.
 */
class Point {
	private:
		int x;	/**< Coordinate along the X-axis of the point. */
		int y;	/**< Coordinate along the Y-axis of the point. */

	public:    
		/**
		 * @brief Construct a new Point object with coodinates (0, 0).
		 */
		Point() {
			this->x = 0;
			this->y = 0;
		}

		/**
		 * @brief Construct a new Point object with coodinates (x, y).
		 *
		 * @param x Coordinate along the X-axis of the point.
		 * @param y Coordinate along the Y-axis of the point.
		 */
		Point(int x0, int y0): x(x0), y(y0) {}
		
		/**
		 * @brief Set the coodinates of the point at (x, y).
		 *
		 * @param x Coordinate along the X-axis of the point.
		 * @param y Coordinate along the Y-axis of the point.
		 */
		void setPosition(int x, int y) {
			this->x = x;
			this->y = y;
		}
		
		/**
		 * @brief Return the coodinate of the point along the X-axis.
		 *
		 * @return Coordinate along the X-axis of the point.
		 */
		int getCoordX() {
			return this->x;
		}
		
		/**
		 * @brief Return the coodinate of the point along the X-axis.
		 *
		 * @return Coordinate along the Y-axis of the point.
		 */
		int getCoordY() {
			return this->y;
		}
		
		/**
		 * @brief Get the position of the point.
		 *
		 * @param x Reference to the coordinate along the X-axis of the point.
		 * @param y Reference to the coordinate along the Y-axis of the point.
		 */
		void getPosition(int& x, int& y){
			x = this->x;
			y = this->y;
		}
		
		// Overloading the << operator to print information about the object
		friend std::ostream& operator<<(std::ostream& os, const Point& obj) {
			os << "Point (" << obj.x << ", " << obj.y << ")" << std::endl;
			return os;
		}
};

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

