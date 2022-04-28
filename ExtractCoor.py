#! /usr/bin/env python3

#EtractCoor: Extract longitude and latitude coordinates from pdf and image files
#C.E. Supsup & T. Nguyen
#28 April 2022

#required modules (install outside this command, using the default terminal on mac or linux)
#pip install tkinter
#pip install tika
#pip install pytesseract
#pip install pillow
#tika module will run only if java is installed.
#if text extraction is not working for images, install tesseract ocr from https://github.com/tesseract-ocr/

#Method 1 - PDF > TEXT > REGEX SEARCH > EXPORT

#Step 1 - extract text from pdf file

#prompt user to provide input 
import tkinter as tk
from tkinter import filedialog
from tika import parser

root = tk.Tk()
root.withdraw()
mydata = filedialog.askopenfilename()

#extract text using tika parser
pdf_data = parser.from_file(mydata)
mytext = pdf_data['content']

#Step 2 - find longitude and latitude using regex and export
import re
import csv

#listing out common patterns of coordinates shown in research papers
#compile the patterns and assign them to different variables
pattern_1 = re.compile(r'\d+\D\d+\W\d+\D\d+\W\w')
pattern_2 = re.compile(r'\d+\d\.\d+\°\w')

#find an item in the text that follow these patterns
#assign that item to a variable
p1_long_lat = pattern_1.findall(mytext)
p2_long_lat = pattern_2.findall(mytext)

for pat1 in p1_long_lat:
    if pat1 == "":
        print("No available coordinates")
        break

    else:
        s1_long_lat = str(p1_long_lat) #convert patterns to string
        rmb1_long_lat = re.sub(r'\\', '', s1_long_lat) #remove backslash
        split1_long_lat = re.split(r'[^\d\w.]+', rmb1_long_lat) #remove other symbols
        filtered1_long_lat = list(filter(None, split1_long_lat)) #remove empty strings
        
        with open("mylonglat_dms.csv", "w") as f_out: #pattern_1 export as a csv file
            csv_writer = csv.writer(f_out)
            i = iter(filtered1_long_lat)
            csv_writer.writerow(["deg", "min", "sec", "direction", "deg", "min", "sec", "direction"])
            for t in zip(*[i] * 8):
                print(t)
                csv_writer.writerow(t)

for pat2 in p2_long_lat:
    if pat2 == "":
        print("No available coordinates")
        break

    else:
        s2_long_lat = str(p2_long_lat)
        rmb2_long_lat = re.sub(r'\\', '', s2_long_lat) #remove backslash
        split2_long_lat = re.split(r'[^\d\w.]+', rmb2_long_lat) #remove other symbols
        filtered2_long_lat = list(filter(None, split2_long_lat)) #remove empty strings

        with open("mylonglat_dd.csv", "w") as f_out: #pattern_2 export as a csv file
            csv_writer = csv.writer(f_out)
            i = iter(filtered2_long_lat)
            csv_writer.writerow(["latitude", "direction", "longitude", "direction"])
            for t in zip(*[i] * 4):
                print(t)
                csv_writer.writerow(t)

#Method 2 - IMAGE > TEXT > REGEX SEARCH > EXPORT
import pytesseract as pt
from PIL import Image

myimg_text = pt.image_to_string(mydata)

img_p1_long_lat = pattern_1.findall(myimg_text)
img_p2_long_lat = pattern_2.findall(myimg_text)

for img_pat1 in img_p1_long_lat:
    if img_pat1 == "":
        print("No available coordinates")
        break

    else:
        s1_long_lat = str(img_p1_long_lat) #convert patterns to string
        rmb1_long_lat = re.sub(r'\\', '', s1_long_lat) #remove backslash
        split1_long_lat = re.split(r'[^\d\w.]+', rmb1_long_lat) #remove other symbols
        filtered1_long_lat = list(filter(None, split1_long_lat)) #remove empty strings
        
        with open("mylonglat_dms.csv", "w") as f_out: #pattern_1 export as a csv file
            csv_writer = csv.writer(f_out)
            i = iter(filtered1_long_lat)
            csv_writer.writerow(["deg", "min", "sec", "direction", "deg", "min", "sec", "direction"])
            for t in zip(*[i] * 8):
                print(t)
                csv_writer.writerow(t)

for img_pat2 in img_p2_long_lat:
    if img_pat2 == "":
        print("No available coordinates")
        break

    else:
        s2_long_lat = str(img_p2_long_lat)
        rmb2_long_lat = re.sub(r'\\', '', s2_long_lat) #remove backslash
        split2_long_lat = re.split(r'[^\d\w.]+', rmb2_long_lat) #remove other symbols
        filtered2_long_lat = list(filter(None, split2_long_lat)) #remove empty strings

        with open("mylonglat_dd.csv", "w") as f_out: #pattern_2 export as a csv file
            csv_writer = csv.writer(f_out)
            i = iter(filtered2_long_lat)
            csv_writer.writerow(["latitude", "direction", "longitude", "direction"])
            for t in zip(*[i] * 4):
                print(t)
                csv_writer.writerow(t)

