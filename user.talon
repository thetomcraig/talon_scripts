^(talon wake)+$: speech.enable()
^(wake up)+$: speech.enable()

^(drowse)+$: speech.disable()

# Define a hotkey to toggle Talon
key(ctrl-shift-t): speech.toggle()