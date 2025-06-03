import importlib.util
import os
import time

from talon import Context, Module, actions, cron, ctrl
from talon_init import TALON_HOME
from user.talon_gaze_ocr.gaze_ocr_talon import move_cursor_to_gaze_point_helper

mod = Module()
state = {}
cron_jobs = {}
callbacks = {}
shush_start: float = 0

ctx = Context()
ctx.matches = r"""
mode: command
mode: dictation
"""


@ctx.action_class("user")
class UserActions:
    def noise_pop():
        print("python noise_tsk")
        actions.user.mouse_on_pop()

    def noise_tsk():
        print("python noise_tsk")
        if not last_command_is_sleep():
            actions.core.repeat_phrase()

    def noise_shush_start():
        global shush_start
        print("shush_start")
        previous_position = ctrl.mouse_pos()
        print("location before scroll")
        print(previous_position)

        move_cursor_to_gaze_point_helper()
        shush_start = time.perf_counter()
        actions.user.mouse_scroll_up_continuous()
        # ctrl.mouse_move(*previous_position)

    def noise_shush_stop():
        print("shush_start")
        actions.user.mouse_scroll_stop()

    def noise_hiss_start():
        global hiss_start
        print("hiss start")
        move_cursor_to_gaze_point_helper()
        hiss_start = time.perf_counter()
        actions.user.mouse_scroll_down_continuous()

    def noise_hiss_stop():
        actions.user.mouse_scroll_stop()


@mod.action_class
class Actions:
    def noise_debounce(name: str, active: bool):
        """Start or stop continuous noise using debounce"""
        if name not in state:
            state[name] = active
            cron_jobs[name] = cron.after("80ms", lambda: callback(name))
        elif state[name] != active:
            cron.cancel(cron_jobs[name])
            state.pop(name)

    def noise_pop():
        """Noise pop"""

    def noise_tsk():
        """Noise tsk"""

    def noise_shush_start():
        """Noise shush started"""

    def noise_shush_stop():
        """Noise shush stopped"""

    def noise_hiss_start():
        """Noise hiss started"""

    def noise_hiss_stop():
        """Noise hiss stopped"""


def last_command_is_sleep():
    try:
        cmd, _ = actions.core.last_command()
        return cmd.script.code.startswith("user.talon_sleep()")
    except Exception:
        return True


def callback(name: str):
    active = state.pop(name)
    callbacks[name](active)


def on_shush(active: bool):
    if active:
        actions.user.noise_shush_start()
    else:
        actions.user.noise_shush_stop()


def on_hiss(active: bool):
    if active:
        actions.user.noise_hiss_start()
    else:
        actions.user.noise_hiss_stop()


callbacks["shush"] = on_shush
callbacks["hiss"] = on_hiss
