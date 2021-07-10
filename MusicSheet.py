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

staffs = CreateStaff.initStaff(lines)

print(staffs)
#
chordsType = ClassifiedTypeChord.inputLabel(feature_type,color,removal,img)
for i in range(len(chordsType)):
    print(chordsType[i].type,chordsType[i].sub_type," : ",chordsType[i].pt1 )

onlySharp = []
for i in range(len(chordsType)):
    if(chordsType[i].type ==5):
        onlySharp.append(chordsType[i])

print("Only Sharp: ",onlySharp)

onlyChord = []
for i in range(len(chordsType)):
    if(chordsType[i].type==1 or chordsType[i].type==4 ):
        onlyChord.append(chordsType[i])

onlySymbol = []
for i in range(len(chordsType)):
    if(chordsType[i].type==2 or chordsType[i].type==3 ):
        onlySymbol.append(chordsType[i])
#
#
CreateStaff.groupNoteToStaff(onlyChord,staffs)
CreateStaff.groupSymbolToStaff(onlySymbol,staffs)
CreateStaff.groupSymbolToStaff(onlySharp,staffs)

#
#
# # print("Sucessfully write result....")
# #
CombineOpenClose.getCombinedType(staffs, img)

data = NotesTranslation.Pos2Pos(staffs)
data = NotesTranslation.ReOrderedStaffs(data)



unprocessed_data, data = NotesTranslation.Pos2Height(data, headlines, abs(lines[0] - lines[1]))


MAIN, BASS = NotesTranslation.SeparateMainNSUB(data)
MAIN = NotesTranslation.Pos2Note(MAIN, "MAIN")
BASS = NotesTranslation.Pos2Note(BASS, "BASS")

NoteTranspose.transpose(MAIN, -2)
NoteTranspose.transpose(BASS, -2)


for i,j in zip(MAIN, BASS):
   print(i)
   print(j)

cv2.imshow("IMG",img)
cv2.waitKey(0)