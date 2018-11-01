import os
import numpy as np
#import cv2
#from PIL import Image as PImage


# Return array of images
def load_images(self, f_path):
   	img_array = []
   	imgs = listdir(f_path)

   	for image in imgs:
		img = PImage.open(path + image)
		img_array.append(img)

	return img_array

def split_RGB(self, image):

	return r, g, b

def main():

	# Get current working directory and locate images	
	curr_work_dir = os.getcwd()
	image_set = ["/img_1/", "/img_2/"]

	filepath_1 = curr_work_dir + image_set[0]
	filepath_2 = curr_work_dir + image_set[1]

	# print(filepath_1)
	# print(filepath_2)

	# Part 1
	# load_images(filepath_1)


if __name__ == "__main__":
    main()