import ChordType
def initStaff(lines):
    line_staff = []
    staffs = []
    distance_staff = abs(lines[5] - lines[4])
    for i in range(len(lines)):
        countLine = i+1
        if(countLine%5==0):
            y_begin = lines[countLine-5]-distance_staff/2
            y_end = lines[i]+distance_staff/2

            line_staff.append(lines[i])
            lines_copy = line_staff.copy()
            staff = ChordType.Staff(y_begin,y_end,lines_copy)
            staffs.append(staff)

            line_staff.clear()
        else:
            line_staff.append(lines[i])
    return staffs

def groupNoteToStaff(chords, staffs, threshhold=5):
    for k in range(len(staffs)):
        staff = []
        for chord in chords:
            anchorPoint = tuple(map(lambda i, j: (i + j)/2, chord.pt1, chord.pt2))
            if(anchorPoint[1]>=staffs[k].begin_y-threshhold and anchorPoint[1]<=staffs[k].end_y+threshhold):
                staff.append(chord)
        staff.sort(key=lambda chord: chord.pt1[0], reverse=False)
        for i in range(len(staff)):
            print(k, " - ",staff[i].type)
        staffs[k].appendChord(staff)

def groupSymbolToStaff(symbols, staffs, threshhold=5):
    for k in range(len(staffs)):
        staff = staffs[k].symbols
        for symbol in symbols:
            anchorPoint = tuple(map(lambda i, j: (i + j)/2, symbol.pt1, symbol.pt2))
            if(anchorPoint[1]>=staffs[k].begin_y-threshhold and anchorPoint[1]<=staffs[k].end_y+threshhold):
                staff.append(symbol)
        staff.sort(key=lambda symbol: symbol.pt1[0], reverse=False)

        staffs[k].appendSymbol(staff)

