from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def SV_EmitPacketEntities(_from, _to, msg):
    pass


@TODO
def SV_WritePlayerstateToClient(_from, _to, msg):
    pass


@TODO
def SV_WriteFrameToClient(client, msg):
    pass


@TODO
def SV_FatPVS(org):
    pass


@TODO
def SV_BuildClientFrame(client):
    pass


@TODO
def SV_RecordDemoMessage():
    pass
