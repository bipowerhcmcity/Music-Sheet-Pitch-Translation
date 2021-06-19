class ChordType:
    def __init__(self, data,children=None):
        self.children = children
        self.data = data

class Chord:
    def __init__(self,pt1, pt2, type, sub_type=None):
        self.pt1 = pt1
        self.pt2 = pt2
        self.type = type
        self.sub_type = sub_type
    def getInfo(self):
        return str(self.type)+"_"+str(self.sub_type)+"-"+str(self.pt1)+"-"+str(self.pt2)

class Staff:
    def __init__(self,begin_y, end_y, lines):
        self.begin_y = begin_y
        self.end_y = end_y
        self.lines = lines
        self.chords=[]
    def appendChord(self, chord):
        self.chords.append(chord)


double_close = ChordType("double_close")
double_open=ChordType("double_open")

double = ChordType("double",[double_close,double_open])

black_chord = ChordType("black_chord")

white_chord = ChordType("white_chord")

single_close = ChordType("single_close")
single_open = ChordType("single_open")

single = ChordType("single",[single_close,single_open])

root = ChordType("",[black_chord,double,single,white_chord])




