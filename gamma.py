import os
from util import image_process as ip
import numpy as np
from scipy import stats

def gamma(exp_times, filepath):
	imgs = ip.load_images(filepath)
	brightness = ip.average_all_img_brightness(imgs)

	g = []
	curve = []

	blue = brightness[0] 
	green = brightness[1]
	red = brightness[2]

	blue_curve, b_gamma = linear_regression_curve(exp_times, np.log10(blue))
	green_curve, g_gamma = linear_regression_curve(exp_times, np.log10(green))
	red_curve, r_gamma = linear_regression_curve(exp_times, np.log10(red))

	g.append(b_gamma)
	g.append(g_gamma)
	g.append(r_gamma)

	curve.append(blue_curve)
	curve.append(green_curve)
	curve.append(red_curve)

	return curve, g, brightness	

# Calculate linear regression coefficients
def linear_regression_curve(exp_times, channel):
	slope, intercept, r_value, p_value, std_error = stats.linregress(exp_times, channel)
	y = np.add(slope * exp_times,intercept)
	gamma = 1/slope
	return y, gamma

# Calulate adjusted brightness
def adjusted_brightness(channel, gamma):
	return np.power(channel, gamma)