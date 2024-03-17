#include <iostream>
#include <opencv2/opencv.hpp>	// see compile.txt file for options
#include <chrono>				// need to be compiled with option :  -std=c++11


int main(int argc, char** argv) {
	
	std::cout << "Test OpenCV" << std::endl;
	
	// Time measurement
	std::chrono::duration<double, std::micro> duration;
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	
	// Open an image
	cv::Mat image = cv::imread("../../../_data/robot.pgm"); 
	
	// Transform image to grayscale
	cv::Mat grayImage;
	cv::cvtColor(image, grayImage, cv::COLOR_BGR2GRAY);
	
	cv::Size size = grayImage.size();
	int nb_pixels = size.height * size.width;
	
	// Erosion with a 3x3 kernel
	cv::Mat image_erode3;
	
	start = std::chrono::high_resolution_clock::now();	// time starts
	cv::erode(grayImage, image_erode3, cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3, 3)));
	end = std::chrono::high_resolution_clock::now();	// time stops
	duration = end - start;
    std::cout << "Execution time of 3*3 erosion: " << duration.count() << " microseconds" << std::endl;	
	std::cout << "Execution time of 3*3 erosion / pixel: " << duration.count() / nb_pixels << " microseconds/pixel" << std::endl;
	

	
	cv::imwrite("robot_erode3.pgm", grayImage);

	// Opening with a 3x3 kernel
	cv::Mat image_opening3;
	cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(9, 9));
	
	start = std::chrono::high_resolution_clock::now();	// time starts
    cv::morphologyEx(grayImage, image_opening3, cv::MORPH_OPEN, kernel);
	end = std::chrono::high_resolution_clock::now();	// time stops
	duration = end - start;
    std::cout << "Execution time of 3*3 opening: " << duration.count() << " microseconds" << std::endl;	
	std::cout << "Execution time of 3*3 opening / pixel: " << duration.count() / nb_pixels << " microseconds/pixel" << std::endl;

	// Display in a window
	std::string windowName = "Blur - Robot from LEnsE"; //Name of the window
	cv::namedWindow(windowName); // Create a window
	cv::imshow(windowName, image_opening3); // Show our image inside the created window.
	cv::waitKey(0); // Wait for any keystroke in the window
	cv::destroyWindow(windowName); //destroy the created window



	return 0;
}

