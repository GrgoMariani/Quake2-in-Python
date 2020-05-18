from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.decorators import va_args, TODO
from shared.QEnums import ERROR_LVL, PRINT_LVL
from .reference_import import ri
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def R_CullBox(mins, maxs):
    pass


@TODO
def R_RotateForEntity(e):
    pass


@TODO
def R_DrawSpriteModel(e):
    pass


@TODO
def R_DrawNullModel():
    pass


@TODO
def R_DrawEntitiesOnList():
    pass


@TODO
def GL_DrawParticles(num_particles, particles, colortable):
    pass


@TODO
def R_DrawParticles():
    pass


@TODO
def R_PolyBlend():
    pass


@TODO
def SignbitsForPlane(out):
    pass


@TODO
def R_SetFrustum():
    pass


@TODO
def R_SetupFrame():
    pass


@TODO
def R_SetupGL():
    pass


@TODO
def R_Clear():
    pass


@TODO
def R_Flash():
    pass


@TODO
def R_RenderView(fd):
    pass


@TODO
def R_SetGL2D():
    pass


@TODO
def GL_DrawColoredStereoLinePair(r, g, b, y):
    pass


@TODO
def GL_DrawStereoPattern():
    pass


@TODO
def R_SetLightLevel():
    pass


@TODO
def R_RenderFrame(fd):
    pass


@TODO
def R_Register():
    pass


@TODO
def R_SetMode():
    pass


@TODO
def R_Init(hinstance, hWnd):
    pass


@TODO
def R_Shutdown():
    pass


@TODO
def R_BeginFrame(camera_separation):
    pass


@TODO
def R_SetPalette(palette):
    pass


@TODO
def R_DrawBeam(e):
    pass


@TODO
def GetRefAPI(rimp):
    pass


@va_args
def SysError(error):
    ri.Sys_error(ERROR_LVL.ERR_FATAL, error)


@va_args
def Com_Printf(fmt):
    ri.Con_Printf(PRINT_LVL.PRINT_ALL, fmt)
