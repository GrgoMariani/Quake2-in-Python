from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def DSoundError(error):
    pass


@TODO
def DS_CreateBuffers():
    pass


@TODO
def DS_DestroyBuffers():
    pass


@TODO
def FreeSound():
    pass


@TODO
def SNDDMA_InitDirect():
    pass


@TODO
def SNDDMA_InitWav():
    pass


@TODO
def SNDDMA_Init():
    pass


@TODO
def SNDDMA_GetDMAPos():
    pass


@TODO
def SNDDMA_BeginPainting():
    pass


@TODO
def SNDDMA_Submit():
    pass


def SNDDMA_Shutdown():
    FreeSound()


@TODO
def S_Activate(active):
    pass
