from wrapper_qpy.decorators import TODO, va_args2, va_args
from wrapper_qpy.custom_classes import Mutable


@TODO
def WIN_DisableAltTab():
    pass


@TODO
def WIN_EnableAltTab():
    pass


@TODO
@va_args2(1)
def VID_Printf(print_level, msg):
    pass


@TODO
@va_args2(1)
def VID_Error(print_level, msg):
    pass


def MapKey(key):
    pass


def AppActivate(fActive, minimize):
    pass


def MainWndProc(hWnd, uMsg, wParam, lParam):
    pass


def VID_Restart_f():
    pass


def VID_Front_f():
    pass


def VID_GetModeInfo(width: Mutable, height: Mutable, mode):
    pass


def VID_UpdateWindowPosAndSize(x, y):
    pass


def VID_NewWindow(width, height):
    pass


def VID_FreeReflib():
    pass


def VID_LoadRefresh():
    pass


def VID_CheckChanges():
    pass


def VID_Init():
    pass


def VID_Shutdown():
    pass
