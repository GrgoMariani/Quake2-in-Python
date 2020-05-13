from shared.QEnums import CVAR_ENUM
from .common import Com_Printf

class cvar_t:
    def __init__(self):
        self.name = ""
        self.string = ""
        self.latched_string = ""
        self.flags = 0
        self.modified = False
        self.value = 0.0
        self.next = None


cvar_vars = None


def Cvar_InfoValidate(s):
    if "\\" in s or "\"" in s or ";" in s:
        return False
    return True


def Cvar_FindVar(var_name):
    var = cvar_vars
    while var is not None:
        if var_name == var.name:
            return var
        var = var.next
    return None


def Cvar_VariableValue(var_name):
    var = Cvar_FindVar(var_name)
    if var is None:
        return 0
    return float(var.string)


def Cvar_VariableString(var_name):
    var = Cvar_FindVar(var_name)
    if var is None:
        return ""
    return var.string


def Cvar_CompleteVariable(partial):
    _len = len(partial)
    if _len == 0:
        return None
    cvar = cvar_vars
    while cvar is not None:
        if partial == cvar.name:
            return cvar.name
        cvar = cvar.next
    return None


def Cvar_Get(var_name, var_value, flags):
    if flags & (CVAR_ENUM.CVAR_USERINFO | CVAR_ENUM.CVAR_SERVERINFO):
        if not Cvar_InfoValidate(var_name):
            Com_Printf("invalid info cvar name")
            return None
    var = Cvar_FindVar(var_name)
    if var is not None:
        var.flags = var.flags | flags
        return var
    if var_value is None:
        return None
    if flags & (CVAR_ENUM.CVAR_USERINFO | CVAR_ENUM.CVAR_SERVERINFO)
        if not Cvar_InfoValidate(var_value):
            Com_Printf("invalid info cvar value")
            return None
    # TODO: Z_Malloc
    # var = Z_Malloc(sizeof(var))
