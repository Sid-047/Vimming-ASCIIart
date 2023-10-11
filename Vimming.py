import time
import numpy
from tkinter import *
from PIL import Image
from tkinter import filedialog

s_=' '
grayScale="@$#&%*+=:^;~-.{}".format(s_)

tk = Tk()
inImg = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff")])
img=Image.open(inImg).convert('L')
ar=numpy.array(img)
pic_w,pic_h=ar.shape
avg_data=numpy.average(ar)
imgList = []
scale = 0.47
dimType = 80
width=pic_w/dimType
height=width/scale
rows=int(pic_h/height)
for i in range(rows):
    y=int(i*height)
    y_=int((i+1)*height)
    Val=""
    for j in range(dimType):
        x=int(j*width)
        x_=int((j+1)*width)
        img_=img.crop((x,y,x_,y_))
        ar=numpy.array(img_)
        w,h=ar.shape
        avg_data=numpy.average(ar.reshape(w,h))
        grayScaleVal=grayScale[int((avg_data*14)/255)]
        Val+=grayScaleVal
    Val='\n'+Val
    if len(set(list(Val)))==2:
        pass
    else:
        imgList.append(Val)

imgData=''.join(imgList)
print(imgData)