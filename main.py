import os
import cv2 as cv
from PIL import Image as PImage
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

from util import image_process as ip
import gamma as gm


# Function: plot_
# Parameters: x, y, xlab, ylab
# Return: Plot with approipiate axis labels and data
# Description: Plot graphs for a given dataset and input for x and y axis
def plot_(x, y, xlab, ylab, main, colr):
	plt.plot(x,y, marker='o', color=colr)
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(main)
	plt.show()
	plt.clf()
	plt.cla()
	plt.close()


def main():

	curr_work_dir = os.getcwd()
	image_set = ["/img_1/", "/img_2/"]
	filepath_1 = curr_work_dir + image_set[0]
	filepath_2 = curr_work_dir + image_set[1]

	# Exposure times
	exp_time = [1/4, 1/5, 1/6, 1/8, 1/10, 1/13, 1/15, 1/20, 1/25, 1/30, 1/40, 1/50, 1/60, 1/80, 1/100, 1/125, 1/160, 1/200, 1/250]

	# Test
	#test_img = curr_work_dir + image_set[0] + "img1_1:004.JPG"
	#img = cv.imread(test_img)
	#print(ip.average_img_brightness(img))

	imgs = ip.load_images(filepath_1)
	brightness = ip.average_all_img_brightness(imgs)

	####### Part 1 #######
	# Plot the exposure time versus the image brightness
	plot_(exp_time, brightness[0], 'T(s)', 'B\'', 'Blue Channel Brightness vs Exposure Time', 'b')
	plot_(exp_time, brightness[1], 'T(s)', 'B\'', 'Green Channel Brightness vs Exposure Time', 'g')
	plot_(exp_time, brightness[2], 'T(s)', 'B\'', 'Red Channel Brightness vs Exposure Time', 'r')

if __name__ == "__main__":
    main()