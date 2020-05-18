from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def M_Banner(name):
    pass


@TODO
def M_PushMenu(draw, key):
    pass


@TODO
def M_ForceMenuOff():
    pass


@TODO
def M_PopMenu():
    pass


@TODO
def Default_MenuKey(m, key):
    pass


@TODO
def M_DrawCharacter(cx, cy, num):
    pass


@TODO
def M_Print(cx, cy, _str):
    pass


@TODO
def M_PrintWhite(cx, cy, _str):
    pass


@TODO
def M_DrawPic(x, y, pic):
    pass


@TODO
def M_DrawCursor(x, y, f):
    pass


@TODO
def M_DrawTextBox(x, y, width, lines):
    pass


@TODO
def M_Main_Draw():
    pass


@TODO
def M_Main_Key(key):
    pass


def M_Menu_Main_f():
    M_PushMenu(M_Main_Draw, M_Main_Key)


@TODO
def Multiplayer_MenuDraw():
    pass


@TODO
def PlayerSetupFunc(unused):
    pass


@TODO
def JoinNetworkServerFunc(unused):
    pass


@TODO
def StartNetworkServerFunc(unused):
    pass


@TODO
def Multiplayer_MenuInit():
    pass


@TODO
def Multiplayer_MenuKey(key):
    pass


def M_Menu_Multiplayer_f():
    Multiplayer_MenuInit()
    M_PushMenu(Multiplayer_MenuDraw, Multiplayer_MenuKey)


@TODO
def M_UnbindCommand(command):
    pass


@TODO
def M_FindKeysForCommand(command, twokeys):
    pass


@TODO
def KeyCursorDrawFunc(menu):
    pass


@TODO
def DrawKeyBindingFunc(_self):
    pass


@TODO
def KeyBindingFunc(_self):
    pass


@TODO
def Keys_MenuInit():
    pass


@TODO
def Keys_MenuDraw():
    pass


@TODO
def Keys_MenuKey(key):
    pass


def M_Menu_Keys_f():
    Keys_MenuInit()
    M_PushMenu(Keys_MenuDraw, Keys_MenuKey)


@TODO
def CrosshairFunc(unused):
    pass


@TODO
def JoystickFunc(unused):
    pass


def CustomizeControlsFunc(unused):
    M_Menu_Keys_f()


@TODO
def AlwaysRunFunc(unused):
    pass


@TODO
def FreeLookFunc(unused):
    pass


@TODO
def MouseSpeedFunc(unused):
    pass


@TODO
def NoAltTabFunc(unused):
    pass


def ClampCvar(_min, _max, value):
    return max(_min, min(_max, value))


@TODO
def ControlsSetMenuItemValues():
    pass


@TODO
def ControlsResetDefaultsFunc(unused):
    pass


@TODO
def InvertMouseFunc(unused):
    pass


@TODO
def LookspringFunc(unused):
    pass


@TODO
def LookstrafeFunc(unused):
    pass


@TODO
def UpdateVolumeFunc(unused):
    pass


@TODO
def UpdateCDVolumeFunc(unused):
    pass


@TODO
def ConsoleFunc(unused):
    pass


@TODO
def UpdateSoundQualityFunc(unused):
    pass


@TODO
def Options_MenuInit():
    pass


@TODO
def Options_MenuDraw():
    pass


@TODO
def Options_MenuKey(key):
    pass


def M_Menu_Options_f():
    Options_MenuInit()
    M_PushMenu(Options_MenuDraw, Options_MenuKey)


@TODO
def M_Credits_MenuDraw():
    pass


@TODO
def M_Credits_Key(key):
    pass


@TODO
def M_Menu_Credits_f():
    pass


@TODO
def StartGame():
    pass


@TODO
def EasyGameFunc(data):
    pass


@TODO
def MediumGameFunc(data):
    pass


@TODO
def HardGameFunc(data):
    pass


@TODO
def LoadGameFunc(unused):
    pass


@TODO
def SaveGameFunc(unused):
    pass


@TODO
def CreditsFunc(unused):
    pass


@TODO
def Game_MenuInit():
    pass


@TODO
def Game_MenuDraw():
    pass


@TODO
def Game_MenuKey(key):
    pass


@TODO
def M_Menu_Game_f():
    pass


@TODO
def Create_Savestrings():
    pass


@TODO
def LoadGameCallback(_self):
    pass


@TODO
def LoadGame_MenuInit():
    pass


@TODO
def LoadGame_MenuDraw():
    pass


@TODO
def LoadGame_MenuKey(key):
    pass


def M_Menu_LoadGame_f():
    LoadGame_MenuInit()
    M_PushMenu(LoadGame_MenuDraw, LoadGame_MenuKey)


@TODO
def SaveGameCallback(_self):
    pass


@TODO
def SaveGame_MenuDraw():
    pass


@TODO
def SaveGame_MenuInit():
    pass


@TODO
def SaveGame_MenuKey(key):
    pass


@TODO
def M_Menu_SaveGame_f():
    pass


@TODO
def M_AddToServerList(adr, info):
    pass


@TODO
def JoinServerFunc(_self):
    pass


@TODO
def AddressBookFunc(_self):
    pass


@TODO
def NullCursorDraw(_self):
    pass


@TODO
def SearchLocalGames():
    pass


def SearchLocalGamesFunc(_self):
    SearchLocalGames()


@TODO
def JoinServer_MenuInit():
    pass


@TODO
def JoinServer_MenuDraw():
    pass


@TODO
def JoinServer_MenuKey(key):
    pass


def M_Menu_JoinServer_f():
    JoinServer_MenuInit()
    M_PushMenu(JoinServer_MenuDraw, JoinServer_MenuKey)


@TODO
def DMOptionsFunc(_self):
    pass


@TODO
def RulesChangeFunc(_self):
    pass


@TODO
def StartServerActionFunc(_self):
    pass


@TODO
def StartServer_MenuInit():
    pass


@TODO
def StartServer_MenuDraw():
    pass


@TODO
def StartServer_MenuKey(key):
    pass


def M_Menu_StartServer_f():
    StartServer_MenuInit()
    M_PushMenu(StartServer_MenuDraw, StartServer_MenuKey)


@TODO
def DMFlagCallback(_self):
    pass


@TODO
def DMOptions_MenuInit():
    pass


@TODO
def DMOptions_MenuDraw():
    pass


@TODO
def DMOptions_MenuKey(key):
    pass


def M_Menu_DMOptions_f():
    DMOptions_MenuInit()
    M_PushMenu(DMOptions_MenuDraw, DMOptions_MenuKey)


@TODO
def DownloadCallback(_self):
    pass


@TODO
def DownloadOptions_MenuInit():
    pass


@TODO
def DownloadOptions_MenuDraw():
    pass


@TODO
def DownloadOptions_MenuKey(key):
    pass


def M_Menu_DownloadOptions_f():
    DownloadOptions_MenuInit()
    M_PushMenu(DownloadOptions_MenuDraw, DownloadOptions_MenuKey)


@TODO
def AddressBook_MenuInit():
    pass


@TODO
def AddressBook_MenuKey(key):
    pass


@TODO
def AddressBook_MenuDraw():
    pass


def M_Menu_AddressBook_f():
    AddressBook_MenuInit()
    M_PushMenu(AddressBook_MenuDraw, AddressBook_MenuKey)


def DownloadOptionsFunc(_self):
    M_Menu_DownloadOptions_f()


@TODO
def HandednessCallback(unused):
    pass


@TODO
def RateCallback(unused):
    pass


@TODO
def ModelCallback(unused):
    pass


@TODO
def FreeFileList(_list, n):
    pass


@TODO
def IconOfSkinExists(skin, pcxfiles, npcxfiles):
    pass


@TODO
def PlayerConfig_ScanDirectories():
    pass


@TODO
def pmicmpfnc(_a, _b):
    pass


@TODO
def PlayerConfig_MenuInit():
    pass


@TODO
def PlayerConfig_MenuDraw():
    pass


@TODO
def PlayerConfig_MenuKey(key):
    pass


@TODO
def M_Menu_PlayerConfig_f():
    pass


@TODO
def M_Quit_Key(key):
    pass


@TODO
def M_Quit_Draw():
    pass


def M_Menu_Quit_f():
    M_PushMenu(M_Quit_Draw, M_Quit_Key)


@TODO
def M_Init():
    pass


@TODO
def M_Draw():
    pass


@TODO
def M_Keydown():
    pass
