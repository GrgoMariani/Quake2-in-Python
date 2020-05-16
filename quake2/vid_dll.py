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


@TODO
def MapKey(key):
    pass


@TODO
def AppActivate(fActive, minimize):
    pass


@TODO
def MainWndProc(hWnd, uMsg, wParam, lParam):
    pass


@TODO
def VID_Restart_f():
    pass


@TODO
def VID_Front_f():
    pass


@TODO
def VID_GetModeInfo(width: Mutable, height: Mutable, mode):
    pass


@TODO
def VID_UpdateWindowPosAndSize(x, y):
    pass


@TODO
def VID_NewWindow(width, height):
    pass


@TODO
def VID_FreeReflib():
    pass


@TODO
def VID_LoadRefresh():
    pass


@TODO
def VID_CheckChanges():
    pass


@TODO
def VID_Init():
    pass


@TODO
def VID_Shutdown():
    pass
