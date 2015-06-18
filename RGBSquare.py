#!/usr/bin/python

import random, math
from PIL import Image, ImageDraw

#Loads in an image, finds the size, and calls grid on each RGB band
def artGen(numGrids):
	pic = Image.open("img.jpg")
	imageWidth = pic.size[0]
	imageHeight = pic.size[1]
	
	r, g, b = pic.split()
	r = grid(r, imageWidth, imageHeight, numGrids, 1)
	g = grid(g, imageWidth, imageHeight, numGrids, 1)
	b = grid(b, imageWidth, imageHeight, numGrids, 1)

	final = Image.merge("RGB", (r, g, b))
	#final = grid(final, imageWidth, imageHeight, numGrids, 2)

	final.save("img2.jpg", "JPEG")

#separates image into grids
def grid(im, width, height, numGrids, switch):
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

			if (switch == 1):
				region = changeImage(im.crop(box))
			elif (switch == 2):
				region = drawPoly(im.crop(box), sqDimension)

			im.paste(region, box)
			right = left
			left = left + sqDimension
		top = bottom
		bottom = bottom + sqDimension
		left = 0
		im.paste(region, box)		
	return im

def randomChooser(region, dimension):
	if random.choice((True, False)):
		changeImage(region)
	else:
		drawPoly(region, dimension)

def changeImage(region):
	if random.choice((True, False)):
		region = region.transpose(Image.FLIP_TOP_BOTTOM)
	elif random.choice((True, False)):
		region = region.transpose(Image.FLIP_LEFT_RIGHT)
	else:
		region = region
	return region

#Currently not being used
def drawPoly(region, dimension):
	if random.choice((True, False)):
		img = Image.new("RGB", (dimension, dimension))
		draw = ImageDraw.Draw(img)

		r = lambda: random.randint(0,255)

		draw.ellipse((0,0,dimension,dimension),fill='#%02X%02X%02X' % (r(),r(),r()))
		img = Image.blend(img, region, .1)
		return img
	else:
		return region
	


num = input("Enter how many grids would you like to divide your image into: ")
artGen(num)

