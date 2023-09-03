import whisper

model = whisper.load_model('base')
result = model.transcribe('https://www.google.com/recaptcha/api2/payload/audio.mp3?p=06ADUVZwAAMwAY01n7xoHdgYIlmMlSqD5r0GuqfiO-0saMOYRFnVSNvZH3ZxayzvOxwcr-LeILxp9p1MQkNTdV6WMzOPlgtHHlTeNNDWD95TzClBHwQ5ZlZI4rV4AxiJsn6bo3nRmtyT0KeM1L_P8WdQsauE47waEj6Fsq2ZNQ1VkNIqAD9-5fBKbAkME5xnoAzuoMzeX0Vmr0&k=6LflndkbAAAAAMtC8hy8LXjRop4gJqLVz0S1OyJQ')

with open('transcription.txt', 'w') as f:
    f.write(result['text'])
# audioFile = whisper.load_audio("audio.mp3")