import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Function: load_images
# Parameter(s): f_path
# Return: Array of images
# Description: Retrieves images from specified src
def load_images(f_path, roi=False):
	img_array = []
	imgs = os.listdir(f_path)
	print("load_images(): ", sorted(imgs))


	for image in sorted(imgs):
		if image.endswith(".JPG"):
			#img = PImage.open(f_path + image)
			img = cv.imread(f_path + image)				
			img_array.append(region_of_interest(img, roi))

	return img_array

# Function: region_of_interest
# Parameters: image
# Return: Crop image from region of interest
# Description: For a given image, crop out a square of the image
def region_of_interest(image, roi):
	# Get image dimensions
	height, width = image.shape[:2]

	if (roi):
		#print("region_of_interest() - Gamma")
		h = int(height / 4)
		w = int(width * 3 / 4)

		# Crop image
		imgCrop = image[h:h+200, w:w+200]

	else:
		#print("region_of_interest() - HDR")
		# Keep OG image
		h = int(height)
		w = int(width)
		imgCrop = image[0:h, 0:w]

	#print("region_of_interest() - image shape:", imgCrop.shape[:2])

	# Sanity check that the region was choosen correctly
	#im[h:h+100, w:w+100] = [255,255,255]

	return imgCrop

# Function: split_channels
# Parameter(s): image
# Return: Numpy array of color channels: b,g,r
# Description: Split image by color channels
def split_channels(image):	
	img = cv.split(image)
	return img

# Description: Calculate the average brightness of a single channel
def avg_channel_brightness(channel):
	sum_pixels = channel.sum()
	num_pixels = channel.size
	avg_brightness = sum_pixels / num_pixels
	return avg_brightness

# Description: Calculate the average brightness of an image
def average_img_brightness(image):
	channel = split_channels(image)

	b_brightness = avg_channel_brightness(channel[0])
	g_brightness = avg_channel_brightness(channel[1])
	r_brightness = avg_channel_brightness(channel[2])

	return [b_brightness, g_brightness, r_brightness]

# Decription: Return matrix of all images brightness for each channel
def average_all_img_brightness(images):
	img_brightness = []

	for img in images:
		img_brightness.append(average_img_brightness(img))

	img_brightness = np.array(img_brightness)

	b_brightness = np.sort(img_brightness[:,0])[::-1]
	g_brightness = np.sort(img_brightness[:,1])[::-1]
	r_brightness = np.sort(img_brightness[:,2])[::-1]

	return [b_brightness, g_brightness, r_brightness]

def merge_channels(channels):
	newImg = cv.merge(channels)
	return newImg

def B_to_power_g(channel, g, a):
	newChan = np.divide(np.float32(np.power(channel, g)), a)
	return newChan

