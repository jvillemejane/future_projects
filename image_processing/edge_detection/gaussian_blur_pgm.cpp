#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>


// Structure to represent a PGM image
struct PGMImage {
    std::string magic_number;
    int width;
    int height;
    int max_gray_value;
    std::vector< std::vector<int> > pixels;
};

// Function to read a PGM image from a file
PGMImage readPGMImage(const std::string& filename) {
    std::ifstream file(filename.c_str());
    PGMImage image;

    if (file.is_open()) {
        file >> image.magic_number >> image.width >> image.height >> image.max_gray_value;

        image.pixels.resize(image.height, std::vector<int>(image.width));

        for (int i = 0; i < image.height; ++i) {
            for (int j = 0; j < image.width; ++j) {
                file >> image.pixels[i][j];
            }
        }

        file.close();
    } else {
        std::cerr << "Error: Unable to open file " << filename << std::endl;
    }

    return image;
}

// Function to write a PGM image to a file
void writePGMImage(const PGMImage& image, const std::string& filename) {
    std::ofstream file(filename.c_str());

    if (file.is_open()) {
        file << image.magic_number << std::endl;
        file << image.width << " " << image.height << std::endl;
        file << image.max_gray_value << std::endl;

        for (int i = 0; i < image.height; ++i) {
            for (int j = 0; j < image.width; ++j) {
                file << image.pixels[i][j] << " ";
            }
            file << std::endl;
        }

        file.close();
    } else {
        std::cerr << "Error: Unable to open file " << filename << std::endl;
    }
}

// Function to apply Gaussian blur to a PGM image
void gaussianBlur(PGMImage& image, int kernel_size, double sigma) {
    std::vector< std::vector<int> > new_pixels(image.height, std::vector<int>(image.width));

    int radius = kernel_size / 2;
    std::vector<double> kernel(kernel_size);

    // Generate the Gaussian kernel
    double sum = 0.0;
    for (int i = 0; i < kernel_size; ++i) {
        int x = i - radius;
        kernel[i] = exp(-(x * x) / (2 * sigma * sigma)) / (sqrt(2 * M_PI) * sigma);
        sum += kernel[i];
    }

    // Normalize the kernel
    for (int i = 0; i < kernel_size; ++i) {
        kernel[i] /= sum;
    }

    // Apply the Gaussian blur filter
    for (int y = radius; y < image.height - radius; ++y) {
        for (int x = radius; x < image.width - radius; ++x) {
            double weighted_sum = 0.0;
            for (int i = -radius; i <= radius; ++i) {
                for (int j = -radius; j <= radius; ++j) {
                    weighted_sum += image.pixels[y + i][x + j] * kernel[i + radius] * kernel[j + radius];
                }
            }
            new_pixels[y][x] = static_cast<int>(weighted_sum);
        }
    }

    image.pixels = new_pixels;
}

int main(int argc, char** argv) {
    // Read the input PGM image
    PGMImage image = readPGMImage("robot.pgm");

    // Apply Gaussian blur with kernel size 3 and sigma 1.0
    gaussianBlur(image, 3, 1.0);

    // Write the filtered image to a new PGM file
    writePGMImage(image, "output.pgm");

    std::cout << "Gaussian blur applied successfully!" << std::endl;

    return 0;
}
