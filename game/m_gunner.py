import random
from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from .reference_import import gi
from wrapper_qpy.linker import LinkEmptyFunctions
from .global_vars import level
from shared.QEnums import SOUND_ATTN_VALUES, SOUND_CHANNELS
from shared.QClasses import mmove_t, mframe_t


LinkEmptyFunctions(globals(), ["ai_move"])


FRAME_stand01 = 0
FRAME_stand02 = 1
FRAME_stand03 = 2
FRAME_stand04 = 3
FRAME_stand05 = 4
FRAME_stand06 = 5
FRAME_stand07 = 6
FRAME_stand08 = 7
FRAME_stand09 = 8
FRAME_stand10 = 9
FRAME_stand11 = 10
FRAME_stand12 = 11
FRAME_stand13 = 12
FRAME_stand14 = 13
FRAME_stand15 = 14
FRAME_stand16 = 15
FRAME_stand17 = 16
FRAME_stand18 = 17
FRAME_stand19 = 18
FRAME_stand20 = 19
FRAME_stand21 = 20
FRAME_stand22 = 21
FRAME_stand23 = 22
FRAME_stand24 = 23
FRAME_stand25 = 24
FRAME_stand26 = 25
FRAME_stand27 = 26
FRAME_stand28 = 27
FRAME_stand29 = 28
FRAME_stand30 = 29
FRAME_stand31 = 30
FRAME_stand32 = 31
FRAME_stand33 = 32
FRAME_stand34 = 33
FRAME_stand35 = 34
FRAME_stand36 = 35
FRAME_stand37 = 36
FRAME_stand38 = 37
FRAME_stand39 = 38
FRAME_stand40 = 39
FRAME_stand41 = 40
FRAME_stand42 = 41
FRAME_stand43 = 42
FRAME_stand44 = 43
FRAME_stand45 = 44
FRAME_stand46 = 45
FRAME_stand47 = 46
FRAME_stand48 = 47
FRAME_stand49 = 48
FRAME_stand50 = 49
FRAME_stand51 = 50
FRAME_stand52 = 51
FRAME_stand53 = 52
FRAME_stand54 = 53
FRAME_stand55 = 54
FRAME_stand56 = 55
FRAME_stand57 = 56
FRAME_stand58 = 57
FRAME_stand59 = 58
FRAME_stand60 = 59
FRAME_stand61 = 60
FRAME_stand62 = 61
FRAME_stand63 = 62
FRAME_stand64 = 63
FRAME_stand65 = 64
FRAME_stand66 = 65
FRAME_stand67 = 66
FRAME_stand68 = 67
FRAME_stand69 = 68
FRAME_stand70 = 69
FRAME_walk01 = 70
FRAME_walk02 = 71
FRAME_walk03 = 72
FRAME_walk04 = 73
FRAME_walk05 = 74
FRAME_walk06 = 75
FRAME_walk07 = 76
FRAME_walk08 = 77
FRAME_walk09 = 78
FRAME_walk10 = 79
FRAME_walk11 = 80
FRAME_walk12 = 81
FRAME_walk13 = 82
FRAME_walk14 = 83
FRAME_walk15 = 84
FRAME_walk16 = 85
FRAME_walk17 = 86
FRAME_walk18 = 87
FRAME_walk19 = 88
FRAME_walk20 = 89
FRAME_walk21 = 90
FRAME_walk22 = 91
FRAME_walk23 = 92
FRAME_walk24 = 93
FRAME_run01 = 94
FRAME_run02 = 95
FRAME_run03 = 96
FRAME_run04 = 97
FRAME_run05 = 98
FRAME_run06 = 99
FRAME_run07 = 100
FRAME_run08 = 101
FRAME_runs01 = 102
FRAME_runs02 = 103
FRAME_runs03 = 104
FRAME_runs04 = 105
FRAME_runs05 = 106
FRAME_runs06 = 107
FRAME_attak101 = 108
FRAME_attak102 = 109
FRAME_attak103 = 110
FRAME_attak104 = 111
FRAME_attak105 = 112
FRAME_attak106 = 113
FRAME_attak107 = 114
FRAME_attak108 = 115
FRAME_attak109 = 116
FRAME_attak110 = 117
FRAME_attak111 = 118
FRAME_attak112 = 119
FRAME_attak113 = 120
FRAME_attak114 = 121
FRAME_attak115 = 122
FRAME_attak116 = 123
FRAME_attak117 = 124
FRAME_attak118 = 125
FRAME_attak119 = 126
FRAME_attak120 = 127
FRAME_attak121 = 128
FRAME_attak201 = 129
FRAME_attak202 = 130
FRAME_attak203 = 131
FRAME_attak204 = 132
FRAME_attak205 = 133
FRAME_attak206 = 134
FRAME_attak207 = 135
FRAME_attak208 = 136
FRAME_attak209 = 137
FRAME_attak210 = 138
FRAME_attak211 = 139
FRAME_attak212 = 140
FRAME_attak213 = 141
FRAME_attak214 = 142
FRAME_attak215 = 143
FRAME_attak216 = 144
FRAME_attak217 = 145
FRAME_attak218 = 146
FRAME_attak219 = 147
FRAME_attak220 = 148
FRAME_attak221 = 149
FRAME_attak222 = 150
FRAME_attak223 = 151
FRAME_attak224 = 152
FRAME_attak225 = 153
FRAME_attak226 = 154
FRAME_attak227 = 155
FRAME_attak228 = 156
FRAME_attak229 = 157
FRAME_attak230 = 158
FRAME_pain101 = 159
FRAME_pain102 = 160
FRAME_pain103 = 161
FRAME_pain104 = 162
FRAME_pain105 = 163
FRAME_pain106 = 164
FRAME_pain107 = 165
FRAME_pain108 = 166
FRAME_pain109 = 167
FRAME_pain110 = 168
FRAME_pain111 = 169
FRAME_pain112 = 170
FRAME_pain113 = 171
FRAME_pain114 = 172
FRAME_pain115 = 173
FRAME_pain116 = 174
FRAME_pain117 = 175
FRAME_pain118 = 176
FRAME_pain201 = 177
FRAME_pain202 = 178
FRAME_pain203 = 179
FRAME_pain204 = 180
FRAME_pain205 = 181
FRAME_pain206 = 182
FRAME_pain207 = 183
FRAME_pain208 = 184
FRAME_pain301 = 185
FRAME_pain302 = 186
FRAME_pain303 = 187
FRAME_pain304 = 188
FRAME_pain305 = 189
FRAME_death01 = 190
FRAME_death02 = 191
FRAME_death03 = 192
FRAME_death04 = 193
FRAME_death05 = 194
FRAME_death06 = 195
FRAME_death07 = 196
FRAME_death08 = 197
FRAME_death09 = 198
FRAME_death10 = 199
FRAME_death11 = 200
FRAME_duck01 = 201
FRAME_duck02 = 202
FRAME_duck03 = 203
FRAME_duck04 = 204
FRAME_duck05 = 205
FRAME_duck06 = 206
FRAME_duck07 = 207
FRAME_duck08 = 208

MODEL_SCALE = 1.150000

sound_pain = 0
sound_pain2 = 0
sound_death = 0
sound_idle = 0
sound_open = 0
sound_search = 0
sound_sight = 0


@TODO
def gunner_idlesound():
    pass


@TODO
def gunner_sight():
    pass


@TODO
def gunner_search():
    pass


@TODO
def gunner_fidget():
    pass


@TODO
def gunner_stand():
    pass


@TODO
def gunner_walk():
    pass


@TODO
def gunner_run():
    pass


gunner_frames_pain3 = [
    mframe_t(ai_move, -3, None),
    mframe_t(ai_move, 1, None),
    mframe_t(ai_move, 1, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 1, None)
]

gunner_move_pain3 = mmove_t(FRAME_pain301, FRAME_pain305, gunner_frames_pain3, gunner_run)

gunner_frames_pain2 = [
    mframe_t(ai_move, -2, None),
    mframe_t(ai_move, 11, None),
    mframe_t(ai_move, 6, None),
    mframe_t(ai_move, 2, None),
    mframe_t(ai_move, -1, None),
    mframe_t(ai_move, -7, None),
    mframe_t(ai_move, -2, None),
    mframe_t(ai_move, -7, None)
]

gunner_move_pain2 = mmove_t(FRAME_pain201, FRAME_pain208, gunner_frames_pain2, gunner_run)

gunner_frames_pain1 = [
    mframe_t(ai_move, 2, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, -5, None),
    mframe_t(ai_move, 3, None),
    mframe_t(ai_move, -1, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 1, None),
    mframe_t(ai_move, 1, None),
    mframe_t(ai_move, 2, None),
    mframe_t(ai_move, 1, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, -2, None),
    mframe_t(ai_move, -2, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None)
]

gunner_move_pain1 = mmove_t(FRAME_pain101, FRAME_pain118, gunner_frames_pain1, gunner_run)


@TODO
def gunner_runandshoot():
    pass


def gunner_pain(_self, other, kick, damage):
    if _self.health < (_self.max_health/2):
        _self.skinnum = 1
    if level.time < _self.pain_debounce_time:
        return
    if damage <= 25 and random.uniform(0, 1) < 0.2:
        return
    _self.pain_debounce_time = level.time + 3
    if random.choice([True, False]):
        gi.sound(_self, SOUND_CHANNELS.CHAN_VOICE, sound_pain, 1, SOUND_ATTN_VALUES.ATTN_NORM, 0)
    else:
        gi.sound(_self, SOUND_CHANNELS.CHAN_VOICE, sound_pain2, 1, SOUND_ATTN_VALUES.ATTN_NORM, 0)
    if skill.value == 3:
        return

    if damage <= 10:
        _self.monsterinfo.currentmove = gunner_move_pain3
    elif damaga <= 25:
        _self.monsterinfo.currentmove = gunner_move_pain2
    else:
        _self.monsterinfo.currentmove = gunner_move_pain1


@TODO
def gunner_dead():
    pass


@TODO
def gunner_die():
    pass


@TODO
def gunner_duck_down():
    pass


@TODO
def gunner_duck_hold():
    pass


@TODO
def gunner_duck_up():
    pass


@TODO
def gunner_dodge():
    pass


@TODO
def gunner_opengun():
    pass


@TODO
def GunnerFire():
    pass


@TODO
def GunnerGrenade():
    pass


@TODO
def gunner_attack():
    pass


@TODO
def gunner_fire_chain():
    pass


@TODO
def gunner_refire_chain():
    pass


@TODO
def SP_monster_gunner():
    pass


from game.g_ai import ai_move
