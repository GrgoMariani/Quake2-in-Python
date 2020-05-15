from wrapper_qpy.decorators import va_args, va_args2, static_vars
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


def SZ_Init(buf, data, length):
    pass


def SZ_Write(buf, data, length):
    pass


def Com_ServerState():
    return server_state


def Com_SetServerState(state):
    global server_state
    server_state = state


def Qcommon_Init(argc, argv):
    # TODO: not finished
    pass



from .sys_win import Sys_ConsoleOutput, Sys_Error
from .console import Con_Print
from .q_shared import Com_sprintf, va
from .files import FS_Gamedir
from .cl_main import CL_Drop, CL_Shutdown
from .sv_main import SV_Shutdown