import pdfminer.high_level as pdfminer
import writer
import time
import audiorecorder
def convert(pdflocation):

        content = pdfminer.extract_text(pdflocation)
        writer.writenow(content)
  
        audiorecorder.record('/home/bettim/Documents/Kishoore/book.txt','/home/bettim/Documents/Kishoore/recordedaudio.mp3')

        print('PASSED')
    
