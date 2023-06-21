#!/bin/python
from PIL import Image, ImageDraw, ImageFont
img = Image.new(mode="RGB",size=(96,48),color=(0,43,89))
font = ImageFont.load("tabule-9.pil")
d=ImageDraw.Draw(img)
d.text((0,0),"BOHUMÍN",font=font,fill=(255,255,255))
d.text((0,10),"Benesov",font=font,fill=(255,255,0))
img.save("img.png")