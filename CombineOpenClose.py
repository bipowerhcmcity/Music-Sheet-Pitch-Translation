import cv2
def getCombinedType(chordsType, staffHeight,img):

    # 2 cases: Single Open
    singleOpen = getArrayType(chordsType,3,2)
    singleClose = getArrayType(chordsType, 3, 1)
    doubleOpen = getArrayType(chordsType,2,2)

    # 2 cases : Double Open
    doubleOpen = getArrayType(chordsType,2,2)
    doubleClose = getArrayType(chordsType,2,1)
    singleOpen = getArrayType(chordsType,3,2)

    black_chord = getArrayType(chordsType,1,None)

    for i in range(len(singleOpen)):
        chords,result_close = findCoupleFromOpen(singleOpen[i],singleClose,doubleOpen, black_chord,staffHeight)
        cv2.circle(img,singleOpen[i].pt1,radius=4,color=(0,255,255), thickness=-1) #yellow
        cv2.circle(img, result_close.pt2, radius=4, color=(0,0,255), thickness=-1) #red
        for j in range(len(chords)):
            cv2.circle(img, chords[j].pt1, radius=4, color=(204,0,102), thickness=-1) #purple

    for i in range(len(doubleOpen)):
        chords,result_close = findCoupleFromOpen(doubleOpen[i],doubleClose,singleOpen, black_chord,staffHeight)
        y= doubleOpen[i].pt1[1] +10
        point = (doubleOpen[i].pt1[0],y)
        cv2.circle(img,point,radius=4,color=(0,255,255), thickness=-1) #yellow
        cv2.circle(img, result_close.pt2, radius=4, color=(0,0,255), thickness=-1) #red
        for j in range(len(chords)):
            cv2.circle(img, chords[j].pt1, radius=4, color=(255,0,0), thickness=-1)  # blue


def getArrayType(chordsType, type,sub_type):
    result = []
    for i in range(len(chordsType)):
        if chordsType[i].type==type and chordsType[i].sub_type == sub_type:
            result.append(chordsType[i])
    return result

def findCoupleFromOpen(open, array1, array2,black_chord, staff_height):
    closes=[]
    for i in range(len(array1)):
        closes.append(array1[i])

    for i in range(len(array2)):
        closes.append(array2[i])
    for i in range(len(closes)):
        print(closes[i].type)

    print(closes)
    count =0
    y = open.pt1[1]
    chords = []
    flag=True
    while flag:
        x = open.pt1[0]+count
        for i in range(len(black_chord)):
            for j in range(len(closes)):
                # print("closes at ",closes[j].getInfo())
                # print("x",x)
                if(x== black_chord[i].pt1[0] and black_chord[i].pt1[1] > y-staff_height and black_chord[i].pt1[1] < y+staff_height):
                    chords.append(black_chord[i])
                if(x==closes[j].pt2[0] and closes[j].pt2[1] > y-staff_height and closes[j].pt2[1] < y+staff_height):
                    flag=False
                    result_close = closes[j]
                    break
        count+=1

    return chords, result_close