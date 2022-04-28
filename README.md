# ExtractCoor - Extract geographic coordinates from pdf and image files
This code can automate longitude and latitude extraction from pdf and image files and store these to a csv file, which can be used directly to any GIS software. Currently, only the following formats can be extracted:
```
Degrees, minutes, and seconds: 6°31′21″N, 114°09′50″W
Decimal degrees: 36.5243°S, 114.1641°W
```
We wrote and tested the python code under Linux Mint and macOS. Before using the tool make sure to install the following:
1. Python3 https://www.python.org/downloads/
2. Java https://java.com/en/download/manual.jsp
3. Tesseract OCR https://github.com/tesseract-ocr/tesseract

Required python modules:
```
pip install tkinter
pip install tika
pip install pytesseract
pip install pillow
```
