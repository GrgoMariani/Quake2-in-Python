"""
Reference import file is an easier way for us to connect the modules in the way the dlls are connected
"""


class game_import_t:
    def __init__(self):
        self.bprintf = None
        self.dprintf = None
        self.cprintf = None
        self.centerprintf = None
        self.sound = None
        self.positioned_sound = None
        self.configstring = None
        self.error = None
        self.modelindex = None
        self.soundindex = None
        self.imageindex = None
        self.setmodel = None
        self.trace = None
        self.pointcontents = None
        self.inPVS = None
        self.inPHS = None
        self.SetAreaPortalState = None
        self.AreasConnected = None
        self.linkentity = None
        self.unlinkentity = None
        self.BoxEdicts = None
        self.Pmove = None
        self.multicast = None
        self.unicast = None
        self.WriteChar = None
        self.WriteByte = None
        self.WriteShort = None
        self.WriteLong = None
        self.WriteFloat = None
        self.WriteString = None
        self.WritePosition = None
        self.WriteDir = None
        self.WriteAngle = None
        self.TagMalloc = None
        self.TagFree = None
        self.FreeTags = None
        self.cvar = None
        self.cvar_set = None
        self.cvar_forceset = None
        self.argc = None
        self.argv = None
        self.args = None
        self.AddCommandString = None
        self.DebugGraph = None
        self.cvar_forceset = None
        self.cvar_forceset = None
        self.cvar_forceset = None
        self.cvar_forceset = None


gi = game_import_t()
