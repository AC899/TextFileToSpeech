from gtts import gTTS
import os
import docx

# user input to a file path with verification that file path exists
#make the user input accept a word document OR  text document

class Main:

    def __init__(self):
        pass

    def reading_file():
        while True:
            try:
                with open('/Users/anilcarrier/Desktop/CVa2022.docx') as f:
                    lines = f.readline()
                    mytext = lines
                    audio = gTTS(text=mytext, lang="en", slow=False)
                    audio.save("text_to_audio.mp3")
                    os.system("start example.mp3")
            except UnicodeDecodeError as e:
                print("I can only translate .txt files on this iteration\n"
                      "Please enter the path to the text file you want me to translate")
                break

Object = Main()
Main.reading_file()