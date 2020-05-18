from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def BoundPoly(numverts, verts, mins, maxs):
    pass


@TODO
def SubdividePolygon(numverts, verts):
    pass


@TODO
def GL_SubdivideSurface(fa):
    pass


@TODO
def EmitWaterPolys(fa):
    pass


@TODO
def DrawSkyPolygon(nump, vecs):
    pass


@TODO
def ClipSkyPolygon(nump, ves, stage):
    pass


@TODO
def R_AddSkySurface(fa):
    pass


@TODO
def R_ClearSkyBox():
    pass


@TODO
def MakeSkyVec(s, t, axis):
    pass


@TODO
def R_DrawSkyBox():
    pass


@TODO
def R_SetSky(name, rotate, axis):
    pass
