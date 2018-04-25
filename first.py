# variables
f = 0


def somefunction():
    global f
    f = "def"
    print(f)


somefunction()
print(f)

# del f
print(f)
