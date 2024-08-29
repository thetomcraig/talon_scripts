import os

from talon import Context, Module, actions, app, ctrl, noise
from talon_plugins import eye_zoom_mouse
from user.talon_gaze_ocr.gaze_ocr_talon import move_cursor_to_gaze_point_helper

ctx = Context()

# For disabling the built in pop to click/pop to zoom functionality
# One of my keyboards triggers this and I haven't figured out to
# properly replace with a parrot sound yet
DISABLE_BUILT_IN_POP_CLICK = False
if DISABLE_BUILT_IN_POP_CLICK is True:
    @ctx.action_class("tracking")
    class TrackingActions:
        def control_zoom_toggle(state: bool=False):
                actions.next(state)
                if state:
                    # Unregistered zoom mouse built in pop event.
                    noise.unregister("pop", eye_zoom_mouse.zoom_mouse.on_pop)


mod = Module()

def get_secret(desired_value: str):
    """
    Helper function to get secrets in a local csv file.
    File should be CSV file in THIS directory, and look like:
        secretName,secretValue
    """
    secret_dict = {}
    user_dir_path = os.path.join(os.getcwd(), 'user', 'talon_scripts')

    with open(os.path.join(user_dir_path, 'secrets.csv'), 'r') as f:
        for line in f.readlines():
            key, value = line.strip().split(',')
            secret_dict[key] = value

    return secret_dict[desired_value]

@ctx.action_class("user")
class UserActions:
    def debugging():
        # print(os.getcwd())
        # actions.app.notify("Debug")
        print(ctrl.mouse_pos())
        
        move_cursor_to_gaze_point_helper()
        print(ctrl.mouse_pos())


    def sleep_talon():
        actions.tracking.control_zoom_toggle(False)
        actions.speech.disable()
        actions.app.notify("Talon asleep")

    def sleep_eye_tracker():
        actions.tracking.control_zoom_toggle(False)
        actions.app.notify("Eye tracking asleep")

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



#####################
# App startup setup #
#####################
# AI Tools
os.environ["OPENAI_API_KEY"] = get_secret("openai_api_key")
app.register("ready", disable)
