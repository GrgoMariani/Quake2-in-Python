from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def Draw_InitLocal():
    pass


@TODO
def Draw_Char(x, y, num):
    pass


@TODO
def Draw_FindPic(name):
    pass


@TODO
def Draw_GetPicSize(w: Mutable, h: Mutable, pic):
    pass


@TODO
def Draw_StretchPic(x, y, w, h, pic):
    pass


@TODO
def Draw_Pic(x, y, pic):
    pass


@TODO
def Draw_TileClear(x, y, w, h, pic):
    pass


@TODO
def Draw_Fill(x, y, w, h, c):
    pass


@TODO
def Draw_FadeScreen():
    pass


@TODO
def Draw_StretchRaw(x, y, w, h, cols, rows, data):
    pass
