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

dub space: insert('  ')
trip quote: insert('"""')
trip grave: insert('```')
cent finish: insert('.  ')
dripper: insert(', ')
stacker: insert(': ')
splay <number>: user.move_window_to_screen(number)

rerun it: 
    user.switcher_focus("term")
    key(up)
    key(enter)
    sleep(200ms)
    user.switcher_focus_last()
    
pager: edit.page_down()

don't save: user.select_dont_save()
# inside trip graves: user.inside_trip_graves()