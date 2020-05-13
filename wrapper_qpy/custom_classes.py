
class Mutable:
    def __init__(self, value):
        self.x = [value]

    def GetMutable(self):
        return self.x[0]

    def SetMutable(self, value):
        self.x[0] = value

