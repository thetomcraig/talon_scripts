closing time: user.sleep_all()
she's coming | she's here: user.sleep_talon()
sleep I | sleep eye | sleep eyes: user.sleep_eye_tracker()



# disk all: edit.save_all()
# disker: edit.save_all()

scrape: user.escape()
abort: user.escape()
coder : user.switcher_focus("Code")
slack: user.switcher_focus("Slack")
postman: user.switcher_focus("Postman")
apps: user.switcher_launch("/System/Applications/Mission Control.app")
terminal | term: user.switcher_focus("term")
brave : user.switcher_focus("brave")
chrome : user.switcher_focus("chrome")
outlook : user.switcher_focus("outlook")
teams: user.switcher_focus("teams")
mail: user.switcher_focus("mail")
merge: user.switcher_focus("Araxis Merge")


tile hide: key(cmd-h)
tile full: user.full_screen_window()
tile close: app.window_close()
next win | tile next | tyler: app.window_next()
tile last: app.window_previous()
tile min | min win | win min: app.window_hide()

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
chopper:
    key(delete)
    key(delete)


shebang: insert('#! ')
dub space: insert('  ')
trip quote: insert('"""')
trip grave: insert('```')
trip tick: insert('```')
cent finish: insert('.  ')
capper: insert('.  ')
stacker: insert(': ')
dasher: insert('- ')
prober: insert('?  ')
tabber: insert('\t\t')
pointer: insert(' -> ')
arrower: insert(' -> ')
breather: insert(', ')
piper: insert(' | ')
spacer: insert('  ')
set equal: insert(' = ')


snip email: user.enter_secret("email")
snip pass: user.enter_secret("password")
snip long pass: user.enter_secret("computer_password")
snip phone: user.enter_secret("phone_number")
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
run local:
    insert('docker compose --profile runlocal up')
    key(up)
    key(enter)
run debug:
    insert('docker compose --profile debug up')
    key(up)
    key(enter)
log in to int:
    insert('sshint')    
    key(enter)
log in to dev:
    insert('sshdev')    
    key(enter)
django shell [<user.text>]:
    insert('export POLARIS_BE_ENV=')
    user.insert_formatted(user.text, "ALL_CAPS")
    key(enter)
    insert('python manage.py shell --settings=polaris.settings.')
    insert(user.text or "")
    key(enter)
screen flask:
    insert('sudo screen -r $(sudo screen -ls | grep flask | ')
    insert('awk "{print $1')
    insert('}")')
    key(enter)
screen django:
    insert('sudo screen -r $(sudo screen -ls | grep django | ')
    insert('awk "{print $1')
    insert('}")')
    key(enter)
docker running:
    insert('docker ps')
    key(enter)
docker down:
    insert('docker compose down --build')
    key(enter)
docker up:
    insert('docker compose up --build')
    key(enter)
docker nuke:
    insert('dcnk')

pager: edit.page_down()

don't save: user.select_dont_save()

tab pin: key(shift-alt-p)

clear notes: user.clear_notifications()