#!/usr/bin/python3
#link zur Challenge: https://www.floriandalwigk.de/die-gem%C3%A4lde-von-r-udolf-und-s-klaus/

from PIL import Image, ImageChops
im1 = Image.open('image.png').convert("1")
im2 = Image.open('image2.png').convert("1")

result = ImageChops.logical_xor(im1,im2)
result.save('result.png')

#aus einer enfernung von ca. 30cm oder mehr, klappt das einscannen des qr codes relativ gut.
#falls der qr code trotzdem nicht richtig erkannt wird, 
#einfach mit Paint oder ähnlichen Professionellen Tools nachbearbeiten

