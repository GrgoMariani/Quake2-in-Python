class Mutable:
    """
    A lot of variables are passed through arguments, which can cause problems to python immutable types
    ( like string and int ). This is why we must see if the arguments of this type should be actually passed
    as immutable.
    The usecase should be simple: if a function expects an immutable we should first set it and on return we should
    get the returned value.
    Although this is a workaround it should not be that complicated to use
    """
    def __init__(self, value):
        self.x = [value]

    def GetValue(self):
        return self.x[0]

    def SetValue(self, value):
        self.x[0] = value
