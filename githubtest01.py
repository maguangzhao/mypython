from PIL import Image,ImageDraw

'''
def add_num(img):
	draw = ImageDraw.Draw(img)
	fillcolor = '#ff0000'
	width,height = img.size
	draw.text((width-50,20),'99',font = None,fill = fillcolor)
	img.save('result1.png','png')

	img.show()

if __name__ == '__main__':
	image = Image.open('test.png')
	add_num(image)
'''
'''
im = Image.open('test.png')

im.rotate(45).show()
'''

def rollimg(img,delta):
	image = img.copy()
	xsize,ysize = image.size
	delta = delta%xsize
	if  delta == 0:
		return image
	part1 = image.crop((0,0,delta,ysize))
	part2 = image.crop((delta,0,xsize,ysize))

	image.paste(part2,(0,0,xsize-delta,ysize))
	image.paste(part1,(xsize-delta,0,xsize,ysize))
	image.show()
	#return image

if __name__ == '__main__':
	image = Image.open('test.png')
	rollimg(image,90)


















