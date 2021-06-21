import os
import NMS
import os
import glob
import numpy as np
import cv2
import TemplateMatching
import ChordType



def addFeature(template,img):
    result = []
    feature = TemplateMatching.FindSelectedArea(img,template)
    template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    w,h = template.shape[::-1]
    for x,y in feature:
        result.append((w+x, h+y))
    return feature,result

def updateIndexArray(img_dir,arrayOfIndexType,pt1, pt2, removal):
    print(img_dir)
    data_path = os.path.join(img_dir, '*g')
    files = glob.glob(data_path)
    data = []
    countNumberOfPointindata = 0
    for f1 in files:
        img_feature = cv2.imread(f1)
        data.append(img_feature)

    for i in data:
        temp1, temp2 = addFeature(i, removal)
        countNumberOfPointindata += len(temp1)

        pt1 += temp1
        pt2 += temp2

    if(countNumberOfPointindata==0):
        indexOfLastElementInData= countNumberOfPointindata
    else:
        indexOfLastElementInData = countNumberOfPointindata
    # crash by 2d array of array of index type
    indexOfCurrentElementInIndexType = arrayOfIndexType[len(arrayOfIndexType) - 1]
    print("Array of Index Type",arrayOfIndexType)
    print("index current",indexOfCurrentElementInIndexType)

    if(isinstance(indexOfCurrentElementInIndexType,list)):
        index = indexOfLastElementInData + indexOfCurrentElementInIndexType[len(indexOfCurrentElementInIndexType) - 1]
        print(index)
    else:
        index = indexOfLastElementInData + indexOfCurrentElementInIndexType

    arrayOfIndexType.append(index)


def inputLabel(feature_type, color, removal, img):
    pt1 = []
    pt2 = []

    arrayOfIndexType = [0]
    ONLY_ONE_CLASS_IN_ONE_TYPE = None

    for t in range(len(feature_type.children)):
        secondary_feature = feature_type.children[t]
        if(secondary_feature.children == ONLY_ONE_CLASS_IN_ONE_TYPE):
            img_dir = "feature_laiganhonanh/" + secondary_feature.data  # Enter Directory of all images
            updateIndexArray(img_dir,arrayOfIndexType,pt1,pt2,removal)
        else:
            print(arrayOfIndexType)
            indexOfCurrentElementInIndexType = arrayOfIndexType[len(arrayOfIndexType) - 1]

            if(isinstance(indexOfCurrentElementInIndexType,list)):
                indexOfCurrentElementInIndexType = indexOfCurrentElementInIndexType[len(indexOfCurrentElementInIndexType) - 1]

            subArray = [indexOfCurrentElementInIndexType]
            for j in range(len(secondary_feature.children)):

                third_feature = secondary_feature.children[j]
                img_dir = "feature_laiganhonanh/" + secondary_feature.data +"/"+ third_feature.data
                updateIndexArray(img_dir, subArray, pt1, pt2,removal)
            print("subArray",subArray)
            arrayOfIndexType.append(subArray)

    print(arrayOfIndexType)
    nms_index = NMS.non_max_suppression_fast(pt1, pt2, 0.5)

    chords = []
    for i in range(int(len(nms_index))):
        print(nms_index[i])
        for j in range(len(arrayOfIndexType)):
            breakFlag = False
            if(isinstance(arrayOfIndexType[j],list)):
                for t in range(len(arrayOfIndexType[j])):
                    if int(nms_index[i]) < arrayOfIndexType[j][t]:
                       # cv2.rectangle(img, pt1[int(nms_index[i])], pt2[int(nms_index[i])], color[j - 1])
                        print("Point",pt1[int(nms_index[i])],pt2[int(nms_index[i])],j,t, int(nms_index[i]), arrayOfIndexType[j][t])
                        chords.append(ChordType.Chord(pt1[int(nms_index[i])],pt2[int(nms_index[i])],j,t))
                        breakFlag=True
                        break
                if (breakFlag):
                    break
            else:
                if int(nms_index[i]) < arrayOfIndexType[j]:
                    #cv2.rectangle(img, pt1[int(nms_index[i])], pt2[int(nms_index[i])], color[j-1])
                    chords.append(ChordType.Chord(pt1[int(nms_index[i])], pt2[int(nms_index[i])], j))
                    break

    return chords
