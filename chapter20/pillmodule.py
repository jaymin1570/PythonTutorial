from PIL import Image,ImageEnhance,ImageFilter
import os

# img1 = Image.open('flower.jpeg')
# img1.save('flower.pdf')
# img1.show()
# 250
# max_size= (250,250)
# img1.thumbnail(max_size)
# img1.save('flower2.jpg')
# img1.show()

# for item in os.listdir():
#     if item.endswith('.jpeg'):
#         img1=Image.open(item)
#         filename,extension= os.path.splitext(item)
#         img1.save(f'{filename}.png')


#-------color-----------
# img1 = Image.open('flower.jpeg')
# enhancer= ImageEnhance.Color(img1)
# enhancer.enhance(5).save('flower2edited.jpeg')

# 0 : blurry
# 1 : original image
# 2 : image with increased sharpness

# ----------brightness--------
# img1 = Image.open('flower.jpeg')
# enhancer= ImageEnhance.Brightness(img1)
# enhancer.enhance(4).save('flower2edited.jpeg')

# ----------contrast-------------
# img1 = Image.open('flower.jpeg')
# enhancer= ImageEnhance.Contrast(img1)
# enhancer.enhance(4).save('flower2edited.jpeg')

img1 = Image.open('flower.jpeg')
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('floweredited.jpg')