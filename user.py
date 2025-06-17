import os

from talon import Context, Module, actions, app, noise, ui
from talon_plugins import eye_zoom_mouse

ctx = Context()

# For disabling the built in pop to click/pop to zoom functionality
# One of my keyboards and airpods sometimes trigger this and I haven't figured out to
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

def read_csv_to_dict(file_path: str):
    """
    Read CSV files that are in the talon scripts directory
    """
    data_dict = {}
    user_dir_path = os.path.join(os.getcwd(), 'user', 'talon_scripts')
    with open(os.path.join(user_dir_path, file_path), 'r') as f:
        for line in f.readlines():
            if not line.strip():
                continue
            key, value = line.strip().split(',')
            data_dict[key] = value
    return data_dict


def get_secret(desired_value: str):
    secret_dict = read_csv_to_dict('secrets.csv')
    return secret_dict[desired_value]


def get_project_root_folder_name(desired_value: str):
    # TODO use the words to replace here to prevent a misspeaks
    folders = read_csv_to_dict('vscode_project_names.csv') 
    return folders.get(desired_value, desired_value)

@ctx.action_class("user")
class UserActions:
    def debugging():
        # print(os.getcwd())
        # actions.app.notify("Debug")
        # print(actions.win.title())
        # print(dir(actions.win))
        pass

    def calibrate_eye_tracker():
        actions.tracking.calibrate()

    def sleep_talon():
        actions.tracking.control_zoom_toggle(False)
        actions.speech.disable()
        actions.app.notify("Talon asleep")

    def sleep_eye_tracker():
        actions.tracking.control_zoom_toggle(False)
        actions.app.notify("Eye tracking asleep")

    def wake_eye_tracker():
        actions.tracking.control_zoom_toggle(True)
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

    def repeat_last_command():
        """Repeat the last talon command"""
        actions.core.repeat_phrase()

    def select_dont_save():
        actions.key("space")

    def show_preferences():
        actions.key("cmd-,")

    def clear_notifications():
        """Using this in conjunction with BetterTouchTool, no solution using AppleScript worked"""
        actions.key("cmd-ctrl-shift-n")

    def open_winnow_jira_task(task_number: int): 
        """Open a winnow jira task"""
        actions.user.open_url(f"https://ayadev.atlassian.net/browse/WIN-{task_number}")

    def insert_winnow_jira_number(task_number: int): 
        """Paste a winnow jira number"""
        actions.insert(f"https://ayadev.atlassian.net/browse/WIN-{task_number}")
        actions.sleep("50ms")

    def open_vscode_project(project_name: str): 
        """
        Switch to the open vscode window for the project "project_name".
        We accomplish this by invoking the vscode project manager extension,
        and putting in the project_name.

        Caveat 1: if project_name is already in the frontmost vscode window,
        the project manager extension will not list it as an option.
        So we need to check if project_name is already open in the frontmost window.
        VSCode and the project manager extension do not provide an API for this, so

        There is no easy way to do this built into VSCode, so have to leverage the title of the window.
        In my window.title settings, I have the root name of the folder in the title and use the separator " | "
        The title settings look like this:
            ${activeEditorShort}${separator}${rootName}${separator}${profileName}${separator}focus:[${focusedView}]
        So, use talon to get the window title
        """
        # Find the name of the root folder associated with the project
        # This is the project that we want to switch to
        root_folder_name = get_project_root_folder_name(project_name)

        # If VSCode is already the front most app, do nothing.
        # The default behavior would be to switch to the next window of vscode,
        # but I don't want to do that here because it would be jarring the user
        app = actions.user.get_running_app("Code")
        if app != ui.active_app():
            actions.user.switcher_focus_app(app)

        # Access the root folder of the currently opened project based on the window title
        # This is based on the window.title settings in VSCode
        # These are mine
            # ${activeEditorShort}${separator}${rootName}${separator}${profileName}${separator}focus:[${focusedView}]
            # With separator: " | "
        root_folder_for_current_project = actions.win.title().split(" | ")[1].strip()
        if root_folder_for_current_project == root_folder_name:
            # The front most project in VSCode is the one that we want, do nothing
            return

        actions.sleep("50ms") 
        actions.user.vscode("projectManager.listProjects")
        actions.sleep("50ms")
        actions.insert(project_name)
        actions.sleep("50ms")
        actions.key("enter")


def disable():
    actions.speech.disable()
@mod.action_class
class Actions:
    def calibrate_eye_tracker():
        """Calibrate the eye tracker"""

    def sleep_talon():
        """Sleep talon"""

    def sleep_eye_tracker():
        """Sleep the eye tracker"""

    def sleep_all():
        """Sleep the computer and talon"""

    def debugging():
        """Where I debug stuff"""

    def repeat_last_command():
        """Repeat the last talon command"""

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

    def open_winnow_jira_task(task_number: int): 
        """Open a winnow jira task"""

    def insert_winnow_jira_number(task_number: int): 
        """Paste a winnow jira number"""

    def open_vscode_project(project_name: str): 
        """Open a vscode project"""



#####################
# App startup setup #
#####################
# AI Tools
os.environ["OPENAI_API_KEY"] = get_secret("openai_api_key")
app.register("ready", disable)
