#!/usr/bin/python3
import numpy as np
from PIL import Image, ImageChops, ImageOps
im2 = ImageOps.grayscale(Image.open('image.png')).convert("1")
im1 = ImageOps.grayscale(Image.open('image2.png')).convert("1")

result = ImageChops.logical_xor(im1,im2)
result.show()
result.save('result.png')

