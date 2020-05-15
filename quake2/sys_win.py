from wrapper_qpy.decorators import va_args
from shared.QCrossPlatform import MessageBox
from shared.QConstants import NULL

from wrapper_qpy.linker import LinkEmptyFunctions

LinkEmptyFunctions(globals(), ["Qcommon_Init"])


@va_args
def Sys_Error(error):
    MessageBox(NULL, text, "Error", 0)
    # TODO: check qwclsemaphore & DeinitConProc()
    exit(1)


def Sys_ConsoleOutput(string):
    pass


def WinMain(argc, argv):
    Qcommon_Init(argc, argv)
    # TODO: continue from here
    return 1


from .common import Qcommon_Init
