import requests
from io import BytesIO
from PIL import Image
import re
from hashlib import md5
import os

image_dir = 'img_raw/'
output_dir = 'img/'

image_files = [file for file in os.listdir(image_dir)
               if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

MAX_WIDTH = 768
MAX_HEIGHT = 768


for fi in range(len(image_files)):
    image_file = os.path.join(image_dir, image_files[fi])

    output_file = os.path.join(output_dir,
            '.'.join(image_files[fi].split('.')[:-1])+'.jpg')
    if os.path.isfile(output_file):
        continue
    print(fi, '/', len(image_files))

    img = Image.open(image_file).convert("RGB")
    sc = min(MAX_WIDTH/img.size[0], MAX_HEIGHT/img.size[1])
    if sc < 1.0:
        img = img.resize((int(sc*img.size[0]+0.5), int(sc*img.size[1]+0.5)))

    img.save(output_file, format="jpeg", optimize=True, quality=75, progressive=True

