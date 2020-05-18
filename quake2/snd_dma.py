from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def S_SoundInfo_f():
    pass


@TODO
def S_Init():
    pass


@TODO
def S_Shutdown():
    pass


@TODO
def S_FindName():
    pass


@TODO
def S_AliasName(aliasname, truename):
    pass


@TODO
def S_BeginRegistration():
    pass


@TODO
def S_RegisterSound(name):
    pass


@TODO
def S_EndRegistration():
    pass


@TODO
def S_PickChannel(entnum, entchannel):
    pass


@TODO
def S_SpatializeOrigin(origin, master_vol, dist_mult, left_vol: Mutable, right_vol: Mutable):
    pass


@TODO
def S_Spatialize(ch):
    pass


@TODO
def S_AllocPlaysound():
    pass


@TODO
def S_FreePlaysound(ps):
    pass


@TODO
def S_IssuePlaysound(ps):
    pass


@TODO
def S_RegisterSexedSound(ent, base):
    pass


@TODO
def S_StartSound(origin, entnum, entchannel, sfx, fvol, attenuation, timeofs):
    pass


@TODO
def S_StartLocalSound(sound):
    pass


@TODO
def S_ClearBuffer():
    pass


@TODO
def S_StopAllSounds():
    pass


@TODO
def S_AddLoopSounds():
    pass


@TODO
def S_RawSamples(samples, rate, width, channels, data):
    pass


@TODO
def S_Update(origin, forward, right, up):
    pass


@TODO
def GetSoundtime():
    pass


@TODO
def S_Update_():
    pass


@TODO
def S_Play():
    pass


@TODO
def S_SoundList():
    pass
