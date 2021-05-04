import numpy as np

def Non_maxSuppresion(pt_features_min, pt_features_max, proc):
    box = np.zeros(shape=(len(pt_features_min),4))
    for i in range(len(pt_features_min)):
        arr = np.zeros(shape=4, dtype=np.int)
        arr[0] = pt_features_min[i][0]
        arr[1] = pt_features_min[i][1]
        arr[2] = pt_features_max[i][0]
        arr[3] = pt_features_max[i][1]

        box[i]=arr

    result_index = np.empty(shape=(0))
    delete_index = np.empty(shape=(0))
    print(len(box))
    while(len(result_index) + len(delete_index) <len(box)):
        indexMax = np.argmax(proc)
        result_index = np.append(result_index,indexMax)
        proc[indexMax] = 0
        for x in range(0,len(box)):
            for y in range(len(result_index)):
                if(x!=y and not (x in delete_index)):
                    if(IOU(box[indexMax],box[x]) > 0.4):
                        delete_index= np.append(delete_index,x)


    return result_index

def IOU(box1, box2):
    # max of min pt, min of max pt
    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])
    xB = min(box1[2], box2[2])
    yB = min(box1[3], box2[3])

    intersectionArea = (xB-xA+1) * (yB-yA+1)

    box1Area = (box1[2]-box1[0] +1) * (box1[3]-box1[1] + 1)
    box2Area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    return intersectionArea/float(box1Area+box2Area - intersectionArea)

def removeArrayFrom2dArray(twodArray, index):
    for i in range(len(twodArray)):
        flag = 0
        for j in range(4):
            if(twodArray[i][j] == twodArray[index][j]):
                flag += 1
            else:
                break
        if(flag==4):
            return np.delete(twodArray,i,axis=0)


