from wrapper_qpy.decorators import va_args
from shared.QEnums import ERROR_LVL
from .reference_import import gi



@va_args
def Sys_Error(error):
    gi.error(ERROR_LVL.ERR_FATAL, "%s", error)

@va_args
def Com_Printf(msg):
    gi.dprintf("%s", msg)
