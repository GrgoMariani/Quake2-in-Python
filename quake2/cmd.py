from shared.QClasses import sizebuf_t
from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions

LinkEmptyFunctions(globals(), ["SZ_Init", "SZ_Write", "Com_Printf"])

MAX_ALIAS_NAME = 32
ALIAS_LOOP_COUNT = 16

cmd_wait = False
cmd_argv = []


def Cmd_Wait_f():
    global cmd_wait
    cmd_wait = True

cmd_text = sizebuf_t()
cmd_text_buf = ""


def Cbuf_Init():
    SZ_Init(cmd_text, cmd_text_buf, 8192)


def Cbuf_AddText(text):
    if cmd_text.cursize + len(text) >= cmd_text.maxsize:
        Com_Printf("Cbuf_AddText: overflow\n")
        return
    SZ_Write(cmd_text, text, len(text))


def Cbuf_InsertText(text):
    templen = cmd_text.cursize
    if templen > 0:
        temp = cmd_text.data
    else:
        temp = None
    Cbuf_AddText(text)
    if templen > 0:
        SZ_Write(cmd_text, temp, templen)


@TODO
def Cbuf_CopyToDefer():
    pass


@TODO
def Cbuf_InsertFromDefer():
    pass


@TODO
def Cbuf_ExecuteText(exec_when, text):
    pass


@TODO
def Cbuf_Execute():
    pass


@TODO
def Cbuf_AddEarlyCommands(clear):
    pass


@TODO
def Cbuf_AddLateCommands():
    pass


@TODO
def Cmd_Exec_f():
    pass


@TODO
def Cmd_Echo_f():
    pass


@TODO
def Cmd_Alias_f():
    pass


def Cmd_Argc():
    return len(cmd_argv)


def Cmd_Argv(arg):
    if arg >= len(cmd_argv):
        return ""
    return cmd_argv[0]


@TODO
def Cmd_MacroExpandString(text):
    pass


@TODO
def Cmd_TokenizeString(text, macroExpand):
    pass


@TODO
def Cmd_AddCommand(cmd_name, function):
    pass


@TODO
def Cmd_RemoveCommand(cmd_name):
    pass


@TODO
def Cmd_Exists(cmd_name):
    pass


@TODO
def Cmd_CompleteCommand(partial):
    pass


@TODO
def Cmd_ExecuteString(text):
    pass


@TODO
def Cmd_List_f():
    pass


def Cmd_Init():
    Cmd_AddCommand("cmdlist", Cmd_List_f)
    Cmd_AddCommand("exec", Cmd_Exec_f)
    Cmd_AddCommand("echo", Cmd_Echo_f)
    Cmd_AddCommand("alias", Cmd_Alias_f)
    Cmd_AddCommand("wait", Cmd_Wait_f)


from .common import SZ_Init, SZ_Write, Com_Printf
