from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def R_RenderDlight(light):
    pass


@TODO
def R_RenderDlights():
    pass


@TODO
def R_MarkLights(light, bit, node):
    pass


@TODO
def R_PushDlights():
    pass


@TODO
def RecursiveLightPoint(node, start, end):
    pass


@TODO
def R_LightPoint(p, color):
    pass


@TODO
def R_AddDynamicLights(surf):
    pass


@TODO
def R_SetCacheState(surf):
    pass


@TODO
def R_BuildLightMap(surf, dest, stride):
    pass
