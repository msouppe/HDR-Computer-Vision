import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from time import gmtime, strftime

from util import analyzer as an
from util import image_process as ip
import gamma as gm
import hdr

def composite_channel(chan1, chan2, chan3, g, a1, a2, method):
	composite_chann = chan1
	height, width = chan1.shape[:2]
	print("\nStart time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	#print("composite_channel() - chan1.shape[:2]: ",  chan1.shape[:2])
	
	for x in range(0, int(height)):
		for y in range(0, int(width)):

			threshold_chan3 = 255/ float((a2/a1) ** g)
			threshold_chan2 = 255/ float(a1 ** g)
			#print(x,y)
			#print("composite_chann[x][y]: ", composite_chann[x][y])
			c1 = composite_chann[x][y]
			c2 = ip.B_to_power_g(chan2, g, a1)
			c3 = ip.B_to_power_g(chan3, g, a2)

			if chan3[x][y] <= threshold_chan3:
				if method == 1:
					pixel3 = c3
				elif method == 2:
					pixel3 = (c1 + c2 + c3)/3
				composite_chann[x][y] = pixel3[x][y]

			elif chan2[x][y] <= threshold_chan2:
				if method == 1:
					pixel2 = c2
				elif method == 2:
					pixel2 = (c1 + c2)/2
				composite_chann[x][y] = pixel2[x][y]

			else:
				continue
	print("End time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	print("composite_channel() - channel completed!")
	return composite_chann

def compsite_imgs(img1, img2, img3, g, a1, a2, method):
	channel_1 = ip.split_channels(img1)
	channel_2 = ip.split_channels(img2)
	channel_3 = ip.split_channels(img3)

	blue = composite_channel(channel_1[0], channel_2[0], channel_3[0], g[0], a1, a2, method)
	green = composite_channel(channel_1[1], channel_2[1], channel_3[1], g[1], a1, a2, method)
	red = composite_channel(channel_1[2], channel_2[2], channel_3[2], g[2], a1, a2, method)

	print("compsite_imgs() - Composited channels completed!\n")

	return (blue, green, red)

def composite(filepath, g, a1, a2, method):
	imgs = ip.load_images(filepath) 

	(b,g,r) = compsite_imgs(imgs[0], imgs[1], imgs[2], g, a1, a2, method)
	composite_image = ip.merge_channels((b,g,r))
	return composite_image
