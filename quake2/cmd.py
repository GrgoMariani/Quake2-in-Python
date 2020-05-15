from shared.QClasses import sizebuf_t
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



def Cmd_Argc():
    return len(cmd_argv)


def Cmd_Argv(arg):
    if arg >= len(cmd_argv):
        return ""
    return cmd_argv[0]


def Cmd_AddCommand(cmd_name, function):

    pass


from .common import SZ_Init, SZ_Write, Com_Printf
