import sys,os
import cv2
import pylab as plt
import numpy as np
import math
import time
import serial
sys.path.append('../piggyphoto')
sys.path.append('../myPys')
import piggyphoto 
import myCV
import Polygon2D
import ColorDetector
import ImageWindow

def main():
	##input image files
	filename = 'images/DSC_0030.JPG'
#	filename = 'images/s_DSC_0030.JPG'
#	filename = 'images/redSpot.JPG'
	img = cv2.imread(filename,cv2.CV_LOAD_IMAGE_COLOR)

	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	hue = hsv[:,:,0]
	saturation = hsv[:,:,1]
	meido = hsv[:,:,2]

	##process
	output_image,binary_img,area = getContactArea(img)

	## image output
	print 'area=',area,'[mm^2]'
	images = {'image':img,'hsv':hsv,'hue':hue,'saturation':saturation,'meido':meido,'red':output_image,'binary':binary_img}
	#images = {'image':img,'ContactArea':output_image}
	myCV.displayImages(images)


def getContactArea(img):
	scale = 1 / 200.0 ## mm/pixel

	colorDetecotor = ColorDetector.ColorDetector(img)
	area_img = colorDetecotor.detectRed()
	img_for_contour = np.copy(area_img)
	contours, hierarchy = cv2.findContours(img_for_contour,cv2.cv.CV_RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (0,255,0), 2)
	area = cv2.countNonZero(area_img) * scale
	return img,area_img,area


#def getContatctPosition(img):






if __name__ == "__main__":
	main()



