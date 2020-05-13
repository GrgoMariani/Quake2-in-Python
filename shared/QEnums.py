from enum import Enum


class CVAR_ENUM(Enum):
    CVAR_ARCHIVE = 1
    CVAR_USERINFO = 2
    CVAR_SERVERINFO = 4
    CVAR_NOSET = 8
    CVAR_LATCH = 16


class connstate_t(Enum):
    ca_uninitialized = 0
    ca_disconnected = 1
    ca_connecting = 2
    ca_connected = 3
    ca_active = 4


class dltype_t(Enum):
    dl_none = 0
    dl_model = 1
    dl_sound = 2
    dl_skin = 3
    dl_single = 4


class keydest_t(Enum):
    key_game = 0
    key_console = 1
    key_message = 2
    key_menu = 3


class solid_t(Enum):
    SOLID_NOT = 0
    SOLID_TRIGGER = 1
    SOLID_BBOX = 2
    SOLID_BSP =3


class multicast_t(Enum):
    MULTICAST_ALL = 0
    MULTICAST_PHS = 1
    MULTICAST_PVS = 2
    MULTICAST_ALL_R = 3
    MULTICAST_PHS_R = 4
    MULTICAST_PVS_R = 5


class pmtype_t(Enum):
    PM_NORMAL = 0
    PN_SPECTATOR = 1
    PM_DEAD = 2
    PM_GIB = 3
    PM_FREEZE = 4


class temp_event_t(Enum):
    TE_GUNSHOT = 0
    TE_BLOOD = 1
    TE_BLASTER = 2
    TE_RAILTRAIL = 3
    TE_SHOTGUN = 4
    TE_EXPLOSION1 = 5
    TE_EXPLOSION2 = 6
    TE_ROCKET_EXPLOSION = 7
    TE_GRENADE_EXPLOSION = 8
    TE_SPARKS = 9
    TE_SPLASH = 10
    TE_BUBBLETRAIL = 11
    TE_SCREEN_SPARKS = 12
    TE_SHIELD_SPARKS = 13
    TE_BULLET_SPARKS = 14
    TE_LASER_SPARKS = 15
    TE_PARASITE_ATTACK = 16
    TE_ROCKET_EXPLOSION_WATER = 17
    TE_GRENADE_EXPLOSION_WATER = 18
    TE_MEDIC_CABLE_ATTACK = 19
    TE_BFG_EXPLOSION = 20
    TE_BFG_BIGEXPLOSION = 21
    TE_BOSSTPORT = 22
    TE_BFG_LASER = 23
    TE_GRAPPLE_CABLE = 24
    TE_WELDING_SPARKS = 25
    TE_GREENBLOOD = 26
    TE_BLUEHYPERBLASTER = 27
    TE_PLASMA_EXPLOSION = 28
    TE_TUNNEL_SPARKS = 29
    TE_BLASTER2 = 30
    TE_RAILTRAIL2 = 31
    TE_FLAME = 32
    TE_LIGHTNING = 33
    TE_DEBUGTRAIL = 34
    TE_PLAIN_EXPLOSION = 35
    TE_FLASHLIGHT = 36
    TE_FORCEWALL = 37
    TE_HEATBEAM = 38
    TE_MONSTER_HEATBEAM = 39
    TE_STEAM = 40
    TE_BUBBLETRAIL2 = 41
    TE_MOREBLOOD = 42
    TE_HEATBEAM_SPARKS = 43
    TE_HEATBEAM_STEAM = 44
    TE_CHAINFIST_SMOKE = 45
    TE_ELECTRIC_SPARKS = 46
    TE_TRACKER_EXPLOSION = 47
    TE_TELEPORT_EFFECT = 48
    TE_DBALL_GOAL = 49
    TE_WIDOWBEAMOUT = 50
    TE_NUKEBLAST = 51
    TE_WIDOWSPLASH = 52
    TE_EXPLOSION1_BIG = 53
    TE_EXPLOSION1_NP = 54
    TE_FLECHETTE = 55


class entity_event_t(Enum):
    EV_NONE = 0
    EV_ITEM_RESPAWN = 1
    EV_FOOTSTEP = 2
    EV_FALLSHORT = 3
    EV_FALL = 4
    EV_FALLFAR = 5
    EV_PLAYER_TELEPORT = 6
    EV_OTHER_TELEPORT = 7


class svc_ops_e(Enum):
    svc_bad = 0
    svc_muzzleflash = 1
    svc_muzzleflash2 = 2
    svc_temp_entity = 3
    svc_layout = 4
    svc_inventory = 5
    svc_nop = 6
    svc_disconnect = 7
    svc_reconnect = 8
    svc_sound = 9
    svc_print = 10
    svc_stufftext = 11
    svc_serverdata = 12
    svc_configstring = 13
    svc_spawnbaseline = 14
    svc_centerprint = 15
    svc_download = 16
    svc_playerinfo = 17
    svc_packetentities = 18
    svc_deltapacketentities = 19
    svc_frame = 20


class clc_ops_e(Enum):
    clc_bad = 0
    clc_nop = 1
    clc_move = 2
    clc_userinfo = 3
    clc_stringcmd = 4


class netadrtype_t(Enum):
    NA_LOOPBACK = 0
    NA_BROADCAST = 1
    NA_IP = 2
    NA_IPX = 3
    NA_BROADCAST_IPX = 4


class netsrc_t(Enum):
    NS_CLIENT = 0
    NS_SERVER = 1


class server_state_t(Enum):
    ss_dead = 0
    ss_loading = 1
    ss_game = 2
    ss_cinematic = 3
    ss_demo = 4
    ss_pic = 5


class client_state_t(Enum):
    cs_free = 0
    cs_zombie = 1
    cs_connected = 2
    cs_spawned = 3


class redirect_t(Enum):
    RD_NONE = 0
    RD_CLIENT = 1
    RD_PACKET = 2


class exptype_t(Enum):
    ex_free = 0
    ex_explosion = 1
    ex_misc = 2
    ex_flash = 3
    ex_mflash = 4
    ex_poly = 5
    ex_poly2 = 6


class _ControlList(Enum):
    AxisNada = 0
    AxisForward = 1
    AxisLook = 2
    AxisSide = 3
    AxisTun = 4
    AxisUp = 5


class sndinitstat(Enum):
    SIS_SUCCESS = 0
    SIS_FAILURE = 1
    SIS_NOTAVAIL = 2


class imagetype_t(Enum):
    it_skin = 0
    it_sprite = 1
    it_wall = 2
    it_pic = 3
    it_sky = 4


class rserr_t(Enum):
    rserr_ok = 0
    rserr_invalid_fullscreen = 1
    rserr_invalid_mode = 2
    rserr_unknown = 3


class modtype_t(Enum):
    mod_bad = 0
    mod_brush = 1
    mod_sprite = 2
    mod_alias = 3


class damage_t(Enum):
    DAMAGE_NO = 0
    DAMAGE_YES = 1
    DAMAGE_AIM = 2


class waponstate_t(Enum):
    WEAPON_READY = 0
    WEAPON_ACTIVATING = 1
    WEAPON_DROPPING = 2
    WEAPON_FIRING = 3


class ammo_t(Enum):
    AMMO_BULLETS = 0
    AMMO_SHELLS = 1
    AMMO_ROCKETS = 2
    AMMO_GRENADES = 3
    AMMO_CELLS = 4
    AMMO_SLUGS = 5


class movetype_t(Enum):
    MOVETYPE_NONE = 0
    MOVETYPE_NOCLIP = 1
    MOVETYPE_PUSH = 2
    MOVETYPE_STOP = 3
    MOVETYPE_WALK = 4
    MOVETYPE_STEP = 5
    MOVETYPE_FLY = 6
    MOVETYPE_TOSS = 7
    MOVETYPE_FLYMISSILE = 8
    MOVETYPE_BOUNCE = 9


class fieldtype_t(Enum):
    F_INT = 0
    F_FLOAT = 1
    F_LSTRING = 2
    F_GSTRING = 3
    F_VECTOR = 4
    F_ANGLEHACK = 5
    F_EDICT = 6
    F_ITEM = 7
    F_CLIENT = 8
    F_FUNCTION = 9
    F_MMOVE = 10
    F_IGNORE = 11


class Q_angle_indexes(Enum):
    PITCH = 0
    YAW = 1
    ROLL = 2


class PRINT_LVL(Enum):
    PRINT_ALL = 0
    PRINT_DEVELOPER = 1


class ERROR_LVL(Enum):
    ERR_FATAL = 0
    ERR_DROP = 1
    ERR_QUIT = 2


class EXEC_LVL(Enum):
    EXEC_NOW = 0
    EXEC_INSERT = 1
    EXEC_APPEND = 2
