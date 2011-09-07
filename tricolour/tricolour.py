#!/usr/bin/python

#Filename: tricolour.py
#Author: Jithu Sunny
#Date: June 29, 2011

import Image, ImageDraw
from math import pi, cos, sin

#Magic Ratio used to keep the width of circle & lines proportionate to the size of the image. Calculated by finding the ratio of width of image to width of line in a test image.
MAGIC_WIDTH = 0.01406
CIRCUM_WIDTH = 0
LINE_WIDTH = 0


def select_Size():
    '''Returns the size of the flag'''

    print '1. 1280 X 960'
    print '2. 1024 X 768'
    print '3. 800 X 600'
    print '4. 320 X 240'
    print '5. Custom'
    choice = int(raw_input('Enter your choice: '))
    
    if choice == 1:
        return 1280, 960
    elif choice == 2:
        return 1024, 768
    elif choice == 3:
        return 800, 600
    elif choice == 4:
        return 320, 240
    else:
        width = int(raw_input('Enter the width: '))
        height = int(raw_input('Enter the height: '))

    return width, height


def draw_Spokes(draw, centre_pt, radius):
    ''' Draw the 24 spokes inside the Ashoka-Chakra'''

    global LINE_WIDTH
    px = centre_pt[0]
    py = centre_pt[1]

    for degree in range(0, 360, 15):
        qx = px + radius * cos(pi/180 * degree)
        qy = py + radius * sin(pi/180 * degree)
        draw.line([px, py, qx, qy], fill = "#23238E", width = LINE_WIDTH)
    return


def draw_Ashoka_Chakra(draw, width, height):
    ''' Draw the Ashoka Chakra'''

    global CIRCUM_WIDTH
    c = CIRCUM_WIDTH

    diameter = height / 3
    radius = diameter / 2
    px = width/2 - radius
    py = height/2 - radius
    qx = px + diameter
    qy = py + diameter
    # The Circle of Ashoka-Chakra
    draw.ellipse([px, py, qx, qy], "#23238E") #Colour code, Navy blue - #23238E
    draw.ellipse([px + c, py + c, qx - c, qy - c], "white")

    sub_diameter = diameter / 5  
    sub_radius = sub_diameter / 2
    px = width/2 - sub_radius
    py = height/2 -sub_radius
    qx = px + sub_diameter
    qy = py + sub_diameter
    # The small circle at the centre of Ashoka-Chakra
    draw.ellipse([px, py, qx, qy], "#23238E")

    draw_Spokes(draw, (width/2, height/2), height/6)# Draw spokes
    return


def draw_Rectangles(draw, width, height):
    ''' Draw & fill the three rectangles on the flag - Deep Saffron, White & India Green'''

    draw.rectangle( [0, 0, width, height/3], "#FF9933") #Colour code, Deep Saffron - #FF9933
    draw.rectangle( [0, height/3, width, 2 * height/3], "white")
    draw.rectangle( [0, 2 * height/3, width, height], "#138808") #Colour code, India green - #138808
    return


def main():
    
    global MAGIC_WIDTH, CIRCUM_WIDTH, LINE_WIDTH

    width, height = select_Size()
   
    CIRCUM_WIDTH = int(MAGIC_WIDTH * width)
    LINE_WIDTH = int(CIRCUM_WIDTH / 3)
    
    im = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(im)

    draw_Rectangles(draw, width, height)
    draw_Ashoka_Chakra(draw, width, height)

    im.save("flag.jpg")

main()
