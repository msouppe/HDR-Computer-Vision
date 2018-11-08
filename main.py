import os
#import numpy as np
import cv2
from PIL import Image as PImage
from PIL import ImageEnhance


# Return array of images
def load_images(f_path):
   	img_array = []
   	imgs = os.listdir(f_path)

   	for image in imgs:
   	   	img = PImage.open(f_path + image)
   	   	img_array.append(img)

   	return img_array

# Calculate the average brightness per image
def brightness(image):
	greyscale = image.convert("L")
	histogram = greyscale.histogram()
	num_pixels = sum(histogram)
	brightnes = scale = len(histogram)

	for index in range(0, scale):
		ratio = histogram[index] / num_pixels
		brightnes += ratio * (-scale + index)

	return 1 if brightnes == 255 else brightnes / scale

def split_RGB(image):

	return r, g, b


def histogram(image):

	return r, g, b



def main():

	# Get current working directory and locate images	
	curr_work_dir = os.getcwd()
	image_set = ["/img_1/", "/img_2/"]

	# Exposure times
	time = [4, 5, 6, 8, 10, 13, 15, 20, 25, 30, 40, 50, 60, 80, 100, 125, 160, 200, 250]

	filepath_1 = curr_work_dir + image_set[0]
	filepath_2 = curr_work_dir + image_set[1]

	print(filepath_1)
	print(filepath_2)

	####### Part 1 #######

	# Load images into an image array
	p1_imgs = load_images(filepath_1)

	# Get average brightness for every image
	p1_brightness = []

	for i in p1_imgs:
		p1_brightness.append(brightness(i))

	print(p1_brightness)

	# Plot the exposure time versus the image brightness


if __name__ == "__main__":
    main()




