^(talon wake)+$: speech.enable()
^(drowse | alright | all right)+$: speech.disable()

#^sea mode$: mode.enable ("command")
#^d mode$: mode.enable ("dictation")

# Define a hotkey to toggle Talon
key(ctrl-cmd-t): speech.toggle()

^(focus term)+$: 


