import librosa
import pylab
import numpy as np
import soundfile as sf
    
#sf.write('stereo_file.wav', np.random.randn(1000000, 2),44100,  'PCM_24')


#dur = 0.25
#y_A1, sr = librosa.load('./music_note/A1.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_A2, sr = librosa.load('./music_note/A2.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_A3, sr = librosa.load('./music_note/A3.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_A4, sr = librosa.load('./music_note/A4.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_A5, sr = librosa.load('./music_note/A5.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_B1, sr = librosa.load('./music_note/B1.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_B2, sr = librosa.load('./music_note/B2.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_B3, sr = librosa.load('./music_note/B3.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_B4, sr = librosa.load('./music_note/B4.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_B5, sr = librosa.load('./music_note/B5.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_C2, sr = librosa.load('./music_note/C2.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_C3, sr = librosa.load('./music_note/C3.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_C4, sr = librosa.load('./music_note/C4.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_C5, sr = librosa.load('./music_note/C5.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_C6, sr = librosa.load('./music_note/C6.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_D2, sr = librosa.load('./music_note/D2.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_D3, sr = librosa.load('./music_note/D3.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_D4, sr = librosa.load('./music_note/D4.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_D5, sr = librosa.load('./music_note/D5.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_D6, sr = librosa.load('./music_note/D6.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_E2, sr = librosa.load('./music_note/E2.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_E3, sr = librosa.load('./music_note/E3.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_E4, sr = librosa.load('./music_note/E4.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_E5, sr = librosa.load('./music_note/E5.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_E6, sr = librosa.load('./music_note/E6.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_F2, sr = librosa.load('./music_note/F2.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_F3, sr = librosa.load('./music_note/F3.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_F4, sr = librosa.load('./music_note/F4.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_F5, sr = librosa.load('./music_note/F5.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_F6, sr = librosa.load('./music_note/F6.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_G2, sr = librosa.load('./music_note/G2.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_G3, sr = librosa.load('./music_note/G3.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_G4, sr = librosa.load('./music_note/G4.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_G5, sr = librosa.load('./music_note/G5.wav', sr=22050, mono=True, offset=0.0, duration=dur)
#y_G6, sr = librosa.load('./music_note/G6.wav', sr=22050, mono=True, offset=0.0, duration=dur)

SOUNDS = ['./music_note/A1.wav','./music_note/A2.wav','./music_note/A3.wav',
'./music_note/A4.wav','./music_note/A5.wav','./music_note/B1.wav','./music_note/B2.wav','./music_note/B3.wav','./music_note/B4.wav','./music_note/B5.wav','./music_note/C2.wav',
'./music_note/C3.wav','./music_note/C4.wav','./music_note/C5.wav','./music_note/C6.wav','./music_note/D2.wav','./music_note/D3.wav','./music_note/D4.wav','./music_note/D5.wav',
'./music_note/D6.wav','./music_note/E2.wav','./music_note/E3.wav','./music_note/E4.wav','./music_note/E5.wav','./music_note/E6.wav','./music_note/F2.wav','./music_note/F3.wav',
'./music_note/F4.wav','./music_note/F5.wav','./music_note/F6.wav','./music_note/G2.wav','./music_note/G3.wav','./music_note/G4.wav','./music_note/G5.wav','./music_note/G6.wav']
#SAMPLE_SOUND = [y_A1,y_A2,y_A3,y_A4,y_A5,y_B1,y_B2,y_B3,y_B4,y_B5,y_C2,y_C3,y_C4,y_C5,y_C6,y_D2,y_D3,y_D4,y_D5,y_D6,y_E2,y_E3,y_E4,y_E5,y_E6,y_F2,y_F3,y_F4,y_F5,y_F6,y_G2,y_G3,y_G4,y_G5,y_G6]


NOTES = ['A1', 'A2','A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4','B5','C2','C3','C4','C5','C6','D2','D3','D4','D5','D6','E2','E3','E4','E5', 'E6','F2','F3','F4','F5','F6','G2','G3','G4','G5','G6']
Duration = [0, 0.5, 0.25, 0.125, 1, 2]
#Duration = [0, 0.25, 0.25, 0.25, 1, 2]
file_handle_note = open('note.csv', 'r')
file_handle_note_type = open('note_type.csv', 'r')
data_note = file_handle_note.readlines()
data_note_type = file_handle_note_type.readlines()



def GetIndex(note):
	for i in range(len(NOTES)):
		if NOTES[i] == note:
			return i
out = []
for i in range(int(len(data_note)/2)):
	main = data_note[i*2].split(',')
	bass = data_note[i*2 + 1].split(',')

	main_type = data_note_type[i*2].split(',')
	bass_type = data_note_type[i*2 + 1].split(',')
	print(main)
	for index in range(len(main)):
		if bass[index].strip() == 'NONE':
			print(main[index].strip())
			y,sr  = librosa.load(SOUNDS[GetIndex(main[index].strip())], sr=22050, mono=True, offset=0.0, duration=Duration[int(main_type[index].strip())])
			out = out + list(y)
		elif main[index].strip() == 'NONE':
			y,sr  = librosa.load(SOUNDS[GetIndex(bass[index].strip())], sr=22050, mono=True, offset=0.0, duration=Duration[int(bass_type[index].strip())])
			out = out + list(y)
		else:
			print(main[index].strip(), '\t\t', int(main_type[index].strip()))
			y1,sr = librosa.load(SOUNDS[GetIndex(main[index].strip())], sr=22050, mono=True, offset=0.0, duration=Duration[int(main_type[index].strip())])
			y2, sr = librosa.load(SOUNDS[GetIndex(bass[index].strip())], sr=22050, mono=True, offset=0.0, duration=Duration[int(bass_type[index].strip())])
			if len(y1) == len(y2):
				out = out + list((y1 + y2)/2)
			else:
				out = out + list(y1) + list(y2)
out = np.array(out)
sf.write('RESULT.wav', out, sr, 'PCM_24')
