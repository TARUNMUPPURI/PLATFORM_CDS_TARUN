# sbi capcha recognition by addin one seconds silence front and back of the video
from pydub import AudioSegment
audio_in_file = "audio_2.wav"
audio_out_file = "out_sine.wav"
# create 1 sec of silence audio segment
one_sec_segment = AudioSegment.silent(duration=1000)  #duration in milliseconds

#read wav file to an audio segment
song = AudioSegment.from_wav(audio_in_file)

#Add above two audio segments    
final_song = one_sec_segment + song + one_sec_segment

#Either save modified audio
final_song.export(audio_out_file, format="wav")


import speech_recognition as sr
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(audio_out_file) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    text1=""
    for i in text:
        if i==" ":
            pass
        else:
            text1+=i
    print(text1)

