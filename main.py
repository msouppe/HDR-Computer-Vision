import os
import cv2 as cv
from PIL import Image as PImage
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

# Function: load_images
# Parameter(s): f_path
# Return: Array of images
# Description: Retrieves images from specified src
def load_images(f_path):
   	img_array = []
   	imgs = os.listdir(f_path)

   	for image in imgs:
   	   	#img = PImage.open(f_path + image)
   	   	img = cv.imread(f_path + image)
   	   	img_array.append(get_img_center(img))

   	return img_array

# Function: brightness
# Parameter(s): image
# Return: Brightness of an image
# Description: Calculate the average brightness per image
def brightness(image):
	sum_pixels = image.sum()
	num_pixels = image.shape[:2]

	#bright = cv.mean(image)
	bright =  sum_pixels/ num_pixels

	return bright

# Function: plot_
# Parameters: x, y, xlab, ylab
# Return: Plot with approipiate axis labels and data
# Description: Plot graphs for a given dataset and input for x and y axis
def plot_(x, y, xlab, ylab):
	plt.plot(x,y)
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.show()
	plt.clf()
	plt.cla()
	plt.close()

# Function: get_img_center
# Parameters: image
# Return: Crop image from region of interest
# Description: For a given image, crop out a square of the image
def get_img_center(image):
	# Get image dimensions
	height, width = image.shape[:2]
	h = int(height / 2)
	w = int(width / 2)

	# Crop image
	imgCrop = image[h:h+100, w:w+100]

	# Sanity check that the region was choosen correctly
	#im[h:h+100, w:w+100] = [255,255,255]

	return imgCrop

# Function: split_BGR
# Parameter(s): image
# Return: 3 arrays, one for every color channel
# Description: Split image by color channels
def split_RGB(image):	
	r = image[0,:,:]
	g = image[:,0,:]
	b = image[:,:,0]

	return r,g,b

def histogram(image):

	return r, g, b

def main():
	# Get current working directory and locate images
	curr_work_dir = os.getcwd()
	image_set = ["/img_1/", "/img_2/"]
	filepath_1 = curr_work_dir + image_set[0]
	filepath_2 = curr_work_dir + image_set[1]

	# Exposure times
	exp_time = [1/4, 1/5, 1/6, 1/8, 1/10, 1/13, 1/15, 1/20, 1/25, 1/30, 1/40, 1/50, 1/60, 1/80, 1/100, 1/125, 1/160, 1/200, 1/250]

	print(filepath_1)      
	print(filepath_2)

	#test_img = curr_work_dir + image_set[0] + "Part1_1:40.JPG"
	#img = cv.imread(test_img)
	#a, b, c = split_RGB(img)
	#print(brightness(a))

	####### Part 1 #######

	# Load images into an image array
	p1_imgs = load_images(filepath_1)

	blue_1 = []
	green_1 = []
	red_1 = []

	print(p1_imgs[1].shape)

	# Split images into color channels
	for i in p1_imgs:
		r,g,b = split_RGB(i)
		blue_1.append(b)
		green_1.append(g)
		red_1.append(r)

	# Get average brightness for every color channel for each img
	brightness_red = []
	brightness_blue = []
	brightness_green = []
	p1_brightness = []

	#print(len(p1_imgs))

	for i in range(0,len(p1_imgs)):
		p1_brightness.append(brightness(red_1[i]))

	#print(p1_brightness)

	# Plot the exposure time versus the image brightness
	plot_(exp_time, exp_time, 'T(s)', 'B\'')

if __name__ == "__main__":
    main()




