# importing speech recognition package from google api
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files


def speaks(output, nameOfFile):

    # num to rename every audio file
    print("Your inputed text : ", output)

    toSpeak = gTTS(text=output, lang='en-us', slow=False)
    # saving the audio file given by google text to speech
    file = str(nameOfFile) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    return file




# Driver Code
if __name__ == "__main__":
    userInput = input("Enter your text:\n")
    fileName = input("Enter file name:\n")
    file = speaks(userInput, fileName)
    print("Here is your file: "+file)

