import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image

r=np.zeros((321,700), dtype=np.uint8)
r[0:321, 0:700]=210
r[108:159, 108:159]=242
r[108:159, 165:216]=127
r[165:216, 108:159]=1
r[165:216, 165:216]=255

g=np.zeros((321,700), dtype=np.uint8)
g[0:321, 0:700]=210
g[108:159, 108:159]=80
g[108:159, 165:216]=186
g[165:216, 108:159]=164
g[165:216, 165:216]=185

b=np.zeros((321,700), dtype=np.uint8)
b[0:321, 0:700]=210
b[108:159, 108:159]=34
b[108:159, 165:216]=0
b[165:216, 108:159]=239
b[165:216, 165:216]=1

microsoft_logo=cv2.merge((b, g, r))

#font=cv2.FONT_HERSHEY_TRIPLEX
#cv2.putText(microsoft_logo, "Microsoft", (284, 164), font, 4, (112, 112, 112), 2)

image = cv2.cvtColor(microsoft_logo, cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)
draw = ImageDraw.Draw(image)
# font = ImageFont.truetype("Input/Microsoft Logo.ttf", 90)
# draw.text((240, 118), "Microsoft", fill=(115, 115, 115) , font=font)
font = ImageFont.truetype("Input/Dhyana-Bold.ttf", 80)
draw.text((240, 95), "Microsoft", fill=(115, 115, 115) , font=font)
microsoft_logo = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

cv2.imshow("", microsoft_logo)
cv2.waitKey()

cv2.imwrite("Output/microsoft_logo.jpg", microsoft_logo)