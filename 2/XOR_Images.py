#!/usr/bin/python3
import numpy as np
from PIL import Image, ImageChops, ImageOps
im1 = Image.open('image.png').convert("1")
im2 = Image.open('image2.png').convert("1")

result = ImageChops.logical_xor(im1,im2)
result.show()
result.save('result.png')

