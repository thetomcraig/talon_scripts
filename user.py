from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

@ctx.action_class("user")
class UserActions:
    def select_dont_save():
        actions.key("space")


def disable():
    actions.speech.disable()

app.register("ready", disable)

@mod.action_class
class Actions:
    def select_dont_save():
        """Select "don't save" from the dialog"""

#     def inside_trip_graves():
#         actions.insert('```')
#         actions.insert('\n')
#         actions.insert('```')
#         actions.sleep("500ms")
#         actions.key("up")
#         actions.insert('\n')
