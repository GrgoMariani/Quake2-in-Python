from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def CRC_Init(crcvalue):
    pass


@TODO
def CRC_ProcessByte(crcvalue, data):
    pass


@TODO
def CRC_Value(crcvalue):
    pass


@TODO
def CRC_Block(start, count):
    pass
