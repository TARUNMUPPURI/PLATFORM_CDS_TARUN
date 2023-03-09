# sbi capcha recognition by adding the same audio twice and storing in other audio file and taking first five letters of the output 
import wave
from pydub import AudioSegment
infiles=["audio_3.wav","audio_3.wav"]
outfile = "sounds.wav"
one_sec_segment = AudioSegment.silent(duration=1000) 
data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()

import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile(outfile) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    text1=""
    for i in text:
        if i==" ":
            pass
        else:
            text1+=i
    print(text1[:5])

