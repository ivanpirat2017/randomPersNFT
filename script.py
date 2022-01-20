from PIL import Image
import os
import random
import re

# пример как должно называться изображение body#40.png или body1#40.png
items = ['bg', 'body', 'head']# слои по возрастанию 
count = 1# количество 
height = 1000
width = 1000






def gendomarr(arr):
    newArr = []
    for item in arr:
        newArr.append(int(re.findall(r'#(\d+).', item)[0]))  
    oldArr = newArr.copy()
    newArr.sort()    
    key=oldArr.index(random.choices(newArr,weights=newArr,k=1)[0])
    return  arr[key]
        
num =0
arrPers = []
def getImgRandom(getpath):
    body = './img/'+getpath+'/'
    filePath =  gendomarr(os.listdir(body))  
    img = Image.open( open(os.path.join(body,filePath  )).name)
    arr = [img, getpath+filePath]
    return arr


def boolarr(arr, obj):
    for per in arr:
        if(per == obj):
            return False
    return True


for i in range(count):
    img = Image.new(mode="RGBA", size=(width, height))
    perspath = ''
    for item in items:
        imagrinfo = getImgRandom(item)
        imrgeItem = imagrinfo[0]
        perspath += imagrinfo[1]
        img.paste(imrgeItem, (0, 0), imrgeItem)
    if(boolarr(arrPers, perspath)):
        num =num+1
        arrPers.append(perspath)
        img.save("dist/mostr"+str(num)+".png")
    arrPers.append(perspath)
