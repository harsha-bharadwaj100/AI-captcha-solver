import whisper

model = whisper.load_model('base')
result = model.transcribe('audio (2).mp3')

with open('transcription.txt', 'w') as f:
    f.write(result['text'])
# audioFile = whisper.load_audio("audio.mp3")