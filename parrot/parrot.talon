mode: command
mode: dictation
-


parrot(shush):
    print("shush start")
    user.noise_debounce("shush", true)
parrot(shush:stop):
    print("shush stop")
    user.noise_debounce("shush", false)

parrot(hiss):
    print("hiss start")
    user.noise_debounce("hiss", true)
parrot(hiss:stop):
    print("hiss stop")
    user.noise_debounce("hiss", false)

parrot(pop):
	user.noise_pop()

parrot(tsk):
    user.noise_tsk()