import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# My library
from util import analyzer as an
from util import image_process as ip
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
exp_time = [1/125, 1/180, 1/350, 1/500, 1/750, 1/1000, 1/1500, 1/2000]
log_exp= log_(exp_time)

#-----------------------------------------------------------------#
#                              Part 1 
#-----------------------------------------------------------------#
curve, g, brightness = gm.gamma(log_exp, img_path)
log_bright = log_(brightness)

# Exposure Time vs Brightness
xlab = 'T(s)'
ylab = 'B`(T)'
color = ['Blue', 'Green', 'Red']
main = ' - Exposure Time vs Brightness'
an.plot_(exp_time, brightness[0], xlab, ylab, color[0] + main, 'b') 
an.plot_(exp_time, brightness[1], xlab, ylab, color[1] + main, 'g')
an.plot_(exp_time, brightness[2], xlab, ylab, color[2] + main, 'r')

# Log of Exposure Time vs Log of Brightness plus regression
xlab = 'log T(s) '
ylab = 'log B`(T)'
main = ' - log(Exposure Time) vs log(Brightness)'
an.multi_plot_(log_exp, log_bright[0], curve[0], xlab, ylab, color[0] + main, 'b')
an.multi_plot_(log_exp, log_bright[1], curve[1], xlab, ylab, color[1] + main, 'g')
an.multi_plot_(log_exp, log_bright[2], curve[2], xlab, ylab, color[2] + main, 'r')

# Exposure Time vs Brightness`G 
xlab = 'T(s)'
ylab = r'B = B`$^{\frac{1}{a}}$'
main = ' - Linearized Exposure Time vs Brightness'
an.plot_(exp_time, gm.adjusted_brightness(brightness[0], g[0]), xlab, ylab, color[0] + main, 'b')
an.plot_(exp_time, gm.adjusted_brightness(brightness[1], g[1]), xlab, ylab, color[1] + main, 'g')
an.plot_(exp_time, gm.adjusted_brightness(brightness[2], g[2]), xlab, ylab, color[2] + main, 'r')

#-----------------------------------------------------------------#
#                              Part 2 
#-----------------------------------------------------------------#
xlab = 'Pixel Values'
ylab = 'Number of Pixels'
hdr_img = ip.load_images(hdr_path)
hdr_exposure = [1/8000, 1/1000, 1/250]

# Histogram B'g (a0 * T)
# Note: exposure time = 1/8000, a0 = 1
main = 'T = ' + str(hdr_exposure[0])
an.hist_gamma(hdr_img[0], g, xlab, ylab, main)

# Histogram B'g (a1 * T)
# Note: exposure time = 1/1000
main = 'T = ' + str(hdr_exposure[1])
an.hist_gamma(hdr_img[1], g, xlab, ylab, main)

# Histogram B'g (a2 * T)
# Note: exposure time = 1/250
main = 'T = ' + str(hdr_exposure[2])
an.hist_gamma(hdr_img[2], g, xlab, ylab, main)

# Histogram B'g (a1 * T) / a1
main = 'T = ' + str(hdr_exposure[1])
a1 = hdr_exposure[1]/ hdr_exposure[0]
an.hist_gamma(hdr_img[1], g, xlab, ylab, main, a1)

# Histogram B'g (a2 * T) / a2
main = 'T = ' + str(hdr_exposure[2])
a2 = hdr_exposure[2]/ hdr_exposure[0]
an.hist_gamma(hdr_img[2], g, xlab, ylab, main, a2)

#-----------------------------------------------------------------#
#                              Part 3 
#-----------------------------------------------------------------#
# HDR1 Histogram
method1 = 1
composite_image_1 = hdr.composite(hdr_path, g, a1, a2, method1)
an.hist_hdr1(composite_image_1, xlab, ylab, g, 'HDR1 Histogram')

# HDR2 Histogram
method2 = 2
composite_image_2 = hdr.composite(hdr_path, g, a1, a2, method2)
an.hist_hdr1(composite_image_2, xlab, ylab, g, 'HDR2 Histogram')

#-----------------------------------------------------------------#
#                              Part 4 
#-----------------------------------------------------------------#
# HDR1 Image
img1 = np.uint8(composite_image_1)
convert1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
plt.imshow(hdr.tone_map(convert1/255))
plt.savefig("HDR1.png")
plt.show()

# HDR2 Image
img2 = np.uint8(composite_image_2)
convert2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
plt.imshow(hdr.tone_map(convert2/255))
plt.savefig("HDR2.png")
plt.show()
