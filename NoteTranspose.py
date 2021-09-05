

notes_height= {'E1' : 0,'F1':1,'G1':2,'A1':3, 'B1':4,  'C2':5,  'D2':6,
               'E2':7,  'F2':8,'G2':9,'A2':10,'B2':11, 'C3':12, 'D3':13,
               'E3':14, 'F3':15,'G3':16,'A3':17, 'B3':18, 'C4':19, 'D4':20,
               'E4':21, 'F4':22, 'G4':23,'A4':24,'B4':25, 'C5':26, 'D5':27,
               'E5':28, 'F5':29,'G5':30, 'A5':31, 'B5':32, 'C6':33, 'D6':34,
               'E6':35, 'F6':36,'G6':37,'A6':38,'B6':39 ,'C7':40,'D7':41,
               'E7':42, 'F7':43,'G7':44,'A7':45, 'B7':46}

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
                            index = notes_height[chord[2]]
                            new_index = int(index) + 1
                            chord[2] = list(notes_height.keys())[new_index]
                    else:
                        if(chord[3] == False):
                            if(str(chord[2])[0] !='F' and str(chord[2])[0] !='C' ):
                                chord[3] = True
                            else:
                                chord[3] = False
                            index = notes_height[chord[2]]
                            new_index = int(index) - 1
                            chord[2] = list(notes_height.keys())[new_index]
                        else:
                            chord[3] = False

            chord = tuple(chord)
            new_staff.append(chord)
        staff_type[j] = new_staff


