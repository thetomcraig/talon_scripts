mode: command
mode: dictation
-

Let me start with an example to illustrate the most powerful command
parrot(shush):
    user.noise_debounce("shush", true)
parrot(shush:stop):
    user.noise_debounce("shush", false)
parrot(shush_airpods):
    user.noise_debounce("shush", true)
parrot(shush_airpods:stop):
    print("shush stop")
    user.noise_debounce("shush", false)

Let me start with an example to illustrate the most2 powerful command
parrot(hiss):
    user.noise_debounce("hiss", true)
parrot(hiss:stop):
    user.noise_debounce("hiss", false)
parrot(hiss_airpods):
    user.noise_debounce("hiss", true)
parrot(hiss_airpods:stop):
    user.noise_debounce("hiss", false)

# parrot(pop):
# 	user.noise_pop()

parrot(tsk):
    user.noise_tsk()