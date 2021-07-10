
notes_height = ['E5', 'D5', 'C5', 'B4', 'A4', 'G4', 'F4','E4', 'D4', 'C4', 'B3', 'A3', 'G3', 'F3','E3', 'D3', 'C3']#, 'B', 'A', 'G', 'F','E', 'D', 'C', 'B', 'A', 'G', 'F']
notes_height_1 = ['E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6','G6']


notes_height_BASS = ['G3', 'F3', 'E3', 'D3', 'C3', 'B2', 'A2','G2', 'F2', 'E2', 'D2', 'C2', 'B1', 'A1','G1', 'F1', 'E1']#, 'B', 'A', 'G', 'F','E', 'D', 'C', 'B', 'A', 'G', 'F']
notes_height_BASS_1 = ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4']



def SeparateMainNSUB(staffs):
	MAIN = []
	SUB = []
	for i in range(len(staffs)):
		if i%2 == 0:
			MAIN.append(staffs[i])
		else:
			SUB.append(staffs[i])
	return MAIN, SUB

#------------------------------------------------------------
def HorzDist(note1, note2):
	return abs(note1[0] - note2[0])
def IsLeft(note1, note2):
	if note1[0] - note2[0] < 0:
		return True
	else:
		return False
def MinIndex(note, staff):
	min_value = 999;
	index = 0;
	for i in range(len(staff)):
		T = staff[i]
		temp = HorzDist(note, T[2])
		if temp < min_value:
			min_value = temp
			index = i
	return index


def ReOrderedStaffs(staffs):
	threshold = 5
	MAIN_staff, SUB_staff = SeparateMainNSUB(staffs)
	MAIN_RE_ORDERED = []
	SUB_RE_ORDERED = []
	for i in range(len(MAIN_staff)):#scan for each main staff
		main_temp = []
		sub_temp = []
		MAIN = MAIN_staff[i].copy()
		SUB = SUB_staff[i].copy()
		while len(MAIN) >0 or len(SUB)>0:
			if len(MAIN) > 0 and len(SUB)>0:
				DIS = HorzDist(MAIN[0][2], SUB[0][2])
				print(DIS)
				if DIS <=threshold:
					main_temp.append(MAIN[0])
					sub_temp.append(SUB[0])
					MAIN.remove(MAIN[0])
					SUB.remove(SUB[0])
				elif DIS >threshold:
					if IsLeft(MAIN[0][2], SUB[0][2]):
						main_temp.append(MAIN[0])
						sub_temp.append(tuple([0, "NONE", (0,0), False, False]))
						MAIN.remove(MAIN[0])
					else:
						sub_temp.append(SUB[0])
						main_temp.append(tuple([0, "NONE", (0,0), False, False]))
						SUB.remove(SUB[0])
			else:
				if len(SUB) == 0:
					main_temp.append(MAIN[0])
					sub_temp.append(tuple([0, "NONE", (0,0), False, False]))
					MAIN.remove(MAIN[0])
				elif len(MAIN) == 0:
					sub_temp.append(SUB[0])
					main_temp.append(tuple([0, "NONE", (0,0), False, False]))
					SUB.remove(SUB[0])
		MAIN_RE_ORDERED.append(main_temp)
		SUB_RE_ORDERED.append(sub_temp)
	new_staffs = []
	for i,j in zip(MAIN_RE_ORDERED, SUB_RE_ORDERED):
	    new_staffs.append(i)
	    new_staffs.append(j)
	return new_staffs


#--------------------------------------------------------------

def RoundNumber(num):
	sign = num/(abs(num))
	standard = (int(abs(num)) + 0.5)
	if abs(num) > standard:
		return (int(num) + int(sign))
	else:
		return (int(num))
def Pos2Pos(staffs):
	data = []
	for staff in staffs:
		data.append(staff.GetNoteInfo())
	return data
def Pos2Height(data, headlines, staffline_dist):
	unprocess_height=[]
	height = []
	for i in range(len(data)):
		temp = []
		temp_1 = []
		for pos in (data[i]):
			tempT = pos[2]
			temp.append(tuple([pos[0], str(pos[1]), RoundNumber((-headlines[i] + tempT[1])/(staffline_dist/2)), pos[3], pos[4]]))
			temp_1.append((-headlines[i] + tempT[1])/(staffline_dist/2))
		height.append(temp)
		unprocess_height.append(temp_1)
	return unprocess_height, height



def Pos2Note(data, key):
	if key == "MAIN":
		result = []
		for staff in data:
			temp = []
			for note in staff:
				print("Note",note)
				if note[2] <0 and abs(note[2]) < len(notes_height_1):
					temp.append(tuple([note[0], note[1], notes_height_1[abs(note[2])],note[3],note[4]]))
				elif note[2]>=0 and note[2] < len(notes_height):
					temp.append(tuple([note[0], note[1], notes_height[note[2]],note[3],note[4]]))
				else:
					temp.append(tuple([note[0], note[1], "NONE",note[3],note[4]]))
			result.append(temp)
		return result
	elif key == "BASS":
		result = []
		for staff in data:
			temp = []

			for note in staff:
				if note[2] < 0 and abs(note[2]) < len(notes_height_BASS_1):
					temp.append(tuple([note[0], note[1], notes_height_BASS_1[abs(note[2])],note[3],note[4]]))
				elif note[2] >=0 and note[2] < len(notes_height_BASS):
					temp.append(tuple([note[0], note[1], notes_height_BASS[note[2]],note[3],note[4]]))
				else:
					temp.append(tuple([note[0], note[1], "NONE"]))
			result.append(temp)
		return result