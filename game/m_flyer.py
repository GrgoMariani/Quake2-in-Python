from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from .reference_import import gi
from wrapper_qpy.linker import LinkEmptyFunctions
from shared.QClasses import mmove_t, mframe_t


LinkEmptyFunctions(globals(), ["ai_charge", "ai_run"])


ACTION_nothing = 0
ACTION_attack1 = 1
ACTION_attack2 = 2
ACTION_run = 3
ACTION_walk = 4

FRAME_start01 = 0
FRAME_start02 = 1
FRAME_start03 = 2
FRAME_start04 = 3
FRAME_start05 = 4
FRAME_start06 = 5
FRAME_stop01 = 6
FRAME_stop02 = 7
FRAME_stop03 = 8
FRAME_stop04 = 9
FRAME_stop05 = 10
FRAME_stop06 = 11
FRAME_stop07 = 12
FRAME_stand01 = 13
FRAME_stand02 = 14
FRAME_stand03 = 15
FRAME_stand04 = 16
FRAME_stand05 = 17
FRAME_stand06 = 18
FRAME_stand07 = 19
FRAME_stand08 = 20
FRAME_stand09 = 21
FRAME_stand10 = 22
FRAME_stand11 = 23
FRAME_stand12 = 24
FRAME_stand13 = 25
FRAME_stand14 = 26
FRAME_stand15 = 27
FRAME_stand16 = 28
FRAME_stand17 = 29
FRAME_stand18 = 30
FRAME_stand19 = 31
FRAME_stand20 = 32
FRAME_stand21 = 33
FRAME_stand22 = 34
FRAME_stand23 = 35
FRAME_stand24 = 36
FRAME_stand25 = 37
FRAME_stand26 = 38
FRAME_stand27 = 39
FRAME_stand28 = 40
FRAME_stand29 = 41
FRAME_stand30 = 42
FRAME_stand31 = 43
FRAME_stand32 = 44
FRAME_stand33 = 45
FRAME_stand34 = 46
FRAME_stand35 = 47
FRAME_stand36 = 48
FRAME_stand37 = 49
FRAME_stand38 = 50
FRAME_stand39 = 51
FRAME_stand40 = 52
FRAME_stand41 = 53
FRAME_stand42 = 54
FRAME_stand43 = 55
FRAME_stand44 = 56
FRAME_stand45 = 57
FRAME_attak101 = 58
FRAME_attak102 = 59
FRAME_attak103 = 60
FRAME_attak104 = 61
FRAME_attak105 = 62
FRAME_attak106 = 63
FRAME_attak107 = 64
FRAME_attak108 = 65
FRAME_attak109 = 66
FRAME_attak110 = 67
FRAME_attak111 = 68
FRAME_attak112 = 69
FRAME_attak113 = 70
FRAME_attak114 = 71
FRAME_attak115 = 72
FRAME_attak116 = 73
FRAME_attak117 = 74
FRAME_attak118 = 75
FRAME_attak119 = 76
FRAME_attak120 = 77
FRAME_attak121 = 78
FRAME_attak201 = 79
FRAME_attak202 = 80
FRAME_attak203 = 81
FRAME_attak204 = 82
FRAME_attak205 = 83
FRAME_attak206 = 84
FRAME_attak207 = 85
FRAME_attak208 = 86
FRAME_attak209 = 87
FRAME_attak210 = 88
FRAME_attak211 = 89
FRAME_attak212 = 90
FRAME_attak213 = 91
FRAME_attak214 = 92
FRAME_attak215 = 93
FRAME_attak216 = 94
FRAME_attak217 = 95
FRAME_bankl01 = 96
FRAME_bankl02 = 97
FRAME_bankl03 = 98
FRAME_bankl04 = 99
FRAME_bankl05 = 100
FRAME_bankl06 = 101
FRAME_bankl07 = 102
FRAME_bankr01 = 103
FRAME_bankr02 = 104
FRAME_bankr03 = 105
FRAME_bankr04 = 106
FRAME_bankr05 = 107
FRAME_bankr06 = 108
FRAME_bankr07 = 109
FRAME_rollf01 = 110
FRAME_rollf02 = 111
FRAME_rollf03 = 112
FRAME_rollf04 = 113
FRAME_rollf05 = 114
FRAME_rollf06 = 115
FRAME_rollf07 = 116
FRAME_rollf08 = 117
FRAME_rollf09 = 118
FRAME_rollr01 = 119
FRAME_rollr02 = 120
FRAME_rollr03 = 121
FRAME_rollr04 = 122
FRAME_rollr05 = 123
FRAME_rollr06 = 124
FRAME_rollr07 = 125
FRAME_rollr08 = 126
FRAME_rollr09 = 127
FRAME_defens01 = 128
FRAME_defens02 = 129
FRAME_defens03 = 130
FRAME_defens04 = 131
FRAME_defens05 = 132
FRAME_defens06 = 133
FRAME_pain101 = 134
FRAME_pain102 = 135
FRAME_pain103 = 136
FRAME_pain104 = 137
FRAME_pain105 = 138
FRAME_pain106 = 139
FRAME_pain107 = 140
FRAME_pain108 = 141
FRAME_pain109 = 142
FRAME_pain201 = 143
FRAME_pain202 = 144
FRAME_pain203 = 145
FRAME_pain204 = 146
FRAME_pain301 = 147
FRAME_pain302 = 148
FRAME_pain303 = 149
FRAME_pain304 = 150

MODEL_SCALE = 1.000000

nextmove = 0


@TODO
def flyer_sight():
    pass


@TODO
def flyer_idle():
    pass


@TODO
def flyer_pop_blades():
    pass


flyer_frames_run = [mframe_t(ai_run, 0, None) for _ in range(0, 45)]

flyer_move_run = mmove_t(FRAME_stand01, FRAME_stand45, flyer_frames_run, None)


@TODO
def flyer_run():
    pass


@TODO
def flyer_walk():
    pass


@TODO
def flyer_stand():
    pass


@TODO
def flyer_stop():
    pass


@TODO
def flyer_start():
    pass


@TODO
def flyer_fire():
    pass


@TODO
def flyer_fireleft():
    pass


@TODO
def flyer_fireright():
    pass


flyer_frames_attack2 = [
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, -10, flyer_fireleft),
    mframe_t(ai_charge, -10, flyer_fireright),
    mframe_t(ai_charge, -10, flyer_fireleft),
    mframe_t(ai_charge, -10, flyer_fireright),
    mframe_t(ai_charge, -10, flyer_fireleft),
    mframe_t(ai_charge, -10, flyer_fireright),
    mframe_t(ai_charge, -10, flyer_fireleft),
    mframe_t(ai_charge, -10, flyer_fireright),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None)
]

flyer_move_attack2 = mmove_t(FRAME_attak201, FRAME_attak217, flyer_frames_attack2, flyer_run)


@TODO
def flyer_slash_left():
    pass


@TODO
def flyer_frames_start_melee():
    pass


@TODO
def flyer_loop_melee():
    pass


flyer_frames_start_melee = [
    mframe_t(ai_charge, 0, flyer_pop_blades),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None),
    mframe_t(ai_charge, 0, None)
]

flyer_move_start_melee = mmove_t(FRAME_attak101, FRAME_attak106, flyer_frames_start_melee, flyer_loop_melee)


@TODO
def flyer_attack():
    pass


@TODO
def flyer_setstart():
    pass


def flyer_nextmove(_self):
    if nextmove == ACTION_attack1:
        _self.monsterinfo.currentmove = flyer_move_start_melee
    elif nextmove == ACTION_attack2:
        _self.monsterinfo.currentmove = flyer_move_attack2
    elif nextmove == ACTION_run:
        _self.monsterinfo.currentmove = flyer_move_run


@TODO
def flyer_melee():
    pass


@TODO
def flyer_check_melee():
    pass


@TODO
def flyer_pain():
    pass


@TODO
def flyer_die():
    pass


@TODO
def SP_monster_flyer():
    pass


from game.g_ai import ai_charge, ai_run
