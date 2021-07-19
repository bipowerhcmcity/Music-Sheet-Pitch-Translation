import ChordType
def markPartition(staffs, verticalLines):
    for i in range(int(len(staffs)/2)):
        for j in range(len(verticalLines)):
            if(verticalLines[j][1]> staffs[i*2].begin_y and verticalLines[j][1]< staffs[i*2].end_y):
                staffs[i*2].point_part.append(verticalLines[j][0])
                staffs[i * 2 + 1].point_part.append(verticalLines[j][0])

        staffs[i * 2].point_part = removeDuplicatedElement(staffs[i * 2].point_part)
        staffs[i * 2+1].point_part = removeDuplicatedElement(staffs[i * 2 + 1].point_part)
        print("Staff Part: ",staffs[i*2].point_part)

def groupNoteToPartition(staffs):
    groupNote = []
    for t in range(len(staffs)):
        group = []
        count = 0
        temparr = []
        for i in range(len(staffs[t].chords)):
            if staffs[t].chords[i].pt1[0] < staffs[t].point_part[count]:
                temparr.append(staffs[t].chords[i])
            else:
                count+=1
                group.append(temparr)

                temparr = [] # use clear() == group will be also cleared.
                temparr.append(staffs[t].chords[i])

        group.append(temparr) # for the last temp arr
        groupNote.append(group)

        # checkBeat and the distance X between 2 first notes:
        # 1) distance:
        beatDictionary = {
            1: 1,
            2: 1 / 2,
            3: 1 / 4,
            4: 2,
            7: 1 / 2
        }
        for i in range(len(group)):
            print("Staff: ",t)
            print(checkTotalBeat(group[i],beatDictionary))

def centerPoint(pt1, pt2):
    return (pt1+pt2)/2

def checkTotalBeat(group, beatDictionary):
    sum = 0
    eleminateMultipleNotes(group)
    for i in range(len(group)):
        # print("Type=",group[i].type)
        sum += beatDictionary[group[i].type]
        if (group[i].dot == True):
            print("dot here...")
            sum += beatDictionary[group[i].type] * 1 / 2
    return sum

def eleminateMultipleNotes(group):
    distance = []
    for i in range(len(group)-1):
        distance.append(abs(group[i].pt1[0]-group[i+1].pt1[0]))

    count = 0
    threshhold = 5 # the very small distance is the multiple notes.
    for i in range(len(distance)):
        if(distance[i] < threshhold):
            group[i-count].updateMultiple(True)
            group[i-count+1].dot = True # the next to chord is also has dot
            group.pop(i-count)
            count+=1

def removeDuplicatedElement(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    res.sort()
    return res