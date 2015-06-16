#!/usr/bin/python

import random, math
from PIL import Image

#Loads in an image, finds the size, and calls grid on it
def artGen():
	pic = Image.open("plazanew.jpg")
	imageWidth = pic.size[0]
	imageHeight = pic.size[1]
	print(imageWidth)
	print(imageHeight)

	r, g, b = pic.split()
	print("Working on R")
	r = grid(r, imageWidth, imageHeight)
	print("Done with R")
	print("Working on G")
	g = grid(g, imageWidth, imageHeight)
	print("Done with G")
	print("Working on B")
	b = grid(b, imageWidth, imageHeight)
	print("Done with B")
	# r.save("r.png", "JPEG")
	# g.save("g.png", "JPEG")
	# b.save("b.png", "JPEG")
	
	final = Image.merge("RGB", (r, g, b))
	final.save("plazanewnew.jpg", "JPEG")

def grid(im, width, height):
	sqAcross = int(width/15)
	sqUpDown = int(height/15)

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

artGen()

