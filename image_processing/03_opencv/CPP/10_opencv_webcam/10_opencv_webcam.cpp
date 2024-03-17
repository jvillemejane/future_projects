#include <iostream>
#include <opencv2/opencv.hpp>	// see compile.txt file for options

#include<iostream>
#include<conio.h>           

int main() {
	cv::VideoCapture capWebcam(0);		 // declare a VideoCapture object to associate webcam, 0 means use 1st (default) webcam

	if (capWebcam.isOpened() == false)	 //  To check if object was associated to webcam successfully
	{
		std::cout << "error: Webcam connect unsuccessful\n";	// if not then print error message
		return(0);												// and exit program
	}

	cv::Mat imgOriginal;        // input image
	cv::Mat imgGrayscale;       // grayscale image
	cv::Mat imgBlurred;         // blured image
	cv::Mat imgOutput;          // Output edge image
	
	cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(9, 9));

	char charCheckForEscKey = 0;

	while (charCheckForEscKey != 27 && capWebcam.isOpened()) {            // until the Esc key is pressed or webcam connection is lost
		bool blnFrameReadSuccessfully = capWebcam.read(imgOriginal);	  // get next frame

		if (!blnFrameReadSuccessfully || imgOriginal.empty()) {				// if frame read unsuccessfully
			std::cout << "error: frame can't read \n";						// print error message
			break;															
		}

		// Resize image
		int up_width = 600;
		int up_height = 400;
		cv::resize(imgOriginal, imgOriginal, cv::Size(up_width, up_height), cv::INTER_LINEAR);
		
		// convert to grayscale
		cv::cvtColor(imgOriginal, imgGrayscale, cv::COLOR_BGR2GRAY);

		// Blur Effect 
		//cv::GaussianBlur(imgGrayscale, imgBlurred, cv::Size(5, 5), 1.2);
		
		// Opening
		cv::morphologyEx(imgGrayscale, imgBlurred, cv::MORPH_CLOSE, kernel);
		
		// Sodel Edge
		cv::Sobel(imgBlurred, imgOutput, CV_64F, 1, 1, 3);		         
		

		//declare windows     
		cv::namedWindow("imgCanny");    
		// show windows                
		cv::imshow("imgCanny", imgOutput);                       

		charCheckForEscKey = cv::waitKey(1);        // delay and get key press
	}

	return(0);
}