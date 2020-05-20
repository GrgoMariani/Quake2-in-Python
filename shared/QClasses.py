class cplane_t:
    def __init__(self):
        self.normal = [0, 0, 0]
        self.dist = 0
        self.type = 0
        self.signbits = 0
        self.pad = [0, 0]


class sizebuf_t:
    def __init__(self):
        self.allowoverflow = False
        self.overflowed = False
        self.data = None
        self.maxsize = 0
        self.cursize = 0
        self.readcount = 0


class level_locals_t:
    def __init__(self):
        self.framenum = 0
        self.time = 0
        self.levelname = ""
        self.mapname = ""
        self.nextmap = ""
        self.intermissiontime = 0
        self.changemap = ""
        self.exitintermission = 0
        self.intermission_origin = [0, 0, 0]
        self.intermission_angle = [0, 0, 0]

        self.sight_client = None
        self.sight_entity = None
        self.sight_entity_framenum = 0
        self.sound_entity = None
        self.sound_entity_framenum = 0
        self.sound2_entity = None
        self.sound2_entity_framenum = 0

        self.pic_health = 0

        self.total_secrets = 0
        self.found_secrets = 0

        self.total_goals = 0
        self.found_goals = 0

        self.total_monsters = 0
        self.killed_monsters = 0

        self.current_entity = None
        self.body_que = 0
        self.power_cubes = 0


class mmove_t:
    def __init__(self, firstframe, lastframe, frame, endfunc):
        self.firstframe = firstframe
        self.lastframe = lastframe
        self.frame = frame
        self.endfunc = endfunc


class mframe_t:
    def __init__(self, aifunc, dist, thinkfunc):
        self.aifunc = aifunc
        self.dist = dist
        self.thinkfunc = thinkfunc


class monsterinfo_t:
    def __init__(self):
        self.currentmove = None
        self.aiflags = 0
        self.nextframe = 0
        self.scale = 0
        self.stand = None
        self.idle = None
        self.search = None
        self.walk = None
        self.run = None
        self.dodge = None
        self.attack = None
        self.melee = None
        self.sight = None
        self.checkattack = None
        self.pausetime = 0
        self.attack_finished = 0
        self.saved_goal = [0, 0, 0]
        self.search_time = 0
        self.trail_time = 0
        self.last_sighting = [0, 0, 0]
        self.attack_state = 0
        self.lefty = 0
        self.idle_time = 0
        self.linkcount = 0
        self.power_armor_type = 0
        self.power_armor_power = 0



