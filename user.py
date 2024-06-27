import os

from talon import Context, Module, actions, app
from talon.mac import applescript

ctx = Context()
mod = Module()

@ctx.action_class("user")
class UserActions:
    def select_dont_save():
        actions.key("space")

    def full_screen_window():
        actions.key("cmd-ctrl-f")

    def show_preferences():
        actions.key("cmd-,")

    def enter_secret(desired_secret: str):
        """Read from secret text file and enter text"""
        secret_dict = {}
        user_dir_path = os.path.join(os.path.expanduser('~'), '.talon', 'user', 'talon_scripts')

        with open(os.path.join(user_dir_path, 'secrets.txt'), 'r') as f:
            for line in f.readlines():
                key, value = line.strip().split(',')
                secret_dict[key] = value

        actions.insert(secret_dict[desired_secret])
        actions.key("enter")

def disable():
    actions.speech.disable()

app.register("ready", disable)

@mod.action_class
class Actions:

    def select_dont_save():
        """Select "don't save" from the dialog"""

    def full_screen_window():
        """Make the window full screen"""

    def show_preferences():
        """Open the preferences"""

    def enter_secret(desired_secret: str): 
        """Enter the secret"""
        
#     def inside_trip_graves():
#         actions.insert('```')
#         actions.insert('\n')
#         actions.insert('```')
#         actions.sleep("500ms")
#         actions.key("up")
#         actions.insert('\n')

