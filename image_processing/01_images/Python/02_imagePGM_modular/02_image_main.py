from ImagePGM import *

# Main function
if __name__ == "__main__":
    # Read the input PGM image
    image = ImagePGM("../../../_data/robot.pgm")

    print("Infos")
    print(image)
    
    image.writeImagePGM("robot2.pgm")
    print("End of test")
