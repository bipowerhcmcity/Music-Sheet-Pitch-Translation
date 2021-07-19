import cv2
import ChordType
def getCombinedType(staffs,img):
    # 2 cases: Single Open in 5 type of double staff.
    for z in range(10):
        staff1 = staffs[z]
        StaffSymbol=[]
        StaffChord = []

        result_chords = []

        for i in range(len(staff1.chords)):
            StaffChord.append(staff1.chords[i])
        for i in range(len(staff1.symbols)):
            StaffSymbol.append(staff1.symbols[i])

        #
        sharp = getArrayType(StaffSymbol,5,None)

        rest = []
        rest += getArrayType(StaffSymbol,7,None)
        # will have more rest here in future....

        # and dot rest: special rest
        dotRest = getArrayType(StaffSymbol,8,None)
        print("Len of dot rest: ",len(dotRest))



        singleOpen = getArrayType(StaffSymbol,3,2)
        singleClose = getArrayType(StaffSymbol, 3, 1)
        doubleOpen = getArrayType(StaffSymbol,2,2)

        # 2 cases : Double Open
        doubleOpen = getArrayType(StaffSymbol,2,2)
        doubleClose = getArrayType(StaffSymbol,2,1)
        singleOpen = getArrayType(StaffSymbol,3,2)


        black_chord = getArrayType(StaffChord,1,None)
        white_chord = getArrayType(StaffChord,4,None)


        # update sharp to chords:

        for i in range(len(sharp)):
            chordBlack = findSingleSymbolInChord(black_chord,sharp[i],1,20)
            chordWhite = findSingleSymbolInChord(white_chord, sharp[i], 1,20)
            # print(chord)
            if(isinstance(chordBlack,ChordType.Chord)):
                chordBlack.sharp = True
            if (isinstance(chordWhite, ChordType.Chord)):
                chordWhite.sharp = True

        for i in range(len(dotRest)):
            chordBlack = findSingleSymbolInChord(black_chord, dotRest[i], -1,100)
            chordWhite = findSingleSymbolInChord(white_chord, dotRest[i], -1,100)
            # print(chord)
            if (isinstance(chordBlack, ChordType.Chord)):
                chordBlack.dot = True
            if (isinstance(chordWhite, ChordType.Chord)):
                chordWhite.dot = True

        for i in range(len(doubleOpen)):
            chords,result_close = findCoupleFromOpen(doubleOpen[i],doubleClose,singleOpen, black_chord)
            y= doubleOpen[i].pt1[1] +10
            point = (doubleOpen[i].pt1[0],y)
            removeArrayFromArray(black_chord, chords)
            cv2.circle(img,point,radius=4,color=(0,255,255), thickness=-1) #yellow
            cv2.circle(img, result_close.pt2, radius=4, color=(0,0,255), thickness=-1) #red
            for j in range(len(chords)):
                cv2.circle(img, chords[j].pt1, radius=4, color=(255,0,0), thickness=-1)  # blue
                chords[j].type = 3
                result_chords.append(chords[j])

        for i in range(len(singleOpen)):
            chords,result_close = findCoupleFromOpen(singleOpen[i],singleClose,doubleOpen, black_chord)
            removeArrayFromArray(black_chord, chords)
            cv2.circle(img,singleOpen[i].pt1,radius=4,color=(0,255,255), thickness=-1) #yellow
            cv2.circle(img, result_close.pt2, radius=4, color=(0,0,255), thickness=-1) #red
            for j in range(len(chords)):
                cv2.circle(img, chords[j].pt1, radius=4, color=(204,0,102), thickness=-1) #purple
                chords[j].type = 2
                result_chords.append(chords[j])


        if(len(black_chord) >0):
            for i in range(len(black_chord)):
                black_chord[i].type = 1
                result_chords.append(black_chord[i])

        for i in range(len(white_chord)):
            result_chords.append(white_chord[i])
        # append rest:
        for i in range(len(rest)):
            result_chords.append(rest[i])

        result_chords.sort(key=lambda chord: chord.pt1[0], reverse=False)
        staffs[z].chords = result_chords


    cv2.imwrite("fullOption.jpg",img)

def getArrayType(chordsType, type,sub_type):
    result = []

    for i in range(len(chordsType)):
        if chordsType[i].type==type and chordsType[i].sub_type == sub_type:
            result.append(chordsType[i])
    return result

def removeArrayFromArray(array1, array2):
    i = 0
    while i < len(array2):
        for j in range(len(array1)):
            if (array2[i].pt1 == array1[j].pt1 and array2[i].pt2 == array1[j].pt2):
                i = 0
                array1.pop(j)
                break
        i += 1

def removeElementFromArray(array,element):
    for j in range(len(array)):
        if(array[j].pt1 == element.pt1 and array[j].pt2 == element.pt2):
            array.pop(j)
            break

def findSingleSymbolInChord(chord, symbol, option, threshhold):
    # option 1 : find note in the right most hand side.
    # option -1 : find note in the left most hand side.

    xSymbol = int((symbol.pt1[0] + symbol.pt2[0])/2)
    count = threshhold
    while count>0:
        for i in range(len(chord)):

            xChord = int((chord[i].pt1[0] + chord[i].pt2[0]) / 2)

            if xSymbol== xChord:
                return chord[i]

                break
        xSymbol+=option
        count-=1

def findCoupleFromOpen(open, array1, array2,black_chord):
    result_close = open
    closes=[]
    for i in range(len(array1)):
        closes.append(array1[i])

    for i in range(len(array2)):
        closes.append(array2[i])

    count =0
    chords = []
    flag=True
    while flag:
        if(len(closes) == 0):
            break
        if (flag == False):
            break
        x = open.pt1[0]+count
        for i in range(len(black_chord)):
            if (flag == False):
                break
            if(len(closes) == 0):
                flag = False
                break
            anchor_blackChordX = int((black_chord[i].pt1[0] + black_chord[i].pt2[0]) / 2)
            if (x == anchor_blackChordX):
                chords.append(black_chord[i])

            for j in range(len(closes)):
                close_anchor = int (closes[j].pt2[0])


                if(x==close_anchor):
                    flag=False
                    result_close = closes[j]

                    if j<len(array1):
                        array1.pop(j)
                    break
            if (flag == False):
                break
        if (flag == False):
            break
        count+=1

    return chords, result_close