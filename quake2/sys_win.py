from wrapper_qpy.decorators import va_args
from .common import Qcommon_Init
from shared.QCrossPlatform import MessageBox
from shared.QConstants import NULL


@va_args
def Sys_Error(error):
    MessageBox(NULL, text, "Error", 0)
    # TODO: check qwclsemaphore & DeinitConProc()
    exit(1)


def WinMain(argc, argv):
    Qcommon_Init(argc, argv)
    # TODO: continue from here
    return 1