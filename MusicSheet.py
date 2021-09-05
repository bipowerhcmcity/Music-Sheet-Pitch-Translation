import numpy as np
import cv2


import HoughTransform.RunLengthEncoding
import StaffLineRemoval
import ClassifiedTypeChord
import ChordType
import CreateStaff
import CombineOpenClose
import NotesTranslation
import NoteTranspose
import ReduceSharp
import PartitionStave
import WritingNote

#feature_type = ["black_chord","double close","double open","single close","single open","white_chord"]
color = [(0,0,255),(0,255,0),(0,255,255),(255,0,0),(204,0,102),(0,0,0)] # red, green, yellow, blue, purple, black

feature_type = ChordType.root

img = cv2.imread("sheet_4.jpg")

clef_sol = cv2.imread("chord.jpg")
lines, staff_height = HoughTransform.RunLengthEncoding.DrawLine(False,img)
removal = StaffLineRemoval.StaffLineRemoval(img)

headlines = []
for i in range(len(lines)):
    if i%5 == 0:
        headlines.append(lines[i])
print(headlines)



headlines = []
for i in range(len(lines)):
    if i%5 == 0:
        headlines.append(lines[i])
print(headlines)
staffs = CreateStaff.initStaff(lines)

print(staffs)
#
chordsType = ClassifiedTypeChord.inputLabel(feature_type,color,removal,img)
for i in range(len(chordsType)):
    if(chordsType[i].type == 4):
        cv2.circle(img, chordsType[i].pt1, radius=4, color=(0,255,0), thickness=-1) #purple
        print(chordsType[i].type,chordsType[i].sub_type," : ",chordsType[i].pt1 )



onlySharp = []
for i in range(len(chordsType)):
    if(chordsType[i].type ==5):
        onlySharp.append(chordsType[i])

print("Only Sharp: ",onlySharp)

onlyVerticalLine = []
for i in range(len(chordsType)):
    if(chordsType[i].type ==6):
        centerX= int((chordsType[i].pt1[0] + chordsType[i].pt2[0])/2)
        pt = tuple([centerX,chordsType[i].pt1[1]])
        onlyVerticalLine.append(pt)

print("Only Vertical Line: ",onlyVerticalLine)
PartitionStave.markPartition(staffs,onlyVerticalLine)


onlyChord = []
for i in range(len(chordsType)):
    if(chordsType[i].type==1 or chordsType[i].type==4 ):
        onlyChord.append(chordsType[i])

onlySymbol = []
for i in range(len(chordsType)):
    if(chordsType[i].type==2 or chordsType[i].type==3 ):
        onlySymbol.append(chordsType[i])

eighthRest = []
for i in range(len(chordsType)):
    if (chordsType[i].type == 7):
        eighthRest.append(chordsType[i])
print("eight Rest: ",eighthRest)

fullRest = []
for i in range(len(chordsType)):
    if (chordsType[i].type == 9):
        fullRest.append(chordsType[i])
print("full Rest: ",fullRest)

dotRest = []
for i in range(len(chordsType)):
    if (chordsType[i].type == 8):
        dotRest.append(chordsType[i])
print("dot Rest: ", dotRest)
#
#
CreateStaff.groupNoteToStaff(onlyChord,staffs)
CreateStaff.groupSymbolToStaff(onlySymbol,staffs)
CreateStaff.groupSymbolToStaff(onlySharp,staffs)
CreateStaff.groupSymbolToStaff(eighthRest,staffs)
CreateStaff.groupSymbolToStaff(fullRest,staffs)
CreateStaff.groupSymbolToStaff(dotRest,staffs)
#
# #
# #
# # # print("Sucessfully write result....")
# # #
CombineOpenClose.getCombinedType(staffs, img)
PartitionStave.groupNoteToPartition(staffs)

# #for i in range(len(staffs)):
# #    for j in range(len(staffs[i].chords)):
# #        print("Staff",i," chord ",j,staffs[i].chords[j].sharp)
#
#
#
data = NotesTranslation.Pos2Pos(staffs)
data = NotesTranslation.ReOrderedStaffs(data)
# to add more parameter to result: add to relesedata, reorder, post2Height, pos2Note

unprocessed_data, data = NotesTranslation.Pos2Height(data, headlines, abs(lines[0] - lines[1]))


MAIN, BASS = NotesTranslation.SeparateMainNSUB(data)
MAIN = NotesTranslation.Pos2Note(MAIN, "MAIN")
BASS = NotesTranslation.Pos2Note(BASS, "BASS")

for i,j in zip(MAIN, BASS):
    result = []
    for x in range(len(i)):
        result.append(i[x][2])
    print(result)
    result = []
    for x in range(len(j)):
        result.append(i[x][2])
    print(result)

nonSharpIndex = ReduceSharp.getNonSharpNote(MAIN+BASS)

NoteTranspose.transpose(MAIN, 3)
NoteTranspose.transpose(BASS, 3)


for i,j in zip(MAIN, BASS):
   print(i)
   print(j)
#
# file_handle_1 = open('note_type.csv', 'w')
# file_handle_2 = open('note.csv', 'w')
# for i,j in zip(MAIN, BASS):
#     file_handle_1.write(','.join([str(note_main[0]) for note_main in i]) + '\n')
#     file_handle_1.write(','.join([str(note_bass[0]) for note_bass in j]) + '\n')
#     file_handle_2.write(','.join([str(note_main[2]) for note_main in i]) + '\n')
#     file_handle_2.write(','.join([str(note_bass[2]) for note_bass in j]) + '\n')
# file_handle_1.close()
# file_handle_2.close()


# Reduce Sharp: just reduce the permanent sharp
allNoteHasSharp = ReduceSharp.getAllNoteHasSharp(MAIN+BASS, nonSharpIndex)
print("Sharp are in note", allNoteHasSharp)
symbol, level = ReduceSharp.IdentifySharpOrFlat(allNoteHasSharp)
if(symbol==-1):
    ReduceSharp.changeSharpToFlat(MAIN+BASS,level)

allMajorChord = ["C","G","D","A","E","B","Ab","Eb","Bb","F"]

print(symbol, level)
MajorChord = allMajorChord[level*symbol]
print("Major chord: ",MajorChord)
for i,j in zip(MAIN, BASS):
   print(i)
   print(j)

print("Writing to pdf...")
WritingNote.start(MajorChord,MAIN,BASS,symbol) # symbol for classify sharp or flat
print(MAIN+BASS)

cv2.imwrite("allresult.jpg",img)
cv2.imshow("All result",img)
cv2.waitKey(0)