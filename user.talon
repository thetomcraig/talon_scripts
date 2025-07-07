# keep this around to easily debug stuff
run debug function:
    user.debugging()
key(ctrl-cmd-d):
    user.debugging()
# face(scrunch_nose): user.debugging()
# face(pucker_lips_right): 
#     user.debugging()
# face(raise_eyebrows):
#     user.debugging()
# face(brow_inner_up):
#     user.debugging()
# face(brow_inner_up:stop):
#     user.debugging()
# face(brow_down_left):
#     user.debugging()
# face(brow_down_left:stop):
#     user.debugging()
face(brow_inner_up):
    user.scroll_up_continuous_custom()
face(brow_inner_up:stop):
  user.mouse_scroll_stop()
face(smile_left):
    user.scroll_down_continuous_custom()
face(smile_left:stop):
  user.mouse_scroll_stop()

key(ctrl-cmd-t):
    speech.toggle()
    tracking.control_zoom_toggle()
    app.notify("Talon toggled!")
#All raw expressions:
#  brow_down_left
#  brow_down_right - false positives
#  brow_inner_up - works
#  brow_outer_up_left
#  brow_outer_up_right
#  blink_left - false positives
#  blink_right - false positives
#  gaze_down_left
#  gaze_down_right
#  gaze_in_left
#  gaze_in_right
#  #gaze_out_left
#  gaze_out_right
#  gaze_up_left
#  gaze_up_right
#  squint_left - false positives with blink
#  squint_right - false positives with blink
#  eye_wide_left - hard to trigger.
#  eye_wide_right - Hard to trigger.
#  jaw_open
#  jaw_left
#  jaw_right
#  mouth_close
#  dimple_left
#  dimple_right
#  frown_left
#  #frown_right
#  mouth_funnel - false positives
#  mouth_lower_down_left
#  mouth_lower_down_right
#  mouth_press_left
#  mouth_press_right
#  mouth_pucker
#  mouth_right
#  mouth_left
#  mouth_roll_lower
#  mouth_roll_upper
#  mouth_shrug_lower
#  #mouth_shrug_upper
#  smile_left
#  smile_right
#  mouth_stretch_left
#  mouth_stretch_right
#  mouth_upper_up_left
#  mouth_upper_up_right



# Talon functions
closing time: user.sleep_all()
she's coming | she's here: user.sleep_talon()
calibrate: user.calibrate_eye_tracker()
sleep (I | eye | eyes): user.sleep_eye_tracker()
awake I | awake eye | awake eyes: user.wake_eye_tracker()
show log:
    insert('tail -f /Users/tomcraig/.talon/talon.log') 
    key(enter)
tick:
    user.repeat_last_command()

# General app stuff
show prefs | prefs show: user.show_preferences()
show help | help menu:
    key(cmd-shift-?)
don't save | no save: user.select_dont_save()
tab pin: key(shift-alt-p)

^code <user.text>$:
    user.open_vscode_project("{text}")

# App launching
^coder: user.switcher_focus("Code")
^finder: user.switcher_focus("Finder")
^slack: user.switcher_focus("Slack")
^postman: user.switcher_focus("Postman")
^terminal | term: user.switcher_focus("term")
^brave | browse: user.switcher_focus("brave")
^browse reload | brave reload:
    user.switcher_focus("brave")
    key(cmd-r)
# Chrome specific because I only use chrome for debugging webapps
^chrome: user.switcher_focus("chrome")
^chrome reload:
    user.switcher_focus("chrome")
    key(cmd-r)
^messages | imessage: user.switcher_focus("Messages")
^outlook: user.switcher_focus("outlook")
^excel: user.switcher_focus("excel")
^teams: user.switcher_focus("teams")
^mail: user.switcher_focus("mail")
^merge: user.switcher_focus("Araxis Merge")
#clear notes: user.clear_notifications()
clear notes: key(cmd-ctrl-shift-g)

# Window functionality
tile hide: key(cmd-h)
tile close | tile kill | kill tile: app.window_close()
next win | tile next | tyler: app.window_next()
tile last: app.window_previous()
tile min | min win | win min: app.window_hide()
splay <number>: user.move_window_to_screen(number)

# General editing
slam: edit.paste()
slammer:
    edit.paste()
    key(enter)
slapper:
    edit.line_insert_down()
    edit.line_insert_down()
wiper:
    key(backspace)
    key(backspace)
chop:
    key(delete)
chopper:
    key(delete)
    key(delete)

# Keys
scrape: user.escape()
abort: user.escape()

# Navigation
pager: edit.page_down()

# Symbols
shebang: insert('#! ')
dub space: insert('  ')
trip quote: insert('"""')
trip grave: insert('```')
cent finish | scent finish | center | capper: insert('.  ')
stacker: insert(': ')
dasher | bullet: insert('- ')
hasher | hash er: insert('# ')
prober: insert('?  ')
tabber: insert('\t\t')
pointer: insert(' -> ')
arrower: insert(' -> ')
breather: insert(', ')
piper: insert(' | ')
spacer: insert('  ')
banger: insert('! ')
set equal: insert(' = ')

# Snippets, secrets
snip email: user.enter_secret("email")
snip pass: user.enter_secret("computer_password")
snip Microsoft pass: user.enter_secret("password")
snip phone: user.enter_secret("phone_number")


# Development work
vim approve:
    key(ctrl-c)
    insert(':wq')
    key(enter)
rerun it: 
    key(cmd-s)
    sleep(200ms)
    user.switcher_focus("term")
    key(up)
    key(enter)
rerun it back: 
    key(cmd-s)
    sleep(200ms)
    user.switcher_focus("term")
    key(up)
    key(enter)
    sleep(200ms)
    user.switcher_focus_last()
make up local:
    key(ctrl-c)
    insert('make uplocal')
    key(enter)
make up test:
    key(ctrl-c)
    insert('make uptest')
    key(enter)
make link <user.text>$:
    key(ctrl-c)
    sleep(200ms)
    insert('make link env={text}')
    key(enter)
docker running:
    insert('docker ps')
    key(enter)
docker down:
    insert('docker compose down')
    key(enter)
docker up:
    insert('docker compose up --build')
    key(enter)
docker volumes:
    insert('docker volume list')
    key(enter)
docker nuke volumes:
    insert('docker volume rm $(docker volume ls -q)')
    key(enter)
docker nuke all:
    insert('dcnk')
win jira <number>$:
    user.open_winnow_jira_task('{number}')
(win | twin) (num | numb) <number>$:
    user.insert_winnow_jira_number('{number}')
az login:
    key(ctrl-c)
    # sleep(200ms)
    insert('az login')
    key(enter)