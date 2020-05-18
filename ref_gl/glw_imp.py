from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def VerifyDriver():
    pass


@TODO
def VID_CreateWindow(width, height, fullscreen):
    pass


@TODO
def GLimp_SetMode(pwidth: Mutable, pheight: Mutable, mode, fullscreen):
    pass


@TODO
def GLimp_Shutdown():
    pass


@TODO
def GLimp_Init(hinstance, wndproc):
    pass


@TODO
def GLimp_InitGL():
    pass


@TODO
def GLimp_BeginFrame(camera_separation):
    pass


@TODO
def GLimp_EndFrame():
    pass


@TODO
def GLimp_AppActivate(active):
    pass
