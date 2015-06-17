#!/usr/bin/python

import random, math
from PIL import Image

#Loads in an image, finds the size, and calls grid on each RGB band
def artGen(numGrids):
	pic = Image.open("img.jpg")
	imageWidth = pic.size[0]
	imageHeight = pic.size[1]
	print(imageWidth)
	print(imageHeight)

	r, g, b = pic.split()
	r = grid(r, imageWidth, imageHeight, numGrids)
	g = grid(g, imageWidth, imageHeight, numGrids)
	b = grid(b, imageWidth, imageHeight, numGrids)

	final = Image.merge("RGB", (r, g, b))
	final.save("imgnew.jpg", "JPEG")

#separates image into grids
def grid(im, width, height, numGrids):
	sqAcross = int(width/numGrids)
	sqUpDown = int(height/numGrids)

	sqDimension = max(sqAcross, sqUpDown)

	left = 0
	top = 0

	while (top + sqDimension) <= height:
		while (left + sqDimension) <= width:
			right = left + sqDimension
			bottom = top + sqDimension
 			
 			box = (left, top, right, bottom)
			region = changeImage(im.crop(box))
			
			im.paste(region, box)

			right = left
			left = left + sqDimension

		top = bottom
		bottom = bottom + sqDimension
		left = 0
		im.paste(region, box)
				
	return im

def changeImage(region):
	if random.choice((True, False)):
		region = region.transpose(Image.FLIP_TOP_BOTTOM)
	elif random.choice((True, False)):
		region = region.transpose(Image.FLIP_LEFT_RIGHT)
	else:
		region = region
	
	return region

num = input("Enter how many grids would you like to divide your image into: ")
artGen(num)

