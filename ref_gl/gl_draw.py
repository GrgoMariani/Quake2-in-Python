from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.linker import LinkEmptyFunctions
from shared.QEnums import imagetype_t
from shared.QConstants import MAX_QPATH


LinkEmptyFunctions(globals(), ["Com_sprintf", "GL_FindImage"])


@TODO
def Draw_InitLocal():
    pass


@TODO
def Draw_Char(x, y, num):
    pass


def Draw_FindPic(name):
    gl = None
    fullname = Mutable("")
    if name[0] != "/" and name[0] != "\\":
        Com_sprintf(Mutable, MAX_QPATH, "pics/%s.pcx", name)
        gl = GL_FindImage(fullname.GetValue(), imagetype_t.it_pic)
    else:
        gl = GL_FindImage(fullname.GetValue(), imagetype_t.it_pic)
    return gl


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

from .q_shared import Com_sprintf
from .gl_image import GL_FindImage