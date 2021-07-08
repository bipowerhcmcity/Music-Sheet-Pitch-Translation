import numpy as np
import cv2


import HoughTransform.RunLengthEncoding
import StaffLineRemoval
import ClassifiedTypeChord
import ChordType
import CreateStaff
import CombineOpenClose
import NotesTranslation

#feature_type = ["black_chord","double close","double open","single close","single open","white_chord"]
color = [(0,0,255),(0,255,0),(0,255,255),(255,0,0),(204,0,102),(0,0,0)] # red, green, yellow, blue, purple, black

feature_type = ChordType.root

img = cv2.imread("sheet_4.jpg")

clef_sol = cv2.imread("chord.jpg")
lines, staff_height = HoughTransform.RunLengthEncoding.DrawLine(False,img)
removal = StaffLineRemoval.StaffLineRemoval(img)
print("Staff_Height",staff_height)



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
#for i in range(len(staffs)):
#    for j in range(len(staffs[i].chords)):
#        print("Staff",i," chord ",j,staffs[i].chords[j].sharp)



data = NotesTranslation.Pos2Pos(staffs)
data = NotesTranslation.ReOrderedStaffs(data)
#for i in data:
#    print(i)

unprocessed_data, data = NotesTranslation.Pos2Height(data, headlines, abs(lines[0] - lines[1]))


MAIN, BASS = NotesTranslation.SeparateMainNSUB(data)
MAIN = NotesTranslation.Pos2Note(MAIN, "MAIN")
BASS = NotesTranslation.Pos2Note(BASS, "BASS")
#for i,j in zip(MAIN, BASS):
#    print(i)
#    print(j)


file_handle_1 = open('note_type.csv', 'w')
file_handle_2 = open('note.csv', 'w')
for i,j in zip(MAIN, BASS):
    file_handle_1.write(','.join([str(note_main[0]) for note_main in i]) + '\n')
    file_handle_1.write(','.join([str(note_bass[0]) for note_bass in j]) + '\n')
    file_handle_2.write(','.join([str(note_main[2]) for note_main in i]) + '\n')
    file_handle_2.write(','.join([str(note_bass[2]) for note_bass in j]) + '\n')
file_handle_1.close()
file_handle_2.close()
#
#
# pt_clef1, pt_clef2 = ClassifiedTypeChord.addFeature(clef_sol,removal)
# h_clef = cv2.cvtColor(clef_sol,cv2.COLOR_BGR2GRAY)
# h_clef = clef_sol.shape[0]
# #
# #
# #
# # # for pt in pt_clef1:
# # #     for i in range(pt[1],h_clef+pt[1],1):
# # #         for line in lines:
# # #             if(i==line):
# # #                 cv2.line(img, (-1000, line), (1000, line), (127, 127, 127), 1)
# #
# # # # Lines:
# # # for line in lines:
# # #         cv2.line(img, (-1000, line), (1000, line), (255,255,255), 1)
# #
# #
# #
# notes_height = ['E5', 'D5', 'C5', 'B4', 'A4', 'G4', 'F4','E4', 'D4', 'C4', 'B3', 'A3', 'G3', 'F3','E3', 'D3', 'C3']#, 'B', 'A', 'G', 'F','E', 'D', 'C', 'B', 'A', 'G', 'F']
# notes_height_1 = ['E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6','G6']
# #
# staffline_dist = lines[1] - lines[0] # blank size between 2 lines in one staff
# print("StaffLine distance: ",staffline_dist)
#
# def RoundNumber(num):
#     sign = num / (abs(num))
#     standard = (int(abs(num)) + 0.5)
#     if abs(num) > standard:
#         return (int(num) + int(sign))
#     else:
#         return (int(num))
#
#
# height = []
# for k in range(len(staffs)):
#     temp = []
#     for chord in (staffs[k].chords):
#         anchorPoint = chord.pt1
#         temp.append(RoundNumber((-staffs[k].lines[0] + anchorPoint[1])/(staffline_dist/2)))
#     height.append(temp)
# #print(height)
#
# result = []
# count = 0
# for i in height:
#     temp = []
#     for j in i:
#         count+=1
#         print(count)
#         if j <0:
#             print(abs(j))
#             print(notes_height_1[abs(j)])
#             temp.append(notes_height_1[abs(j)])
#         else:
#             # print(abs(j))
#             # print(j)
#             print(notes_height[j])
#             temp.append(notes_height[j])
#     result.append(temp)
# for i in result:
#     print(i)
#
cv2.imshow("IMG",img)
cv2.waitKey(0)