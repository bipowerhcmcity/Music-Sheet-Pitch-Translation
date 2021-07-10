

notes_height= ['E1', 'F1','G1','A1', 'B1', 'C2','D2', 'E2', 'F2','G2','A2', 'B2', 'C3', 'D3', 'E3', 'F3','G3',
                       'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4','A4','B4', 'C5', 'D5', 'E5', 'F5',
                'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6','G6','A6','B6']

def findNoteinNote_height(note):
    for i in range(len(notes_height)):
        if(note == notes_height[i]):
            return i


def transpose(staff_type,level):
    for j in range(len(staff_type)):
        staff = staff_type[j]
        new_staff = []
        for i in range(len(staff)):
            chord = list(staff[i])
            if(chord[2] == "NONE"):
                continue
            else:
                absLevel = level
                absLevel = abs(absLevel)
                for t in range(absLevel):
                    if(level >0):
                        if(chord[3] == False and str(chord[2])[0] !='E' and str(chord[2])[0] !='B' ):
                            chord[3] = True
                        else:
                            chord[3] = False
                            index = findNoteinNote_height(chord[2])
                            new_index = int(index) + 1
                            chord[2] = notes_height[new_index]
                    else:
                        if(chord[3] == False):
                            if(str(chord[2])[0] !='F' and str(chord[2])[0] !='C' ):
                                chord[3] = True
                            else:
                                chord[3] = False
                            index = findNoteinNote_height(chord[2])
                            new_index = int(index) - 1
                            chord[2] = notes_height[new_index]
                        else:
                            chord[3] = False

            chord = tuple(chord)
            new_staff.append(chord)
        staff_type[j] = new_staff


