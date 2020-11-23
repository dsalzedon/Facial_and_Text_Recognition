import zipfile
import pytesseract
from PIL import Image, ImageDraw, ImageFont
import cv2 as cv
import numpy as np


def get_slides(word):
    slides = []
    for x in img_wrds:
        if word in img_wrds[x]:
            slide = create_slide(x, img_faces[x])
            slides.append(slide)
    return slides


def create_slide(pic_name, crop_faces):
    if len(crop_faces) == 0:
        canvas = Image.new('RGB',(750, 50), (255,255,255))
        draw = ImageDraw.Draw(canvas)
        draw.text((15, 10),"Result found in {}\nBut there were no faces in that file!".format(pic_name), fill='black')
    else:
        canvas = Image.new('RGB',(750, 350))
        canvas_white = Image.new('RGB',(750, 50), (255,255,255))
        canvas.paste(canvas_white, (0,0))
        draw = ImageDraw.Draw(canvas)
        draw.text((15, 10),"Result found in {}".format(pic_name), font=fnt, fill='black')

        x = 0
        y = 50

        for face in crop_faces:
            face = Image.fromarray(face).resize((150,150))
            canvas.paste(face, (x,y))

            if x + face.width >= canvas.width:
                x = 0
                y = int(y + face.height)
            else:
                x = int(x + face.width)

    return canvas


def create_canvas(slides, word_search):
	canvas = Image.new('RGB',(750, 350*len(slides)), (255,255,255))

	x = 0
	y = 0

	for pic in slides:
	    canvas.paste(pic, (x,y))

	    if x + pic.width >= canvas.width:
	        x = 0
	        y = int(y + pic.height)
	    else:
	        x = int(x + pic.width)

	#canvas.show()
	canvas.save(f"img/{word_search}.jpg")

	return canvas



# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('readonly/haarcascade_eye.xml')


zip_path = "/Users/dsalzedo/Documents/Python/Scripts/Face_Recog/small_img.zip"
# fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 15)

# creating dictionary, { image_name: text in picture}
with zipfile.ZipFile(zip_path) as myzip:
    my_files = myzip.namelist()
    print(my_files)
    img_wrds = {x: pytesseract.image_to_string(cv.cvtColor(np.array(Image.open(myzip.open(x))), cv.COLOR_BGR2GRAY)) for x in my_files}

# creating dictionary, { image_name: faces}
img_faces = {}
with zipfile.ZipFile(zip_path) as myzip:
    for x in my_files:
        pil_image = Image.open(myzip.open(x))
        img = np.array(pil_image)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3, 5)
        img_faces[x] = [img[y:y+h, x:x+h] for (x,y,w,h) in faces]


word_search = "Christopher"
slides = get_slides(word_search)

canvas = create_canvas(slides, word_search)

# show canvas for Christopher
canvas.show()

word_search = "Mark"
slides = get_slides(word_search)

canvas = create_canvas(slides, word_search)

# show canvas for Mark
canvas.show()
