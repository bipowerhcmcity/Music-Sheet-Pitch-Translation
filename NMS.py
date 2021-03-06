# import numpy as np
#
# def Non_maxSuppresion(pt_features_min, pt_features_max, proc):
#     box = np.zeros(shape=(len(pt_features_min),4))
#     for i in range(len(pt_features_min)):
#         arr = np.zeros(shape=4, dtype=np.int)
#         arr[0] = pt_features_min[i][0]
#         arr[1] = pt_features_min[i][1]
#         arr[2] = pt_features_max[i][0]
#         arr[3] = pt_features_max[i][1]
#
#         box[i]=arr
#
#     result_index = np.empty(shape=(0))
#     delete_index = np.empty(shape=(0))
#     print(len(box))
#     while(len(result_index) + len(delete_index) <len(box)):
#         indexMax = np.argmax(proc)
#         result_index = np.append(result_index,indexMax)
#         proc[indexMax] = 0
#         for x in range(0,len(box)):
#             for y in range(len(result_index)):
#                 if(x!=y and not (x in delete_index)):
#                     if(IOU(box[indexMax],box[x]) > 0.4):
#                         delete_index= np.append(delete_index,x)
#
#     print("Before deleting: ",result_index)
#     result_index = result_index[~np.isin(result_index, delete_index)]
#     print("After deleting: ", result_index)
#
#     return result_index
#
# def IOU(box1, box2):
#     # max of min pt, min of max pt
#     xA = max(box1[0], box2[0])
#     yA = max(box1[1], box2[1])
#     xB = min(box1[2], box2[2])
#     yB = min(box1[3], box2[3])
#
#     intersectionArea = (xB-xA+1) * (yB-yA+1)
#
#     box1Area = (box1[2]-box1[0] +1) * (box1[3]-box1[1] + 1)
#     box2Area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
#
#     return intersectionArea/float(box1Area+box2Area - intersectionArea)
# #
# # def removeArrayFrom2dArray(twodArray, index):
# #     for i in range(len(twodArray)):
# #         flag = 0
# #         for j in range(4):
# #             if(twodArray[i][j] == twodArray[index][j]):
# #                 flag += 1
# #             else:
# #                 break
# #         if(flag==4):
# #             return np.delete(twodArray,i,axis=0)

# import the necessary packages
import numpy as np
# Malisiewicz et al.
def non_max_suppression_fast(pt1, pt2, overlapThresh):
    pick = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i in range(len(pt1)):
        x1.append(pt1[i][0])
        y1.append(pt1[i][1])
        x2.append(pt2[i][0])
        y2.append(pt2[i][1])


    print(x1)
    x1=np.array(x1)
    x2 = np.array(x2)
    y1 = np.array(y1)
    y2 = np.array(y2)

    # compute the area of the bounding boxes and sort the bounding
    # boxes by the bottom-right y-coordinate of the bounding box
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)
    # keep looping while some indexes still remain in the indexes
    # list
    while len(idxs) > 0:
        # grab the last index in the indexes list and add the
        # index value to the list of picked indexes
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        # find the largest (x, y) coordinates for the start of
        # the bounding box and the smallest (x, y) coordinates
        # for the end of the bounding box
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])
        # compute the width and height of the bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        # compute the ratio of overlap
        overlap = (w * h) / area[idxs[:last]]
        # delete all indexes from the index list that have
        idxs = np.delete(idxs, np.concatenate(([last],
            np.where(overlap > overlapThresh)[0])))
        # return only the bounding boxes that were picked using the
        # integer data type
    return pick
