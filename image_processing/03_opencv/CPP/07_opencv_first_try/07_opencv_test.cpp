#include <iostream>
#include <opencv2/opencv.hpp>	// see compile.txt file for options
#include <chrono>				// need to be compiled with option :  -std=c++11


int main(int argc, char** argv) {
	
	std::cout << "Test OpenCV" << std::endl;
	
	// Time measurement
	std::chrono::duration<double, std::milli> duration;
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	
	
	// Open an image
	start = std::chrono::high_resolution_clock::now();	// time starts
	cv::Mat image = cv::imread("../../../_data/robot.pgm"); 
	end = std::chrono::high_resolution_clock::now();	// time stops
	duration = end - start;
    std::cout << "Execution time of read image: " << duration.count() << " milliseconds" << std::endl;
	
	// Display in a window
	std::string windowName = "Robot from LEnsE"; //Name of the window
	cv::namedWindow(windowName); // Create a window
	cv::imshow(windowName, image); // Show our image inside the created window.
	cv::waitKey(0); // Wait for any keystroke in the window
	cv::destroyWindow(windowName); //destroy the created window
	
	// Access to informations about the image
	cv::Size size = image.size();	
	std::cout << "W,H = " << size.height << "," << size.width << std::endl;
	std::cout << "Channels = " << image.channels() << std::endl;
	std::cout << "Depth = " << image.depth() << std::endl;
	std::cout << "Type = " << image.type() << std::endl;
	
	// Write an image in PGM
	cv::Mat grayImage;
	cv::cvtColor(image, grayImage, cv::COLOR_BGR2GRAY);
	cv::imwrite("robot2.pgm", grayImage);

	return 0;
}

