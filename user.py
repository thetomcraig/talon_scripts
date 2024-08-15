import os
import sys

import talon
from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

def get_secret(desired_value: str):
    """Get a secret value from the secrets.csv file"""
    secret_dict = {}
    user_dir_path = os.path.join(os.getcwd(), 'user', 'talon_scripts')

    with open(os.path.join(user_dir_path, 'secrets.csv'), 'r') as f:
        for line in f.readlines():
            key, value = line.strip().split(',')
            secret_dict[key] = value

    return secret_dict[desired_value]


# AI Tools Setup
os.environ["OPENAI_API_KEY"] = get_secret("openai_api_key")


@ctx.action_class("user")
class UserActions:

    def sleep_talon():
        actions.tracking.control_zoom_toggle(False)
        actions.speech.disable()
        actions.app.notify("Talon asleep")

    def sleep_eye_tracker():
        actions.tracking.control_zoom_toggle(False)
        actions.app.notify("Eye tracking asleep")

    def debugging():
        print(os.getcwd())

    def sleep_all():
        actions.tracking.control_zoom_toggle(False)
        actions.speech.disable()
        app.notify("Turn in of work complete!!")
        actions.sleep("180ms")
        actions.user.system_command("pmset sleepnow")

    def enter_secret(desired_secret: str):
        """Read from secret text file and enter text"""
        secret = get_secret(desired_secret)
        actions.insert(secret)
        actions.key("enter")

    def select_dont_save():
        actions.key("space")

    def full_screen_window():
        actions.key("cmd-ctrl-f")

    def show_preferences():
        actions.key("cmd-,")

    def clear_notifications():
        """Using this in conjunction with BetterTouchTool, no solution using AppleScript worked"""
        actions.key("cmd-ctrl-shift-n")

def disable():
    actions.speech.disable()

app.register("ready", disable)

@mod.action_class
class Actions:
    def sleep_talon():
        """Sleep talon"""

    def sleep_eye_tracker():
        """Sleep the eye tracker"""

    def sleep_all():
        """Sleep the computer and talon"""

    def debugging():
        """Where I debug stuff"""

    def select_dont_save():
        """Select "don't save" from the dialog"""

    def full_screen_window():
        """Make the window full screen"""

    def show_preferences():
        """Open the preferences"""

    def enter_secret(desired_secret: str): 
        """Enter the secret"""

    def clear_notifications(): 
        """Clear notifications and notification center on macOS"""

        
        
#     def inside_trip_graves():
#         actions.insert('```')
#         actions.insert('\n')
#         actions.insert('```')
#         actions.sleep("500ms")
#         actions.key("up")
#         actions.insert('\n')

