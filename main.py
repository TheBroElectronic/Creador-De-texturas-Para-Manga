from PIL import Image
import os


def Resize(img, n):
    # calculate the size Function
    x, y = img.size
    width = int(x * n / 100)
    height = int(y * n / 100)
    dim = (width, height)
    return dim


arr = os.listdir('CarpetaImg')
imgBase = Image.open('Base/base.png')
Image1copy = imgBase.copy()
Image2 = "nada"
Image3 = "nada"
num = 0

for i in arr:
    if Image2 == 'nada':
        Image2 = Image.open('CarpetaImg/' + i)
        x, y = Image2.size
        if x > 831:
            Image3 = Image2.crop((830, 0, x, y))
            Image2 = Image2.crop((0, 0, 830, y))

    elif Image3 == 'nada':
        Image3 = Image.open('CarpetaImg/' + i)
        x, y = Image3.size
        if x > 831:
            Imagea = Image3.resize(Resize(Image3, 50))
            # paste image2 into the imgages
            Image1copy = imgBase.copy()
            Image1copy.paste(Imagea.copy(), (0, 0))
            # save
            Image1copy.save('pasted' + str(num) + 'a.png')
            Image3 = Image.open('Base/nxt.jpg')

    if (Image2 != 'nada' and Image3 != 'nada') or num >= int(len(arr) / 2):
        if num >= int(len(arr) / 2):
            Image3 = Image.open('Base/end.jpg')
        print(num)
        ###SAVE###
        Image2 = Image2.resize(Resize(Image2, 47))
        Image3 = Image3.resize(Resize(Image3, 47))
        # paste image2 and 3 into the imgages
        Image1copy.paste(Image3.copy(), (0, 0))
        Image1copy.paste(Image2.copy(), (390, 0))
        # save
        Image1copy.save('pasted' + str(num) + '.png')
        ##########
        Image3 = "nada"
        Image2 = "nada"
        num = num + 1
