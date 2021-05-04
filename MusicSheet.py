import numpy as np
import cv2

import HoughTransform.RunLengthEncoding
import TemplateMatching
import NMS
import os
import glob
img_dir = "feature" # Enter Directory of all images
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
for f1 in files:
    img = cv2.imread(f1)
    data.append(img)
img = cv2.imread("sheet.jpg")
clef_sol = cv2.imread("chord.jpg")
lines = HoughTransform.RunLengthEncoding.DrawLine(False,img)

pt1 = []
pt2 = []
confidences = []
def addFeature(template):
    result = []
    feature, confidence = TemplateMatching.FindSelectedArea(img,template,(177,255,177),"black_chord")
    template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    w,h = template.shape[::-1]
    for x,y in feature:
        result.append((w+x, h+y))
    return feature,result, confidence

for i in data:
    temp1, temp2, confidence = addFeature(i)
    pt1 += temp1
    pt2 += temp2
    confidences += confidence

# temp1, temp2,confidence = addFeature(clef_sol)
# pt1+=temp1
# pt2+=temp2
# confidences+= confidence



pt_clef1, pt_clef2, clef_confidence = addFeature(clef_sol)
h_clef = cv2.cvtColor(clef_sol,cv2.COLOR_BGR2GRAY)
h_clef = clef_sol.shape[0]

nms_index = NMS.Non_maxSuppresion(pt1,pt2, confidences)
for i in range(int(len(nms_index))):
    cv2.rectangle(img,pt1[int(nms_index[i])],pt2[int(nms_index[i])],(177,255,177))

for pt in pt_clef1:
    for i in range(pt[1],h_clef+pt[1],1):
        for line in lines:
            if(i==line):
                cv2.line(img, (-1000, line), (1000, line), (127, 127, 127), 1)

cv2.imshow("IMG",img)
cv2.waitKey(0)