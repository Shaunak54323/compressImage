import os
from PIL import Image

def compressImage(image):
    Image.open(os.join(os.getcwd(), image)).save("Compressed_" + image, "JPEG", quality=50)

formats = [".jpg", ".png", ".jpeg"]
for file in os.listdir(os.getcwd()):
    if file.endswith(tuple(formats)):
        compressImage(file)
        print("Done Compressing ... " + file)