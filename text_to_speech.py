import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say('''They say, "The holy water's watered down
And this town's lost its faith
Our colors will fade eventually"
So, if our time is runnin' out
Day after day
We'll make the mundane our masterpiece

[Pre-Chorus]
Oh my, my
Oh my, my love
I take one look at you''')
# engine.say("I'll created by  Lucky")
engine.runAndWait()