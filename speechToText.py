#!/usr/bin/env python3                                                                                
import datetime as dt                                                                                                      
import speech_recognition as sr  
 
# get audio from the microphone                                                                       
r = sr.Recognizer()
r.dynamic_energy_threshold = True # type: bool
r.dynamic_energy_adjustment_damping = 0.15 # type: float
r.dynamic_energy_adjustment_ratio = 1.5 # type: float
r.pause_threshold = 0.8 # type: float



with sr.Microphone() as mic:                                                                       
    print("Speak:")
    
    #d1 = dt.datetime.now()
    #print(d1.minute)
    #print(d1.second)
    
    audio = r.listen(mic, 7)
    print("it has stopped recording")

#d2 = dt.datetime.now()
#print(d2.minute)
#print(d2.second)

try:
    print(r.recognize_google(audio_data= audio, language = "en-IN"))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

#d3 = dt.datetime.now()
#print(d3.minute)
#print(d3.second)
