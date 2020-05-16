from wrapper_qpy.decorators import TODO, va_args2, va_args



@TODO
def SV_FlushRedirect(sv_redirected, outputbug):
    pass


@TODO
@va_args2(2)
def SV_ClientPrintf(cl, level, string):
    pass


@TODO
@va_args2(1)
def SV_BroadcastPrintf(level, string):
    pass


@TODO
@va_args
def SV_BroadcastCommand(string):
    pass


@TODO
def SV_Multicast(origin, _to):
    pass


@TODO
def SV_StartSound(origin, entity, channel, soundindex, volume, attentuation, timeofs):
    pass


@TODO
def SV_SendClientDatagram(client):
    pass


@TODO
def SV_DemoCompleted():
    pass


@TODO
def SV_RateDrop(c):
    pass


@TODO
def SV_SendClientMessages():
    pass
