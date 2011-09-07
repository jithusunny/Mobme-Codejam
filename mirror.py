#!/usr/bin/python

#Filename: mirror.py
#Author: Jithu Sunny
#Date: June, 21 2011

from math import sqrt
from urllib import urlretrieve
import os, re, string, Image, ImageChops, sys

def extension(url):
    '''Returns the extension of the image in the url'''
    match = re.search(r'.[A-Za-z]+$', url)
    if match:
        return match.group()
    else:
        return ''

def rms(list):
    '''Returns the Root Mean Square value of a set of numbers.'''
    sum = 0

    for item in list:
        sum += item * item

    mean = sum/len(list)
    return sqrt(mean)

def make_even(im1, im2):
    '''Checks for disparity in image sizes & makes it even.'''
    if im1.size > im2.size:
        im2 = im2.resize(im1.size, Image.BICUBIC)
    elif im2 > im1:
        im1 = im1.resize(im2.size, Image.BICUBIC)

    return im1, im2

def main():
    '''Main Function'''

    url1 = raw_input('Enter the link to the first image: ')
    url2 = raw_input('Enter the link to the second image: ')

    ext1 = extension(url1)
    ext2 = extension(url2)

    if string.upper(ext1) != string.upper(ext2):
        print 'File-types dont match..!'
        sys.exit(1)

    file1 = 'im1' + ext1
    file2 = 'im2' + ext2

    urlretrieve(url1, file1)
    urlretrieve(url2, file2)

    diff_perc_seq = []

    im1 = Image.open(file1)
    im2 = Image.open(file2)
 
    
    im1, im2 = make_even(im1, im2) #The image sizes are even now.

    diff_image = ImageChops.difference(im1, im2) #diff_image contains the pixel level difference as an RGB tuple.

    #getbbox returns box containing the non-zero regions of the image. If its none, difference is none..!
    if diff_image.getbbox() is None:
        print 'Mirror Images..! The images are 100% similar. Similarity Scale value - 100'
    else:
        pixel_tuple_seq = diff_image.getdata() #pixel_tuple_seq contains the list of difference pixel tuples(R, G, B).


        pixel_rms_seq = map(rms, pixel_tuple_seq) #pixel_rms_seq contains the rms list of difference pixel tuples.
        #The percentage of difference is found out using formula, perc = (value/255) * 100
        for item in pixel_rms_seq:
            diff_perc_seq.append(item/255*100)
        avg_diff = sum(diff_perc_seq)/len(diff_perc_seq) #The total average difference is found out.
        similarity = 100 - avg_diff

        if avg_diff == 100:
            print 'The images are completely dissimilar. Similarity scale value - 0'
        else:
            print 'The images are %.2f%% similar. Similarity scale value - %.2f ' %(similarity, similarity)
    os.system('rm ' + file1 + ' ' + file2)

main()
