#include <iostream>
#include <fstream>
#include <string>

int main() {
    // File path
    std::string filename = "example.txt";

    // Create an input file stream object
    std::ifstream infile;

    // Open the file
    infile.open(filename.c_str());

    // Check if the file was successfully opened
    if (!infile.is_open()) {
        std::cerr << "Error: Unable to open file " << filename << std::endl;
        return 1;
    }

    // Read and process the file contents
    std::string line;
    while (std::getline(infile, line)) {
        // Process each line of the file
        std::cout << line << std::endl;
    }

    // Close the file
    infile.close();

    return 0;
}



/*


#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Function to read a PGM image from a file
void readPGMImage(string filename) {
	
    // Create an input file stream object
    ifstream my_file;

    // Open the file
    my_file.open(filename);
	
	
	
    PGMImage image;
	
	
    if (my_file.is_open()) {
	
		
        my_file >> image.magic_number >> image.width >> image.height >> image.max_gray_value;

        image.pixels.resize(image.height, std::vector<int>(image.width));

        for (int i = 0; i < image.height; ++i) {
            for (int j = 0; j < image.width; ++j) {
                file >> image.pixels[i][j];
            }
        }
		
        my_file.close();
    } else {
        cerr << "Error: Unable to open file " << filename << endl;
    }

    return;
}


int main () {
	
	readPGMImage("robot.pgm");
  
  
  string line;
  
  
  ifstream myfile ("robot.pgm");
  if (myfile.is_open())
  {

    while(getline(myfile, line)) {
      cout << line << endl;
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 
	
	
	return 0;
}

*/