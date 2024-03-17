#ifndef	__IMAGE_PGM_H__
#define	__IMAGE_PGM_H__


#include <iostream>
#include <string>
#include <vector>
#include <fstream> 

class ImagePGM {
	public:
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
