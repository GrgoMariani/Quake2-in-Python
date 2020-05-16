from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.decorators import va_args, TODO
from shared.QEnums import ERROR_LVL, PRINT_LVL
from .reference_import import ri



@va_args
def SysError(error):
    ri.Sys_error(ERROR_LVL.ERR_FATAL, error)


@va_args
def Com_Printf(fmt):
    ri.Con_Printf(PRINT_LVL.PRINT_ALL, fmt)
