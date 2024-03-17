#ifndef POINT_H  // If the identifier POINT_H is not defined
#define POINT_H  // Define POINT_H to prevent multiple inclusion

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
		Point();

		/**
		 * @brief Construct a new Point object with coodinates (x, y).
		 *
		 * @param x Coordinate along the X-axis of the point.
		 * @param y Coordinate along the Y-axis of the point.
		 */
		Point(int x0, int y0);
		
		/**
		 * @brief Set the coodinates of the point at (x, y).
		 *
		 * @param x Coordinate along the X-axis of the point.
		 * @param y Coordinate along the Y-axis of the point.
		 */
		void setPosition(int x, int y);
		
		/**
		 * @brief Return the coodinate of the point along the X-axis.
		 *
		 * @return Coordinate along the X-axis of the point.
		 */
		int getCoordX();
		
		/**
		 * @brief Return the coodinate of the point along the X-axis.
		 *
		 * @return Coordinate along the Y-axis of the point.
		 */
		int getCoordY();
		
		/**
		 * @brief Get the position of the point.
		 *
		 * @param x Reference to the coordinate along the X-axis of the point.
		 * @param y Reference to the coordinate along the Y-axis of the point.
		 */
		void getPosition(int& x, int& y);
		
		// Declaration of operator<< as a friend function
		friend std::ostream& operator<<(std::ostream& os, const Point& point);
};

#endif