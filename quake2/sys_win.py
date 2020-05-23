from wrapper_qpy.decorators import va_args, TODO
from wrapper_qpy.linker import LinkEmptyFunctions
from shared.QCrossPlatform import MessageBox
from shared.QConstants import NULL


LinkEmptyFunctions(globals(), ["Qcommon_Init"])

ActiveApp = 0


@va_args
def Sys_Error(error):
    MessageBox(NULL, text, "Error", 0)
    # TODO: check qwclsemaphore & DeinitConProc()
    exit(1)

@TODO
def Sys_Quit():
    pass


@TODO
def WinError():
    pass


@TODO
def Sys_ScanForCD():
    pass


def Sys_CopyProtect():
    pass


@TODO
def Sys_Init():
    pass


@TODO
def Sys_ConsoleInput():
    pass


@TODO
def Sys_ConsoleOutput(string):
    pass


@TODO
def Sys_SendKeyEvents():
    pass


@TODO
def Sys_GetClipboardData():
    pass


@TODO
def Sys_AppActivate():
    pass


@TODO
def Sys_UnloadGame():
    pass


@TODO
def Sys_GetGameAPI():
    pass


@TODO
def ParseCommandLine():
    pass


@TODO
def WinMain(argc, argv):
    Qcommon_Init(argc, argv)
    # TODO: continue from here
    return 1


from .common import Qcommon_Init
