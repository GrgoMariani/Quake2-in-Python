from wrapper_qpy.decorators import va_args

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
    # TODO: not finished
    pass


def Com_ServerState():
    return server_state


def Com_SetServerState(state):
    global server_state
    server_state = state


def Qcommon_Init(argc, argv):
    # TODO: not finished
    pass