import cv2
def getCombinedType(staffs,img):

    # 2 cases: Single Open in 5 type of double staff.

    for i in range(10):
        staff1 = staffs[i]
        StaffSymbol=[]
        StaffChord = []

        for i in range(len(staff1.chords)):
            StaffChord.append(staff1.chords[i])
        for i in range(len(staff1.symbols)):
            StaffSymbol.append(staff1.symbols[i])


        singleOpen = getArrayType(StaffSymbol,3,2)
        singleClose = getArrayType(StaffSymbol, 3, 1)
        doubleOpen = getArrayType(StaffSymbol,2,2)

        # 2 cases : Double Open
        doubleOpen = getArrayType(StaffSymbol,2,2)
        doubleClose = getArrayType(StaffSymbol,2,1)
        singleOpen = getArrayType(StaffSymbol,3,2)

        black_chord = getArrayType(StaffChord,1,None)

        for i in range(len(singleOpen)):
            chords,result_close = findCoupleFromOpen(singleOpen[i],singleClose,doubleOpen, black_chord)
            cv2.circle(img,singleOpen[i].pt1,radius=4,color=(0,255,255), thickness=-1) #yellow
            cv2.circle(img, result_close.pt2, radius=4, color=(0,0,255), thickness=-1) #red
            for j in range(len(chords)):
                cv2.circle(img, chords[j].pt1, radius=4, color=(204,0,102), thickness=-1) #purple

        for i in range(len(doubleOpen)):
            chords,result_close = findCoupleFromOpen(doubleOpen[i],doubleClose,singleOpen, black_chord)
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

def findCoupleFromOpen(open, array1, array2,black_chord):
    closes=[]
    for i in range(len(array1)):
        closes.append(array1[i])

    for i in range(len(array2)):
        closes.append(array2[i])

    count =0
    y = open.pt1[1]
    chords = []
    flag=True
    while flag:
        x = open.pt1[0]+count
        for i in range(len(black_chord)):
            for j in range(len(closes)):
                anchor_blackChordX = int ((black_chord[i].pt1[0] + black_chord[i].pt2[0])/2)
                if(x== anchor_blackChordX):
                    chords.append(black_chord[i])
                if(x==closes[j].pt2[0]):
                    flag=False
                    result_close = closes[j]
                    break
        count+=1

    return chords, result_close