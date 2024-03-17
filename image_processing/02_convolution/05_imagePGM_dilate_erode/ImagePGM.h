#ifndef	__IMAGE_PGM_H__
#define	__IMAGE_PGM_H__


#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include "Kernel.h" 

class ImagePGM {
	public:
		/**
		 * @brief Construct a new empty ImagePGM object from a filename.
		 */
		ImagePGM(void);
		/**
		 * @brief Construct a new ImagePGM object from a filename.
		 * @param filename Name of the file name of the image (constant).
		 */
		ImagePGM(const std::string& filename);

		/**
		 * @brief Open an image file.
		 * @param filename Name of the file of the image (constant).
		 * @return true if the file exists.
		 */
		bool readImagePGM(const std::string& filename);

		/**
		 * @brief Write an image file.
		 * @param filename Name of the file of the image (constant).
		 * @return true if the file is created.
		 */
		bool writeImagePGM(const std::string& filename);
		
		/**
		 * @brief Rotate the image.
		 */		
		void rotateImagePGM(void);
		
		/**
		 * @brief Convolute image to a specific Kernel.
		 * @param ker Kernel for convolution.
		 */		
		ImagePGM convImagePGM(Kernel& ker);
		
		/**
		 * @brief Dilate image with a specific Kernel.
		 * @param ker Kernel for dilatation.
		 */		
		ImagePGM dilateImagePGM(Kernel& ker);

		/**
		 * @brief Set the size of the image.
		 * @param t_width Width of the image.
		 * @param t_height Height of the image.
		 */			
		void setSize(int t_width, int t_height);
		
		/**
		 * @brief Set the maximum gray value of the image.
		 * @param t_max_gray_value Maximum gray value of the image.
		 */		
		void setMaxGray(int t_max_gray_value);

		/**
		 * @brief Set the pixel values of the image.
		 * @param t_pixels A 2D matrix of int.
		 */			
		void setPixels(std::vector< std::vector<int> > t_pixels);
		
		/**
		 * @brief Get the total number of pixels of the image.
		 * @return Total number of pixels of the image.
		 */		
		int getNbPixels(void);
		
		// Declaration of operator<< as a friend function
		friend std::ostream& operator<<(std::ostream& os, const ImagePGM& img);

	private:
		int width;             /**< Width of the image. */
		int height;            /**< Height of the image. */
		int channels;          /**< Number of color value for each pixel of the image. */
		int max_gray_value;    /**< Value of the white color. */
		std::string magic_number;  /**< Type of the file. */

		std::vector< std::vector<int> > pixels; /**< Value of each pixels. */
};


#endif
