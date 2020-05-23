from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), ["SV_DropClient"])

sv_client = None


@TODO
def SV_BeginDemoserver():
    pass


@TODO
def SV_New_f():
    pass


@TODO
def SV_Configstrings_f():
    pass


@TODO
def SV_Baselines_f():
    pass


@TODO
def SV_Begin_f():
    pass


@TODO
def SV_NextDownload_f():
    pass


@TODO
def SV_BeginDownload_f():
    pass


def SV_Disconnect_f():
    SV_DropClient(sv_client)


@TODO
def SV_ShowServerinfo_f():
    pass


@TODO
def SV_Nextserver():
    pass


@TODO
def SV_Nextserver_f():
    pass


@TODO
def SV_ExecuteUserCommand():
    pass


@TODO
def SV_ClientThink(cl, cmd):
    pass


@TODO
def SV_ExecuteClientMessage(cl):
    pass


from .sv_main import SV_DropClient
