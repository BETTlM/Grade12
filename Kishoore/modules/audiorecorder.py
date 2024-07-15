from gtts import gTTS



def record(textfile,audfile):
    file = open(textfile,'r')
    content = file.read()
    file.close()


    tts = gTTS(text=content, lang='en')
    tts.save(audfile)
