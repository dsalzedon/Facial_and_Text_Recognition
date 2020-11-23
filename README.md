# Facial Recognition   

This code uses the libraries **PIL**, **PYTESSERACT**, **OPENCV**, and **NUMPY** as the core of the program. It opens a zip file with images inside and searchs for a name in the images' text; if there's a match it would then go through all the faces it recognized in the images and returns as a new image with these faces on it. If there's a match for the word but not faces are recognized in the image, it would output "there's a match but no faces in the file".   

First, the path of the zip file is given, the code returns a list with the name of the files in it, and loops through the zip file once more and with **PYTESSERACT**, converts all the words in the image to strings, by opening the file as an image -> converting it to a gray scale for easier processing -> and then converting the image's text into strings. It then creates a dictionary with the name of the file as the key and the strings as values.

Second, it loops through the zipe file and converts the images to a gray scale for easier processing. With **OPENCV** it detects the faces in the image and returns a dictionary with the name of the file as key and the faces it found as values.

Third, it loops through the values in the dictionary of strings searching for the name, if there's a match it then creates a new image with these faces and appends it to a list. After all the strings are compare, it creates a new image with all the faces found.

Here's an example looking for "Christopher":
![alt text](https://raw.githubusercontent.com/dsalzedon/facial_recognition/main/img/1.png)   
Here's an example looking for "Mark":
![alt text](https://raw.githubusercontent.com/dsalzedon/facial_recognition/main/img/2.png)   
