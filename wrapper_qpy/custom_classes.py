
class Mutable:
    def __init__(self, value):
        self.x = [value]

    def GetValue(self):
        return self.x[0]

    def SetValue(self, value):
        self.x[0] = value

