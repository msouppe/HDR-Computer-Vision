import os
from util import image_process as ip

# Get current working directory and locate images
curr_work_dir = os.getcwd()
image_set = ["/img_1/", "/img_2/"]
filepath_1 = curr_work_dir + image_set[0]
filepath_2 = curr_work_dir + image_set[1]




def gamma():
	imgs = ip.load_images(filepath_1)
	brightness = ip.average_all_img_brightness(imgs)