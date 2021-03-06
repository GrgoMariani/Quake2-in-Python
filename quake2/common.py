from wrapper_qpy.decorators import va_args, va_args2, static_vars, TODO
from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.linker import LinkEmptyFunctions
from shared.QEnums import ERROR_LVL


LinkEmptyFunctions(globals(), ["Con_Print", "Com_sprintf", "va", "FS_Gamedir", "CL_Drop", "CL_Shutdown", "SV_Shutdown",
                               "Sys_ConsoleOutput", "Sys_Error"])

MAXPRINTMSG = 4096
MAX_NUM_ARGVS = 50
MAX_QPATH = 64

com_argv = list()

realtime = 0

host_speeds = None
log_stats = None
developer = None
timescale = None
fixedtime = None
logfile_active = None
showtrace = None
dedicated = None

logfile = None

rd_target = 0
rd_buffer = None
rd_buffersize = 0
rd_flush = None

server_state = 0


def Com_BeginRedirect(target, buffer, buffersize, flush):
    global rd_target, rd_buffer, rd_buffersize, rd_flush
    if not target or not buffer or not buffersize or not flush:
        return
    rd_target, rd_buffer, rd_buffersize, rd_flush = target, buffer, buffersize, flush


def Com_EndRedirect():
    global rd_target, rd_buffer, rd_buffersize, rd_flush
    rd_flush(rd_target, rd_buffer)
    rd_target = 0
    rd_buffer = None
    rd_buffersize = 0
    rd_flush = None


@va_args
def Com_Printf(msg):
    global rd_buffer
    if rd_target > 0:
        if len(msg) + len(rd_buffer) > rd_buffersize -1:
            rd_flush(rd_target, rd_buffer)
        rd_buffer = msg
        return
    Con_Print(msg)
    Sys_ConsoleOutput(msg)
    if logfile_active is not None and logfile_active.value > 0:
        global logfile
        if logfile is None:
            name = Mutable()
            Com_sprintf(name, MAX_QPATH, "%s/qconsole.log", FS_Gamedir())
            logfile = open(name.GetValue(), "w")
        else:
            logfile.print(msg)
        if logfile_active.value > 1:
            logfile.flush()


def Com_DPrintf(msg):
    if developer is None or developer.value == 0:
        return
    Con_Print("%s", msg)



@va_args2(1)
@static_vars(recursive=False)
def Com_Error(code, msg):
    if Com_Error.recursive:
        Sys_Error("recursive error after: %s", msg)
    Com_Error.recursive = True
    if code == ERROR_LVL.ERR_DISCONNECT:
        CL_Drop()
        Com_Error.recursive = False
        # TODO: abortframe longjmp
    elif code == ERROR_LVL.ERR_DROP:
        Com_Printf("********************\nERROR: %s\n********************\n", msg)
        SV_Shutdown(va("Server crashed: %s\n", msg), False)
        CL_Drop()
        Com_Error.recursive = False
        # TODO: abortframe longjmp
    else:
        SV_Shutdown(va("Server fatal crashed: %s\n", msg), False)
        CL_Shutdown()
    global logfile
    if logfile is not None:
        logfile.flush()
        logfile.close()
        logfile = None
    Sys_Error("%s", msg)


@TODO
def Com_Quit():
    pass


def Com_ServerState():
    return server_state


def Com_SetServerState(state):
    global server_state
    server_state = state


@TODO
def MSG_WriteChar():
    pass


@TODO
def MSG_WriteByte():
    pass


@TODO
def MSG_WriteShort():
    pass


@TODO
def MSG_WriteLong():
    pass


@TODO
def MSG_WriteFloat():
    pass


@TODO
def MSG_WriteString():
    pass


@TODO
def MSG_WriteCoord():
    pass


@TODO
def MSG_WritePos():
    pass


@TODO
def MSG_WriteAngle():
    pass


@TODO
def MSG_WriteAngle16():
    pass


@TODO
def MSG_WriteDeltaUsercmd(buf, _from, cmd):
    pass


@TODO
def MSG_WriteDir():
    pass


@TODO
def MSG_ReadDir():
    pass


@TODO
def MSG_WriteDeltaEntity():
    pass


@TODO
def MSG_BeginReading():
    pass


@TODO
def MSG_ReadChar():
    pass


@TODO
def MSG_ReadByte():
    pass


@TODO
def MSG_ReadShort():
    pass


@TODO
def MSG_ReadLong():
    pass


@TODO
def MSG_ReadFloat():
    pass


@TODO
def MSG_ReadString():
    pass


@TODO
def MSG_ReadStringLine():
    pass


@TODO
def MSG_ReadCoord():
    pass


@TODO
def MSG_ReadPos():
    pass


@TODO
def MSG_ReadAngle():
    pass

@TODO
def MSG_ReadAngle16():
    pass

@TODO
def MSG_ReadDeltaUsercmd():
    pass

@TODO
def MSG_ReadData():
    pass


@TODO
def SZ_Init(buf, data, length):
    pass


@TODO
def SZ_Clear(buf):
    pass


@TODO
def SZ_GetSpace(buf, length):
    pass


@TODO
def SZ_Write(buf, data, length):
    pass


@TODO
def SZ_Print(buf, data):
    pass


@TODO
def COM_CheckParm(parm):
    pass


@TODO
def COM_Argc():
    pass


@TODO
def COM_Argv():
    pass


@TODO
def COM_ClearArgv(argc, argv):
    pass


@TODO
def COM_InitArgv():
    pass


@TODO
def COM_AddParm(parm):
    pass


@TODO
def memsearch(start, count, search):
    pass


@TODO
def CopyString(_in):
    pass


@TODO
def Info_Print(s):
    pass


@TODO
def Z_Free(ptr):
    pass


@TODO
def Z_Stats_f():
    pass


@TODO
def Z_FreeTags(tag):
    pass


@TODO
def Z_TagMalloc(size, tag):
    pass


@TODO
def Z_Malloc(size):
    return Z_TagMalloc(size, 0)


@TODO
def COM_BlockSequenceCheckByte(base, length, sequence, challenge):
    pass


@TODO
def COM_BlockSequenceCRCByte(base, length, sequence):
    pass


@TODO
def frand():
    pass


@TODO
def crand():
    pass


@TODO
def Com_Error_f():
    pass


@TODO
def Qcommon_Init(argc, argv):
    pass


@TODO
def Qcommon_Frame(msec):
    pass


def Qcommon_Shutdown():
    pass


from .sys_win import Sys_ConsoleOutput, Sys_Error
from .console import Con_Print
from .q_shared import Com_sprintf, va
from .files import FS_Gamedir
from .cl_main import CL_Drop, CL_Shutdown
from .sv_main import SV_Shutdown