from wrapper_qpy.decorators import va_args, TODO
from shared.QEnums import ERROR_LVL
from .reference_import import gi
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def ShutdownGame():
    pass


@TODO
def GetGameAPI(_import):
    pass


@va_args
def Sys_Error(error):
    gi.error(ERROR_LVL.ERR_FATAL, "%s", error)


@va_args
def Com_Printf(msg):
    gi.dprintf("%s", msg)


@TODO
def ClientEndServerFrames():
    pass


@TODO
def CreateTargetChangeLevel(map):
    pass


@TODO
def EndDMLevel():
    pass


@TODO
def CheckDMRules():
    pass


@TODO
def ExitLevel():
    pass


@TODO
def G_RunFrame():
    pass
