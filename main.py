import os
import cv2 as cv
from PIL import Image as PImage
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

from util import image_process as ip


# Function: plot_
# Parameters: x, y, xlab, ylab
# Return: Plot with approipiate axis labels and data
# Description: Plot graphs for a given dataset and input for x and y axis
def plot_(x, y, xlab, ylab, main):
	plt.plot(x,y)
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(main)
	plt.show()
	plt.clf()
	plt.cla()
	plt.close()


def main():

	# Exposure times
	exp_time = [1/4, 1/5, 1/6, 1/8, 1/10, 1/13, 1/15, 1/20, 1/25, 1/30, 1/40, 1/50, 1/60, 1/80, 1/100, 1/125, 1/160, 1/200, 1/250]

	# Test
	test_img = curr_work_dir + image_set[0] + "img1_1:004.JPG"
	img = cv.imread(test_img)
	print(ip.average_img_brightness(img))

	####### Part 1 #######
	# Plot the exposure time versus the image brightness
	plot_(exp_time, brightness[0], 'T(s)', 'B\'', 'Blue Channel Brightness vs Exposure Time')
	plot_(exp_time, brightness[1], 'T(s)', 'B\'', 'Green Channel Brightness vs Exposure Time')
	plot_(exp_time, brightness[2], 'T(s)', 'B\'', 'Red Channel Brightness vs Exposure Time')

if __name__ == "__main__":
    main()