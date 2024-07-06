^(talon wake)+$: 
    speech.enable()
    app.notify("Listening")
^(drowse | alright | all right)+$:
    speech.disable()
    app.notify("Sleeping!")
key(ctrl-cmd-t):
    speech.toggle()
    app.notify("Talon toggled!")

# disk all: edit.save_all()
# disker: edit.save_all()

# # Misc Edit
# scrape: user.escape()
# abort: user.escape()

slam: edit.paste()
slammer:
    edit.paste()
    key(enter)
slapper:
    edit.line_insert_down()
    edit.line_insert_down()

shebang: insert('#! ')
dub space: insert('  ')
trip quote: insert('"""')
trip grave: insert('```')
trip tick: insert('```')
cent finish: insert('.  ')
dripper: insert(', ')
stacker: insert(': ')
dasher: insert('- ')
tabber: insert('\t\t')
pointer: insert(' -> ')
arrower: insert(' -> ')
piper: insert(' | ')
set equal: insert(' = ')

snip email: insert('thetomcraig@icloud.com')
snip work_email: insert('tom.craig@ayahealthcare.com')
#snip email password: user.enter_secret('email_password')
snip pass: user.enter_secret("password")
snip long pass: user.enter_secret("computer_password")
show prefs | prefs show: user.show_preferences()
splay <number>: user.move_window_to_screen(number)

show help | help menu:
    key(cmd-shift-?)
rerun it: 
    user.switcher_focus("term")
    key(up)
    key(enter)
    sleep(200ms)
    user.switcher_focus_last()
    
pager: edit.page_down()

don't save: user.select_dont_save()

tile full: user.full_screen_window()
# inside trip graves: user.inside_trip_graves()

tab pin: key(shift-alt-p)
