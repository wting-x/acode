from PIL import Image
from PIL import ImageEnhance
# 原始图像
image = Image.open('image.jpg')
image.show()

#色度增强
enh_col = ImageEnhance.Color(image)
color = 1.5
image_colored = enh_col.enhance(color)
image_colored.show()

#对比度增强
enh_con = ImageEnhance.Contrast(image_colored)
contrast = 1.3
image_contrasted = enh_con.enhance(contrast)
image_contrasted.show()

#亮度增强
enh_bri = ImageEnhance.Brightness(image_contrasted)
brightness = 1.3
image_brightened = enh_bri.enhance(brightness)
image_brightened.show()

#锐度增强
enh_sha = ImageEnhance.Sharpness(image_brightened)
sharpness = 3.0
image_sharped = enh_sha.enhance(sharpness)
image_sharped.show()

image_sharped.save("newImage.jpg")