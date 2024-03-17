#ifndef	__KERNEL_H__
#define	__KERNEL_H__


#include <iostream>
#include <string>
#include <vector>
#include <fstream> 

class Kernel {
	public:
		/**
		 * @brief Construct a new Kernel object, square matrix.
		 * @param t_size Size of the kernel. Must be odd.
		 * @param t_matrix Coefficients of the Kernel.
		 *		matrix = "1, 2, 3; 3, 1, 5" is a 2 rows and 3 cols matrix
		 * @param t_gain Global gain on the coefficients.
		 */
		Kernel(int t_size, const std::string& t_matrix, double t_gain=1);
		
		/**
		 * @brief Set the coefficients of the kernel.
		 * @param t_matrix Coefficients of the Kernel.
		 *		matrix = "1, 2, 3; 3, 1, 5" is a 2 rows and 3 cols matrix
		 */
		void setMatrix(const std::string& t_matrix);

		/**
		 * @brief Get the size of the kernel.
		 * @return Size of the kernel in pixels.
		 */
		int getSize(void);

		/**
		 * @brief Get the coefficients of the kernel.
		 * @return A 2D array of int.
		 */		
		std::vector< std::vector<double> >& getCoeffs(void);

		// Declaration of operator<< as a friend function
		friend std::ostream& operator<<(std::ostream& os, Kernel& ker);

	private:
		int size;            	/**< Size of the kernel. */
		double gain;			/**< Global gain on the coefficients. */
		std::vector< std::vector<double> > coeffs; /**< Value of each coefficients of the kernel. */
};


#endif
