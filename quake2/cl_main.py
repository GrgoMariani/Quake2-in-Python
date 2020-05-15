from wrapper_qpy.decorators import static_vars, TODO


@TODO
def CL_WriteDemoMessage():
    pass


@TODO
def CL_Stop_f():
    pass


@TODO
def CL_Record_f():
    pass


@TODO
def Cmd_ForwardToServer():
    pass


@TODO
def CL_ForwardToServer_f():
    pass


@TODO
def CL_Pause_f():
    pass


@TODO
def CL_Quit_f():
    pass


@TODO
def CL_Drop():
    pass


@TODO
def CL_SendConnectPacket():
    pass


@TODO
def CL_CheckForResend():
    pass


@TODO
def CL_Connect_f():
    pass


@TODO
def CL_Rcon_f():
    pass


@TODO
def CL_ClearState():
    pass


@TODO
def CL_Disconnect():
    pass


@TODO
def CL_Disconnect_f():
    pass


@TODO
def CL_Packet_f():
    pass


@TODO
def CL_Changing_f():
    pass


@TODO
def CL_Reconnect_f():
    pass


@TODO
def CL_ParseStatusMessage():
    pass


@TODO
def CL_PingServers_f():
    pass


@TODO
def CL_Skins_f():
    pass


@TODO
def CL_ConnectionlessPacket():
    pass


@TODO
def CL_DumpPackets():
    pass


@TODO
def CL_ReadPackets():
    pass


@TODO
def CL_FixUpGender():
    pass


@TODO
def CL_Userinfo_f():
    pass


@TODO
def CL_Snd_Restart_f():
    pass


@TODO
def CL_RequestNextDownload():
    pass


@TODO
def CL_Precache_f():
    pass


@TODO
def CL_InitLocal():
    pass


@TODO
def CL_WriteConfiguration():
    pass


@TODO
def CL_FixCvarCheats():
    pass


@TODO
def CL_SendCommand():
    pass


@TODO
def CL_Frame():
    pass


@TODO
def CL_Init():
    pass


@static_vars(isdown=False)
def CL_Shutdown():
    if CL_Shutdown.isdown:
        print("recursive shutdown")
        return
    CL_Shutdown.isdown = True
    CL_WriteConfiguration()
