
class ani:
    def __init__(self) -> None:
        pass
        
    def mymethod(self):
        print("animal makes a sound")
class dog(ani):
    def mymethod(self):
        print("dog makes a sound")
class bird(ani):
    def mymethod(self):
        print("bird makes a sound")
ani1 = ani()
dog1 = dog()
bird1 = bird()

ani1.mymethod()
dog1.mymethod()
bird1.mymethod()