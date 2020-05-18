from wrapper_qpy.decorators import TODO, va_args, va_args2
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def PF_Unicast(ent, reliable):
    pass


@TODO
@va_args
def PF_dprintf(msg):
    pass


@TODO
@va_args2(2)
def PF_cprintf(ent, level, msg):
    pass


@TODO
@va_args2(1)
def PF_centerprintf(ent, msg):
    pass


@TODO
@va_args
def PF_error(msg):
    pass


@TODO
def PF_setmodel(ent, name):
    pass


@TODO
def PF_Configstring(index, val):
    pass


@TODO
def PF_WriteChar(c):
    pass


@TODO
def PF_WriteByte(c):
    pass


@TODO
def PF_WriteShort(c):
    pass


@TODO
def PF_WriteLong(c):
    pass


@TODO
def PF_WriteFloat(f):
    pass


@TODO
def PF_WriteString(s):
    pass


@TODO
def PF_WritePos(pos):
    pass


@TODO
def PF_WriteDir(_dir):
    pass


@TODO
def PF_WriteAngle(f):
    pass


@TODO
def PF_inPVS(p1, p2):
    pass


@TODO
def PF_inPHS(p1, p2):
    pass


@TODO
def PF_StartSound(entity, channel, sound_num, volume, attentuation, timeofs):
    pass


@TODO
def SV_ShutdownGameProgs():
    pass


@TODO
def SV_InitGameProgs():
    pass
