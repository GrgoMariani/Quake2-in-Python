from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def CMod_LoadSubmodels(l):
    pass


@TODO
def CMod_LoadSurfaces(l):
    pass


@TODO
def CMod_LoadNodes(l):
    pass


@TODO
def CMod_LoadBrushes(l):
    pass


@TODO
def CMod_LoadLeafs(l):
    pass


@TODO
def CMod_LoadPlanes(l):
    pass


@TODO
def CMod_LoadLeafBrushes(l):
    pass


@TODO
def CMod_LoadBrushSides(l):
    pass


@TODO
def CMod_LoadAreas(l):
    pass


@TODO
def CMod_LoadAreaPortals(l):
    pass


@TODO
def CMod_LoadVisibility(l):
    pass


@TODO
def CMod_LoadEntityString(l):
    pass


@TODO
def CM_LoadMap(name, clientload, checksum):
    pass


@TODO
def CM_InlineModel(name):
    pass


@TODO
def CM_NumClusters():
    pass


@TODO
def CM_NumInlineModels():
    pass


@TODO
def CM_EntityString():
    pass


@TODO
def CM_LeafContents(leafnum):
    pass


@TODO
def CM_LeafCluster(leafnum):
    pass


@TODO
def CM_LeafArea(leafnum):
    pass


@TODO
def CM_InitBoxHull():
    pass


@TODO
def CM_HeadnodeForBox(mins, maxs):
    pass


@TODO
def CM_PointLeafnum_r(p, num):
    pass


@TODO
def CM_PointLeafnum(p):
    pass


@TODO
def CM_BoxLeafnums_r(nodenum):
    pass


@TODO
def CM_BoxLeafnums_headnode(mins, maxs, _list, listsize, headnode, topnode):
    pass


@TODO
def CM_BoxLeafnums(mins, maxs, _list, listsize, topnode):
    pass


@TODO
def CM_PointContents(p, headnode):
    pass


@TODO
def CM_TransformedPointContents(p, headnode, origin, angles):
    pass


@TODO
def CM_ClipBoxToBrush(mins, maxs, p1, p2, trace, brush):
    pass


@TODO
def CM_TestBoxInBrush(mins, maxs, p1, trace, brush):
    pass


@TODO
def CM_TraceToLeaf(leafnum):
    pass


@TODO
def CM_TestInLeaf(leafnum):
    pass


@TODO
def CM_RecursiveHullCheck(num, p1f, p2f, p1, p2):
    pass


@TODO
def CM_BoxTrace(start, end, mins, maxs, headnode, brushmask):
    pass


@TODO
def CM_TransformedBoxTrace(start, end, mins, maxs, headnode, brushmask, origin, angles):
    pass


@TODO
def CM_DecompressVis(_in, out):
    pass


@TODO
def CM_ClusterPVS(cluster):
    pass


@TODO
def CM_ClusterPHS(cluster):
    pass


@TODO
def FloodArea_r(area, floodnum):
    pass


@TODO
def FloodAreaConnections():
    pass


@TODO
def CM_SetAreaPortalState(portalnum, open):
    pass


@TODO
def CM_AreasConnected(area1, area2):
    pass


@TODO
def CM_WriteAreaBits(buffer, area):
    pass


@TODO
def CM_WritePortalState(f):
    pass


@TODO
def CM_ReadPortalState(f):
    pass


@TODO
def CM_HeadnodeVisible(nodenum, visbits):
    pass
