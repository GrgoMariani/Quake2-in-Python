from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


MAX_OSPATH = 128

fs_gamedir = ""


def FS_Gamedir():
    return fs_gamedir


@TODO
def FS_ExecAutoexec():
    pass


@TODO
def FS_SetGameDir(_dir):
    pass

