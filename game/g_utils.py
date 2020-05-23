from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from .reference_import import gi
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


def G_ProjectSource(point, distance, forward, right, result):
    result[0] = point[0] + forward[0] * distance[0] + right[0] * distance[1]
    result[1] = point[1] + forward[1] * distance[0] + right[1] * distance[1]
    result[2] = point[2] + forward[2] * distance[0] + right[2] * distance[1] + distance[2]


@TODO
def G_Find():
    pass


@TODO
def findradius():
    pass


@TODO
def G_PickTarget():
    pass


@TODO
def Think_Delay():
    pass


@TODO
def G_UseTargets():
    pass


@TODO
def tv():
    pass


@TODO
def vtos():
    pass


@TODO
def G_SetMovedir():
    pass


@TODO
def vectoyaw():
    pass


@TODO
def vectoangles():
    pass


@TODO
def G_CopyString():
    pass


@TODO
def G_InitEdict():
    pass


@TODO
def G_Spawn():
    pass


@TODO
def G_FreeEdict():
    pass


@TODO
def G_TouchTriggers():
    pass


@TODO
def G_TouchSolids():
    pass


@TODO
def KillBox():
    pass
