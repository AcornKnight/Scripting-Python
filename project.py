#! /usr/bin/env

import os, argprase
from PIL import ImageColor
from PIL import Image


# Project 1 Part 1



# Parser

parser = argprase.ArgumentParser(description='This parser will take an image file from the user then modify it based on optional arguements.')

parser.add_argument('filename',help='Enter a file or a folder.')

parser.add_argument('--resize', '-r',nargs=2,, help='Enter the new height and width for the file [height width]')

parser.add_argument('--crop', '-c',nargs=2, help='Enter the file size as height width that you wish to crop.')

parser.add_argument('--sign', '-s', help='Provides the file containing the signature of the owner.')

parser.add_argument('--rotate', '-r', help='Rotates the file image the given degrees.')

parser.add_argument('--upload', '-u', help='Provide a link where the image will be uploaded into the server.')

args = parser.parse_args()

prints(args)

# Functions

def operation_resize(argv.filename,argv.resize[0],argv.resize[1])

     myimage = Image.open(argv.filename)
	 resizedImage = myimage.resize((argv.resize[0], argv.resize[1]))
	 resizedImage.save('resized.png')

def operation_crop(argv.filename,argv.crop[0],argv.crop[1])

     myimage = Image.open(argv.filename)
	 croppedIm = myimage.crop((imagesize[0], imagesize[1], argv.crop[0], argv.crop[1]))
	 croppedIm.save('cropped.png')
	 
def operation_sign(argv.filename,argv.sign)

    CopyIm = argv.filename.copy()
	// crCopyIm = CopyIm.crop((500, 500, 900, 900))
	CopyIm.paste(argv.sign, (300, 300))
	CopyIm.save('signed.png')
	 
def operation_rotate(argv.filename,argv.rotate[0])

     myimage = Image.open(argv.filename)
	 rotatedImage=myimage.rotate(rotate[0])
	 rotatedImage.save('rotated.png')
	 

	 
	 
# Checks input to see if input is a file or a directory, if it is a directory, processes it.

if 

# Function Call

myimage = Image.open(argv.filename)
imagesize=myimage.size