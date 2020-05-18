from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def CL_ParseInventory():
    pass


@TODO
def Inv_DrawString():
    pass


def SetStringHighBit(s):
    for i in range(len(s)):
        s[i] = chr(ord(s[i]) | 128)


@TODO
def CL_DrawInventory():
    pass
