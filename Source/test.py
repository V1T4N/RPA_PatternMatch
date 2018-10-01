import os
import cv2
from PIL import ImageGrab
#import numpy as np
#from matplotlib import pyplot as plt

scs = ImageGrab.grab()
scs.save("Source/screenshot.png")


img = cv2.imread('Source/screenshot.PNG',0)
#img2 = img.copy()
template = cv2.imread('Source/temp1.PNG',0)
template2 = cv2.imread('Source/temp2.PNG',0)

w, h = template.shape[::-1]

w2, h2 = template2.shape[::-1]


#img = img2.copy()

#Apply Template Maching for "Hypogram" button
##################################################################

res = cv2.matchTemplate(img,template,cv2.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

#Apply Template Maching for "Report" button
##################################################################
res2 = cv2.matchTemplate(img,template2,cv2.TM_CCORR_NORMED)
min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)

top_left2 = max_loc2
bottom_right2 = (top_left2[0] + w2, top_left2[1] + h2)
##################################################################


#plot square
cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)

cv2.rectangle(img,top_left2, bottom_right2, (0,0,255), 2)



#plt.subplot(121),plt.imshow(res,cmap = 'gray')
#plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(img,cmap = 'gray')
#plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

#plt.show()

path_w = 'Source/pos.txt'


with open(path_w, mode='w') as f:
    f.write(str(top_left[0] + 30))
    f.write(",")
    f.write(str(top_left[1] + 5))
    f.write("\n")
    f.write(str(top_left2[0] + 30))
    f.write(",")
    f.write(str(top_left2[1] + 5))
print(top_left)
print(top_left2)