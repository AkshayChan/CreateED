import pyttsx
engine = pyttsx.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+20)
var = 'Hello World.'
engine.say(var)
engine.runAndWait()
 