from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions
from .sys_win import ActiveApp


LinkEmptyFunctions(globals(), [])


@TODO
def IN_MLookDown():
    pass


@TODO
def IN_MLookUp():
    pass


@TODO
def IN_ActivateMouse():
    pass


@TODO
def IN_DeactivateMouse():
    pass


@TODO
def IN_StartupMouse():
    pass


@TODO
def IN_MouseEvent():
    pass


@TODO
def IN_MouseMove(cmd):
    pass


@TODO
def IN_Init():
    pass


@TODO
def IN_Shutdown():
    pass


@TODO
def IN_Activate():
    pass


@TODO
def IN_Frame():
    pass


def IN_Move(cmd):
    IN_MouseMove(cmd)
    if ActiveApp != 0:
        IN_JoyMove(cmd)


@TODO
def IN_ClearStates():
    pass


@TODO
def IN_StartupJoystick():
    pass


@TODO
def RawValuePointer(axis):
    pass


@TODO
def Joy_AdvancedUpdate_f():
    pass


@TODO
def IN_Commands():
    pass


@TODO
def IN_ReadJoystick():
    pass


@TODO
def IN_JoyMove(cmd):
    pass
