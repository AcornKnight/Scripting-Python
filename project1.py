#! /usr/bin/env

# Noah R Gestiehr
# Scripting II Dr. Noor
# CIT 483 Fall 2021
# This code will create a parser object, ask a user to pass a filename and a command, if the filename is a zipped directory
# Unzip it, then perform the command on the given pictures before saving them into a new processed directory.


import os, argparse, shutil, re, glob
from PIL import ImageColor
from PIL import Image


# Project 1 Part 1



# Parser

parser = argparse.ArgumentParser(description='This parser will take an image file from the user then modify it based on optional arguements.')

parser.add_argument('filename',help='Enter a file or a folder.')

parser.add_argument('--resize', '-r',nargs=2,, help='Enter the new height and width for the file [height width]')

parser.add_argument('--crop', '-c',nargs=2, help='Enter the file size as height width that you wish to crop.')

parser.add_argument('--sign', '-s', help='Provides the file containing the signature of the owner.')

parser.add_argument('--rotate', '-r', help='Rotates the file image the given degrees.')

parser.add_argument('--upload', '-u', help='Provide a link where the image will be uploaded into the server.')

args = parser.parse_args()

prints(args)

# Functions

def operation_resize(filename,resize0,resize1):

     myimage = Image.open(filename)
	 resizedImage = myimage.resize((resize0, resize1))
	 resizedImage.save('resized.png')
     shutil.copy('resized.png','processed')

def operation_crop(filename,crop0,crop1):

     myimage = Image.open(argv.filename)
	 croppedIm = myimage.crop((imagesize[0], imagesize[1], crop0, crop1))
	 croppedIm.save('cropped.png')
     shutil.copy('cropped.png','processed')
	 
def operation_sign(filename,sign):

    CopyIm = filename.copy()
	// crCopyIm = CopyIm.crop((500, 500, 900, 900))
	CopyIm.paste(sign, (300, 300))
	CopyIm.save('signed.png')
    shutil.copy('signed.png','processed')
	 
def operation_rotate(filename,rotate):

     myimage = Image.open(filename)
	 rotatedImage=myimage.rotate)
	 rotatedImage.save('rotated.png')
     shutil.copy('rotated.png','processed')
	 

	 
	 
# Checks input to see if input is a file or a directory, if it is a directory, processes it.

if os.path.isdir(argv.filename):
    filepart = os.path.splitext(argv.filename)
    if ( filepart[1] == '.zip'):
       os.system('unzip {argv.filename}')
    if ( filepart[1] == '.tar'):
        os.system('tar -xvf {argv.filename}')

# helpme = argv.filename
for file in glob.glob("{argv.filename}/*.png"):
    shutil.copy(file, '.')
    
    
# Function Call

# shutil.rmtree('processed')
os.mkdir('processed')
myimage = Image.open(argv.filename)
imagesize=myimage.size

if argv.resize:
    operation_resize(argv.filename,argv.resize[0],argv.resize[1])
    
if argv.crop:
    operation_crop(argv.filename,argv.crop[0],argv.crop[1])

if argv.rotate:
    operation_rotate(argv.filename,argv.rotate[0])

if argv.sign:
    operation_sign(argv.filename,argv.sign)