import time
from api import API_KEY_ASSEMBLYAI
import requests
import sys
import time
filename=sys.argv[1]
upload_endpoint="https://api.assemblyai.com/v2/upload"
trascript_endpoint = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization': API_KEY_ASSEMBLYAI}

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    
    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))


    audio_url=upload_response.json()['upload_url']
    return audio_url


def transcribe(audio_url):

    transcript_request = { "audio_url": audio_url}
    transcript_response = requests.post(trascript_endpoint, json=transcript_request, headers=headers)
    job_id=transcript_response.json()['id']
    return job_id


# pooool
def poll(transcript_id):
    pooling_endpoint=trascript_endpoint+'/'+transcript_id
    pooling_response=requests.get(pooling_endpoint,headers=headers)
    return pooling_response.json()



def get_transcription_result_url(audio_url):
    
    transcript_id=transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data,None
        elif data['status']=='error':
            return data,"error"
        print('waiting 30 seconds...')
        time.sleep(5)

def save_transcript(audio_url):
    data,error = get_transcription_result_url(audio_url)
    print(data['text'][:-1])


audio_url=upload(filename)
save_transcript(audio_url)