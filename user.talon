^(talon wake)+$: 
    speech.enable()
    app.notify("Listening")
^(drowse | alright | all right)+$:
    speech.disable()
    app.notify("Sleeping!")
key(ctrl-cmd-t):
    speech.toggle()
    app.notify("Talon toggled!")


slam: edit.paste()
slammer:
    edit.paste()
    key(enter)
slapper:
    edit.line_insert_down()
    edit.line_insert_down()

trip quote: insert('"""')
trip grave: insert('```')
cent finish: insert('.  ')
splay <number>: user.move_window_to_screen(number)

# inside trip graves: user.inside_trip_graves()