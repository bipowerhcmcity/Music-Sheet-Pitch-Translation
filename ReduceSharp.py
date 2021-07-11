def getNonSharpNote(staffs):
    index = []
    for staff in staffs:
        subIndex = []
        j=0
        for i in range(len(staff)):
            if(staff[i][2] == "NONE"):
                j+=1
                continue
            else:
                if(staff[i][3] == False):
                    subIndex.append(i-j)
        index.append(subIndex)
    return index

def getAllNoteHasSharp(staffs, nonSharpIndex):
    arrayNote = []
    count =0
    for notes in staffs:

        for i in nonSharpIndex[count]:
            if(notes[i][3] == True):
                arrayNote.append(str(notes[i][2])[0])
                for j in range(len(arrayNote)-1):
                    if(arrayNote[-1] == arrayNote[j]):
                        arrayNote.pop(-1)
                        break
        count+=1



    return arrayNote

def IdentifySharpOrFlat(arrayNote):
    sharp = ['F','C','G','D','A']
    flat = ['A', 'D', 'G', 'C','F']

    sharpCount = 0
    flatCount = 0
    for i in range(len(arrayNote)):
        for sharp_element in sharp[:len(arrayNote)]:
            if(sharp_element == arrayNote[i]):
                sharpCount+=1
                break
        for sharp_element in flat[:len(arrayNote)]:
            if(sharp_element == arrayNote[i]):
                flatCount+=1
                break
    if(flatCount>sharpCount):
        return "flat", flatCount
    else:
        return "sharp",sharpCount

def reduceSharp(staffs, type, level):
    sharp = ['F', 'C', 'G', 'D', 'A']
    flat = ['A', 'D', 'G', 'C', 'F']
    flatReal = ['B', 'E', 'A', 'D', 'G']

    if type == "sharp":
        arr = sharp[:level]
    else:
        arr = flat[:level]

    for staff in staffs:
        for j in range(len(staff)):
            listTypeNote = list(staff[j])
            for i in range(len(arr)):
                if(str(staff[j][2])[0] == arr[i] and staff[j][3] == True ):
                    listTypeNote[3] = False
                    if(type == "flat"):
                        listTypeNote[2] = listTypeNote[2].replace(flat[i],flatReal[i])

            staff[j] = tuple(listTypeNote)



