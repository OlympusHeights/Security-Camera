''' 
File: dload_images.py
Description: Will download the images pointed from a text file fill with urls. 
OpenCV will read each image, change to grayscale, and resize them. Finally, OpenCV will overwrite the 
previous image and save the new image. 
Run: python dload_img.py  

'''
import urllib.request
import cv2
import numpy as np
import os 

def download_img():
	neg_images_link = '' # txt file leading to the images
	neg_images_url = urllib.request.urlopen(neg_images_link).read().decode() # Reading url links from txt 

	if not os.path.exists('neg'): # Make dir if not created already
		os.makedir('neg')

	pic_num = 1 # track imgs 

	for i in neg_images_urls.split('\n') # seperate url by new line
		try: 
			print(i)
			urllib.request.urlretrieve(i, "neg/" + str(pic_num) + '.jpg') # get pictures store and name it 
			img = cv2.imread("neg/" + str(pic_num) + 'jpg', cv2.IMREAD_GRAYSCALE)# cv2 read img as a gray pic
			resized_images = cv2.resize(img, (100, 100)) # cv2 resize img 
			cv2.imwrite("neg/" + str(pic_num) + '.jpg', resized_images)# now overwrite the img with new size
			pic_num += 1 # increase counter
		except Exception as e:
			print(str(e))


download_img()