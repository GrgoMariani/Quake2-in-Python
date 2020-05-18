from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


"""
    We will be skipping most of these functions as they only contain
    reading the data from the cd
"""


def CDAudio_Play2(track, looping):
    pass


def CDAudio_Play(track, looping):
    pass


def CDAudio_Stop():
    pass


def CDAudio_Pause():
    pass


def CDAudio_Resume():
    pass


def CDAudio_Stop():
    pass


def CDAudio_MessageHandler(hWnd, uMsg, wParam, lParam):
    pass


def CDAudio_Update():
    pass


def CDAudio_Init():
    pass


def CDAudio_Shutdown():
    pass


def CDAudio_Activate(actuve):
    pass
