import os
import cv2 as cv
from PIL import Image as PImage
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

# Repo library
from util import analyzer as an
import gamma as gm
import hdr

def log_(value):
	log_value = np.log10(value)
	return log_value

# Get current working directory and locate images
curr_work_dir = os.getcwd()
img_path = curr_work_dir + "/images/"
hdr_path = curr_work_dir + "/hdr/"

# Exposure times
#exp_time = [1/4, 1/5, 1/6, 1/8, 1/10, 1/13, 1/15, 1/20, 1/25, 1/30, 1/40, 1/50, 1/60, 1/80, 1/100, 1/125, 1/160, 1/200, 1/250]
exp_time = [1/125, 1/180, 1/350, 1/500, 1/750, 1/1000, 1/1500, 1/2000]
log_exp= log_(exp_time)

###################################################################
############################## Part 1 #############################
###################################################################
curve, g, brightness = gm.gamma(log_exp, img_path)
log_bright = log_(brightness)

# Exposure Time vs Brightness
xlab = 'T(s)'
ylab = 'B`(T)'
color = ['Blue', 'Green', 'Red']
main = ' - Exposure Time vs Brightness'
#an.plot_(exp_time, brightness[0], xlab, ylab, color[0] + main, 'b') 
#an.plot_(exp_time, brightness[1], xlab, ylab, color[1] + main, 'g')
#an.plot_(exp_time, brightness[2], xlab, ylab, color[2] + main, 'r')

# Log of Exposure Time vs Log of Brightness plus regression
xlab = 'log T(s) '
ylab = 'log B`(T)'
main = ' - log(Exposure Time) vs log(Brightness)'
#an.multi_plot_(log_exp, log_bright[0], curve[0], xlab, ylab, color[0] + main, 'b')
#an.multi_plot_(log_exp, log_bright[1], curve[1], xlab, ylab, color[1] + main, 'g')
#an.multi_plot_(log_exp, log_bright[2], curve[2], xlab, ylab, color[2] + main, 'r')

# Exposure Time vs Brightness`G 
xlab = 'T(s)'
ylab = r'B = B`$^{\frac{1}{a}}$'
main = ' - Linearized Exposure Time vs Brightness'
#an.plot_(exp_time, gm.adjusted_brightness(brightness[0], g[0]), xlab, ylab, color[0] + main, 'b')
#an.plot_(exp_time, gm.adjusted_brightness(brightness[1], g[1]), xlab, ylab, color[1] + main, 'g')
#an.plot_(exp_time, gm.adjusted_brightness(brightness[2], g[2]), xlab, ylab, color[2] + main, 'r')

###################################################################
############################## Part 2 #############################
###################################################################
xlab = 'Pixel Values'
ylab = 'Number of Pixels'
hdr = ['hdr1_42.JPG', 'hdr2_44.JPG', 'hdr3_45.JPG']
print(g)

# Histogram B'g (a0 * T)
# Note: exposure time = 1/2000
#       a0 = 1
an.hist_(hdr_path + hdr[0], g, xlab, ylab)

# Histogram B'g (a1 * T)
# Note: exposure time = 1/750
#       a1 = 2.6667
an.hist_(hdr_path + hdr[1], g, xlab, ylab)

# Histogram B'g (a2 * T)
# Note: exposure time = 1/250
#       a2 = 8
an.hist_(hdr_path + hdr[2], g, xlab, xlab)

# Histogram B'g (a1 * T) / a1
a1 = 2.6667
an.hist_(hdr_path + hdr[1], g, xlab, ylab, a1)

# Histogram B'g (a2 * T) / a2
a2 = 8
an.hist_(hdr_path + hdr[2], g, xlab, xlab, a2)

###################################################################
############################## Part 3 #############################
###################################################################
