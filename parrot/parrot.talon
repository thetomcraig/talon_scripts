mode: command
mode: dictation
-

parrot(shush):
    print("shush start")
    user.noise_debounce("shush", true)
parrot(shush:stop):
    print("shush stop")
    user.noise_debounce("shush", false)
# parrot(shush_airpods):
#     print("shush airpods start")
#     user.noise_debounce("shush", true)
# parrot(shush_airpods:stop):
#     print("shush airpods stop")
#     user.noise_debounce("shush", false)

# parrot(hiss):
#     print("hiss start")
#     user.noise_debounce("hiss", true)
# parrot(hiss:stop):
#     print("hiss stop")
#     user.noise_debounce("hiss", false)
# parrot(hiss_airpods):
#     print("hiss airpods start")
#     user.noise_debounce("hiss", true)
# parrot(hiss_airpods:stop):
#     print("hiss airpods stop")
#     user.noise_debounce("hiss", false)

# parrot(pop_1_airpods):
#     print("pop start")
# 	user.noise_pop()

# parrot(tsk):
#     print("tsk start")
#     user.noise_tsk()