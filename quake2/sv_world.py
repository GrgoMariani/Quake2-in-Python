from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def ClearLink(l):
    pass


@TODO
def RemoveLink(l):
    pass


@TODO
def InsertLinkBefore(l, before):
    pass


@TODO
def SV_CreateAreaNode(depth, mins, maxs):
    pass


@TODO
def SV_ClearWorld():
    pass


@TODO
def SV_UnlinkEdict(ent):
    pass


@TODO
def SV_LinkEdict(ent):
    pass


@TODO
def SV_AreaEdicts_r(node):
    pass


@TODO
def SV_AreaEdicts(mins, maxs, _list, maxcount, areatype):
    pass


@TODO
def SV_PointContents(p):
    pass


@TODO
def SV_HullForEntity(ent):
    pass


@TODO
def SV_ClipMoveToEntities(clip):
    pass


@TODO
def SV_TraceBounds(start, mins, maxs, end, boxmins, boxmaxs):
    pass


@TODO
def SV_Trace(start, mins, maxs, end, passedict, contentmask):
    pass
