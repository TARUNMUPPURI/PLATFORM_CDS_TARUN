# import noisereduce as nr
# import librosa
# import soundfile as sf

# # Load audio file
# audio_file, sample_rate = librosa.load('audio_2.wav')

# # Estimate noise profile
# noise_profile = nr.profile_noise(audio_file, sample_rate)

# # Reduce noise
# reduced_audio = nr.reduce_noise(audio_file, noise_profile)

# # Save output audio file
# sf.write('output_audio.wav', reduced_audio, sample_rate)



# from scipy.io import wavfile
# import noisereduce as nr
# # load data
# rate, data = wavfile.read("/home/muppuri/python/speech_recognition/audio_4.wav")
# # perform noise reduction
# reduced_noise = nr.reduce_noise(y=data, sr=rate)
# wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)




import noisereduce as nr
from pydub import AudioSegment
from pydub.playback import play
import scipy.io.wavfile
from playsound import playsound

# load data
rate, data = scipy.io.wavfile.read("/home/muppuri/python/speech_recognition/canara_captchas/E6KX4.wav")
print(rate,data)
audio_out_file = "mywav_reduced_noise.wav"
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
print(reduced_noise)
#reduced_noise.export(audio_out_file, format="wav")
scipy.io.wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)
# song = AudioSegment.from_wav("/home/beena/Downloads/mywav_reduced_noise.wav")
print('playing sound using  pydub')
playsound('mywav_reduced_noise.wav')