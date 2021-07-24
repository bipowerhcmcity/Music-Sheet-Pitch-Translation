import mingus.extra.lilypond as lilypond
translate = {'b':"es"
                ,1:"4",
                 2:"8",
                 3:"16",
                 4:"2",
                 7:"r8",
                 9:"r1",
                 "Eb":["e","a","b"],
                 "F":"b",
                 "Bb":["b","e"],
                 "Ab":["e","a","b","d"],
                 "G":"f",
                 "D":["f","c"],
                 "A":["f","c","g"],
                 "E":["f","c","g","d"],
                 "B":["f","c","g","d","a"],
                 }
version = "\\version \"2.22.1\" "
def start(Chord,main,bass,symbol):
    NotesHaveSharp = translate[Chord]
    majorChord = Chord[0].lower()
    if len(Chord) >1:
        symbolChord = translate[Chord[1]]
        majorChord += symbolChord
    print(majorChord)
    result =version

    for i,j in zip(main,bass):
        output = "\\score{ \\new PianoStaff <<"
        output+="\\new Staff = ""RH"" <<"
        output+=writingNote(i,"MAIN",majorChord,NotesHaveSharp,symbol)+"} >>"
        output += "\\new Staff = ""LH"" <<"
        output+=writingNote(j, "BASS", majorChord, NotesHaveSharp, symbol)+"} >> >> \\layout{ } \\midi{ }  }"
        result+=output
    print(result)

    lilypond.to_pdf(result, "result/result")


def writingNote(staff1_test,type,majorChord, NotesHaveSharp,symbol):
    if(type == "MAIN"):
        upper = "\\absolute {\\clef ""treble""\\key "
    else:
        upper = "\\absolute {\\clef ""bass""\\key "
    outputNotes = ""

    startedCombine = False

    for i in range(len(staff1_test)):
        note = list(staff1_test[i])
        previousNote = list(staff1_test[i-1])

        currentOctave = int((note[2])[1]) - 3
        octave = ""
        pitchNote = ""
        durationNote=""

        for i in range(currentOctave):
            octave += "'"

        pitchNote = (note[2])[0].lower()
        if (note[3] == True):
            pitchNote += "is"
        for j in NotesHaveSharp:
            if (pitchNote == j and symbol == -1):
                pitchNote += "es"  # flat
            if (pitchNote == j and symbol == 1):
                pitchNote += "is"  # sharp

        if note[0] == 7:
            if (startedCombine):
                previousDuration = translate[previousNote[0]]
                print("note: ",note)
                print("Dot or not:",previousNote)
                if previousNote[6] == True:
                    previousDuration += "."
                outputNotes += ">"+previousDuration+" "
                startedCombine = False
            pitchNote = translate[note[0]]
            outputNotes+=pitchNote+" "
        elif note[0] ==9:
            if (startedCombine):
                previousDuration = translate[previousNote[0]]
                print("note: ",note)
                print("Dot or not:",previousNote)
                if previousNote[6] == True:
                    previousDuration += "."
                outputNotes += ">"+previousDuration+" "
                startedCombine = False
            pitchNote = translate[note[0]]
            outputNotes+=pitchNote+" "
        elif note[5] == True:
            if(startedCombine==False):
                pitchNote="<"+pitchNote
                startedCombine=True
            outputNotes +=pitchNote + octave+" "
        else:
            if(startedCombine):
                previousDuration = translate[previousNote[0]]
                print("note: ", note)
                print("Dot or not:", previousNote)
                if previousNote[6] == True:
                    previousDuration += "."
                outputNotes+=">"+previousDuration+" "
                startedCombine = False

            durationNote = translate[note[0]]
            if note[6] == True:
                durationNote+="."

            outputNotes+=pitchNote + octave+durationNote + " "
    return upper+ majorChord+"\\major\\time 4/4 "+outputNotes