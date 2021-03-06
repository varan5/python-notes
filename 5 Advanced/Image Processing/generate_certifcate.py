#Generate Certificate
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
def makeCertificate(bkgrnd_file, trgt_file, name, course):
	#load the captcha background in memory
	img = Image.open(bkgrnd_file)
	if img is None:
		print(bkgrnd_file, 'not found')
		return

	#get the image draw/write object
	pen = ImageDraw.Draw(img)
	#decide over the font
	fnt = ImageFont.truetype(font='c:/windows/fonts/coopbl.ttf', size=40)
	#then the fore_color
	fg_color = (136, 0, 21)  # (r,g,b)
	#generate captcha text

	#see how much space name needs
	reqd_size = pen.textsize(text=name, font=fnt)
	#lets write
	xy = 760- reqd_size[0]/2, 645- reqd_size[1]
	pen.text(xy = xy,text=name, font=fnt, fill=fg_color)

	# see how much space course needs
	reqd_size = pen.textsize(text=course, font=fnt)
	# lets write
	xy = 760 - reqd_size[0] / 2, 815 - reqd_size[1]
	pen.text(xy=xy, text=course, font=fnt, fill=fg_color)

	#date
	now  = datetime.now()
	#print(now)
	#print(now.strftime('%a %A'))
	#print(now.strftime('%b %B'))
	#print(now.strftime('%d/%m/%Y'))
	#print(now.strftime('%H:%M:%S'))

	# lets write day of the month (1-31)
	day = now.strftime("%d")
	pen.text(xy=(310,900), text=day, font=fnt, fill=fg_color)

	# lets write month of the year (JAN-FEB)
	mth = now.strftime("%b")
	pen.text(xy=(465, 900), text=mth, font=fnt, fill=fg_color)

	# lets write 4 digit  year (2020)
	yr = now.strftime("%Y")
	pen.text(xy=(590, 900), text=yr, font=fnt, fill=fg_color)

	#save it
	img.save(trgt_file)

makeCertificate('d:/images/blank.png', 'd:/images/cert_new.png', 'Vikas Kumar','Python Image Library')