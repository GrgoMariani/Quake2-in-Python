from shared.QEnums import CVAR_ENUM
from .common import Com_Printf, Com_ServerState
from .q_shared import Com_sprintf, Info_SetValueForKey
from .files import FS_ExecAutoexec, FS_SetGameDir
from .cmd import Cmd_Argc, Cmd_Argv, Cmd_AddCommand
from wrapper_qpy.custom_classes import Mutable


class cvar_t:
    def __init__(self):
        self.name = ""
        self.string = ""
        self.latched_string = ""
        self.flags = 0
        self.modified = False
        self.value = 0.0
        self.next = None


cvar_vars = dict()


def Cvar_InfoValidate(s):
    if "\\" in s or "\"" in s or ";" in s:
        return False
    return True


def Cvar_FindVar(var_name):
    if var_name in cvar_vars.keys():
        return cvar_vars[var_name]
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
    if partial in cvar_vars.keys():
        return partial
    for cvar in cvar_vars:
        if cvar.name[0:len(partial)] == partial:
            return cvar_vars[partial].name
    return None


def Cvar_Get(var_name, var_value, flags):
    global cvar_vars
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
    var = cvar_t()
    var.name = var_name
    var.string = val_value
    var.modified = True
    var.value = float(var.string)
    var.flags = flags
    cvar_vars[var_name] = var
    return var


userinfo_modified = False

def Cvar_Set2(var_name, value, force):
    var = Cvar_FindVar(var_name)
    if var is None:
        return Cvar_Get(var_name, value, 0)
    if var.flags & (CVAR_ENUM.CVAR_USERINFO | CVAR_ENUM.CVAR_SERVERINFO):
        if not Cvar_InfoValidate(value):
            Com_Printf("invalid info cvar value\n")
            return var
    if not force:
        if var.flags & CVAR_ENUM.CVAR_NOSET:
            Com_Printf("%s is write protected.\n", var_name)
            return var
        if var.flags & CVAR_ENUM.CVAR_LATCH:
            if len(var.latched_string) > 0:
                if value == var.latched_string:
                    return var
            else:
                if value == var.string
                    return var
            if Com_ServerState():
                Com_Printf("%s will be changed for next game.\n", var_name)
                var.latched_string = value
            else:
                var.string = value
                var.value = float(var.string)
                if var.name == "game":
                    FS_SetGameDir(var.string)
                    FS_ExecAutoexec()
            return var
    else:
        if len(var.latched_string) > 0:
            var.latched_string = 0
    if var.string == value:
        return var
    var.modified = True
    if var.flags & CVAR_ENUM.CVAR_USERINFO:
        global userinfo_modified
        userinfo_modified = True
    var.string = value
    var.value = float(var.string)
    return var


def Cvar_ForceSet(var_name, value):
    return Cvar_Set2(var_name, value, True)


def Cvar_Set(var_name, value):
    return Cvar_Set2(var_name, value, False)


def Cvar_FullSet(var_name, value, flags):
    var = Cvar_FindVar(var_name)
    if var is None:
        return Cvar_Get(var_name, value, flags)
    var.modified = True
    if var.flags & CVAR_ENUM.CVAR_USERINFO:
        global userinfo_modified
        userinfo_modified = True
    var.string = value
    var.value = float(var.string)
    var.flags = flags
    return var


def Cvar_SetValue(var_name, value):
    val = Mutable("")
    if value == int(value):
        Com_sprintf(val, 32, "%i", int(value))
    else:
        Com_sprintf(val, 32, "%f", value)
    Cvar_Set(var_name, val.GetValue())


def Cvar_GetLatchedVars()
    for var in cvar_vars:
        if len(var.latched_string) == 0:
            continue
        var.string = var.latched_string
        var.latched_string = ""
        var.value = float(var.string)
        if var.name == "game":
            FS_SetGameDir(var.string)
            FS_ExecAutoexec()

def Cvar_Command():
    v = Cvar_FindVar(Cmd_Argv(0))
    if v is None:
        return False
    if Cmd_Argc() == 1:
        Com_Printf("\"%s\" is \"%s\"\n", v.name, v.string)
        return True
    Cvar_Set(v.name, Cmd_Argv(1))
    return True


def Cvar_Set_f():
    flags = 0
    c = Cmd_Argc()
    if c not in [3, 4]:
        Com_Printf("usage: set <variable> <value> [u / s]\n")
        return
    if c == 4:
        if Cmd_Argv(3) == "u":
            flags = CVAR_ENUM.CVAR_USERINFO
        elif Cmd_Argv(3) == "s":
            flags = CVAR_ENUM.CVAR_SERVERINFO
        else:
            Com_Printf("flags can only be 'u' or 's'\n")
            return
        Cvar_FullSet(Cmd_Argv(1), Cmd_Argv(2), flags)
    else:
        Cvar_Set(Cmd_Argv(1), Cmd_Argv(2))


def Cvar_WriteVariables(path):
    buffer = Mutable()
    with open(path, "a") as f:
        for var in cvar_vars:
            if var.flags & CVAR_ENUM.CVAR_ARCHIVE:
                Com_sprintf(buffer, 1024, "set %s \"%s\"\n", var.name, var.string)
                f.write(buffer.GetValue())


def Cvar_List_f():
    for var in cvar_vars:
        if var.flags & CVAR_ENUM.CVAR_ARCHIVE:
            Com_Printf("*")
        else:
            Com_Printf(" ")
        if var.flags & CVAR_ENUM.CVAR_USERINFO:
            Com_Printf("U")
        else:
            Com_Printf("*")
        if var.flags & CVAR_ENUM.CVAR_SERVERINFO:
            Com_Printf("S")
        else:
            Com_Printf("*")
        if var.flags & CVAR_ENUM.CVAR_NOSET:
            Com_Printf("-")
        elif var.flags & CVAR_ENUM.CVAR_LATCH:
            Com_Printf("L")
        else:
            Com_Printf("*")
        Com_Printf (" %s \"%s\"\n", var.name, var.string)
    Com_Printf("%i cvars\n", i)


def Cvar_BitInfo(bit):
    info = Mutable()
    for var in cvar_vars:
        if var.flags & bit:
            Info_SetValueForKey(info, var.name, var.string)
    return info.GetValue()


def Cvar_Userinfo():
    return Cvar_BitInfo(CVAR_ENUM.CVAR_USERINFO)


def Cvar_Serverinfo():
    return Cvar_BitInfo(CVAR_ENUM.CVAR_SERVERINFO)


def Cvar_Init():
    Cmd_AddCommand("set", Cvar_Set_f)
    Cmd_AddCommand("cvarlist", Cvar_List_f)
