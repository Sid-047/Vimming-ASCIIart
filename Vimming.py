import time
import numpy
from tkinter import *
from PIL import Image

s_=' '
grayScale="@$#&%*+=:^;~-.{}".format(s_)

img=Image.open(loc).convert('L')
ar=numpy.array(img)
pic_w,pic_h=ar.shape
avg_data=numpy.average(ar.reshape(pic_w,pic_h))
types=[80,150,250,pic_w]
imgrayScaleet=[]
T_type=0
cols_w=0

if cols>pic_w:
    cols=pic_w
    cols_w+=1
    types.pop()
if cols_w<=1:
    scale=0.47
    width=pic_w/cols
    height=width/scale
    rows=int(pic_h/height)
    imgList=[]
    for i in range(rows):
        y=int(i*height)
        y_=int((i+1)*height)
        imgList.append("")
        Val=""
        for j in range(cols):
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
            imgList[i]=Val
    imgData=''.join(imgList)
    T_Col2=time.time()
    chrC=rows*cols
    T_type=T_Col2-T_Col1
    print("Resolution Type: ",cols," Done!")
    print(">No. Of Characters: ", chrC)
    print("Execution time: ",T_type,"Secs\n")
    
print("Time Consumed: ",Doc_t,"Secs\n")