class Sun:
    __instance = None
    def __init__(self):
        if Sun.__instance != None:
            print("Exists!!!")
        else:
            Sun.__instance = self
    def inst():
        if Sun.__instance == None:
            Sun()
        return Sun.__instance

a = Sun.inst()
b = Sun.inst()
print(a is b)
