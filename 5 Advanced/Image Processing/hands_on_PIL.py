#HANDS-ON PIL (Python Image Library, aka pillow)
from PIL import Image, ImageDraw, ImageFont

#create a new image
size = 500,300 #w,h
bg_color = 242,247,151
canvas = Image.new('RGB', size, bg_color)

#get the drawing pen for the canvas
pen = ImageDraw.Draw(canvas)

#dimension
dim = (50,50), (450,250) #x1y1, x2y2
dim2 = (450,50), (50, 250)
#color
fg_color = 126,0,31
fill_color= 255,200,200

#draw 2 lines
#pen.line(xy=dim, fill=fg_color, width=10)
#pen.line(xy=dim2, fill=fg_color, width=10)

#draw an arc
#pen.arc(xy=dim, start= 30, end=300, fill=fg_color, width=5)

#draw a rectangle
#pen.rectangle(xy=dim, fill=fill_color, outline=fg_color, width=5)

#draw an ellipse
#pen.ellipse(xy=dim, fill=None, outline= fg_color, width=5)

#draw a chord
#pen.chord(xy=dim, start= 30, end= 300, fill=fill_color, outline=fg_color, width=5)

#draw a pieslice
#pen.pieslice(xy=dim,start=30, end=300, fill=fill_color, outline=fg_color, width=5)

#lets write at the center of the canvas
fnt = ImageFont.truetype('c:/windows/fonts/arial.ttf', size=40)
#data = 'Computer'
#reqd_size = pen.textsize(text=data, font=fnt)
#pen.text(xy=((size[0]-reqd_size[0])/2, (size[1]- reqd_size[1])/2), text=data, fill=fg_color, font=fnt)

data = '''Python
Image
Library'''
reqd_size = pen.multiline_textsize(text=data, font=fnt)
pen.text(xy=((size[0]-reqd_size[0])/2, (size[1]- reqd_size[1])/2), text=data, fill=fg_color, font=fnt)


#save the canvas image
canvas.save('d:/images/pil_lesson.jpg')
