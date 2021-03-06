#Captcha
from PIL import Image, ImageDraw, ImageFont
import random
def getCaptchaText(n= 5):
	digits = [str(x) for x in range(10)]
	small_case = [chr(x) for x in range(97,123)]
	upper_case = [chr(x) for x in range(65,91)]
	all = [small_case, upper_case, digits]

	captcha = ''
	for x in range(n):
		captcha = captcha + random.choice(all[x % len(all)])

	return captcha


#load the captcha_background
canvas = Image.open('d:/images/captcha_background.png')
size = canvas.size #w,h

#get the drawing pen for the canvas
pen = ImageDraw.Draw(canvas)

#font to write
fnt = ImageFont.truetype('c:/windows/fonts/arial.ttf', size=40)
#captcha
data = getCaptchaText()
#its reqd size
reqd_size = pen.textsize(text=data, font=fnt)

#color
fg_color = 126,0,31

#lets write at the center of the canvas
pen.text(xy=((size[0]-reqd_size[0])/2, (size[1]- reqd_size[1])/2), text=data, fill=fg_color, font=fnt)

#save the canvas image
canvas.save('d:/images/new_captcha.png')
