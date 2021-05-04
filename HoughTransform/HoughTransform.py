import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("line.jpg")
print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

secondary_kernel=np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]],dtype=np.uint8 )
ret,thresh1 = cv2.threshold(gray,200,255,cv2.ADAPTIVE_THRESH_MEAN_C)
kernel = np.array([[0,0,0],[1,1,1],[0,0,0]],dtype=np.uint8)
dilate = cv2.dilate(thresh1,kernel,iterations=60)

cv2.imshow("threshhold",thresh1)

canny = cv2.Canny(dilate,50,150)
print("canny",canny.shape)
ret,f = cv2.threshold(dilate,200,255,cv2.THRESH_BINARY_INV)
cv2.imshow('dreet', f)
check=[f==thresh1]
np.savetxt("HUY1.csv",f,delimiter=",",fmt="%.3f")

lines = cv2.HoughLines(canny,1,np.pi/2,200)
print(lines.shape)

for i in range(lines.shape[0]):
    for rho,theta in lines[i]:
        a = (np.cos(theta))
        a = a.astype("float64")
        b = (np.sin(theta))
        b = b.astype("float64")
        x0 = a*rho
        y0 = b*rho
        x1 = (x0 + 1000*(-b))
        y1 = (y0 + 1000*(a))
        x2 = (x0 - 1000*(-b))
        y2 = (y0 - 1000*(a))
        # print(type(a),type(b),type(x0),type(y0),type(x1),type(y1),type(x2),type(y2))
        print(int(round(y1,0)),int(round(y2,0)))
        cv2.line(img, (int(round(x1,0)), int(round(y1,0))), (int(round(x2,0)), int(round(y2,0))), (255, 255, 0), 1)
        #cv2.line(img,(x1,y1-1+3),(x2,y2-1+3),(255,255,0),1)


cv2.imshow("img",img)
cv2.imshow("canny",canny)

cv2.waitKey(0)
