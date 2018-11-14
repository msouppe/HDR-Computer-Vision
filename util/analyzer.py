import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

# Function: plot_
# Parameters: x, y, xlab, ylab, main, color
# Return: Plot with approipiate axis labels and data
# Description: Plot graphs for a given dataset and input for x and y axis
def plot_(x, y, xlab, ylab, main, colr):
	plt.plot(x, y, marker='o', color=colr)
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(main)
	plt.show()
	plt.clf()
	plt.cla()
	plt.close()

def multi_plot_(x, y, y1, xlab, ylab, main, colr):
	plt.plot(x, y, marker='o', color=colr)
	plt.plot(x, y1, color='black')
	plt.xlabel(xlab)
	plt.ylabel(ylab)
	plt.title(main)
	plt.show()
	plt.clf()
	plt.cla()
	plt.close()

def hist_gamma(imag, g, xlab, ylab, a=1):
	img = cv.imread(imag)
	num_bins = 256
	color = ('b','g','r')

	for i,col in enumerate(color):
		end = np.power(255, g[i])
		image = np.divide(np.float32(np.power(img, g[i])), a)

		plt.subplot(1, 3, i+1)
		histr = cv.calcHist([image], [i], None, [256], [0,end])
		plt.plot(histr, color = col)
		plt.xlabel(xlab)
		plt.ylabel(ylab)

	plt.tight_layout()
	plt.show()

def hist_hdr1(image, xlab, ylab, g):
	color = ('b','g','r')

	for i,col in enumerate(color):
		end = np.power(255, g[i])
		plt.subplot(1, 3, i+1)
		histr = cv.calcHist([image], [i], None, [256], [0,256])
		plt.plot(histr, color = col)
		plt.fill_between(histr, 0, closep)
		plt.xlabel(xlab)
		plt.ylabel(ylab)

	plt.tight_layout()
	plt.show()