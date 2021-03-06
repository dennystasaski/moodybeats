import requests
import os

class GoogleAPI:
    speech_url = 'https://texttospeech.googleapis.com/v1/text:synthesize?fields=audioContent&key={token}'

    def __init__(self):
        self.API_TOKEN = os.environ['API_KEY']

    def text_to_speech(self, text):
        body = {
             "input": {
                "text": text
             },
             "voice": {
                "languageCode": "en-US",
                "ssmlGender": "female"
             },
             "audioConfig": {
                "audioEncoding": "mp3"
             }
        }
        url = self.speech_url.replace('{token}', self.API_TOKEN)
        response = requests.post(url=url, json=body)
        return response.json()
