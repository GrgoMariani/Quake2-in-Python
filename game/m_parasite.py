from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from .reference_import import gi
from wrapper_qpy.linker import LinkEmptyFunctions
from shared.QClasses import mmove_t, mframe_t


LinkEmptyFunctions(globals(), ["ai_stand"])


FRAME_break01 = 0
FRAME_break02 = 1
FRAME_break03 = 2
FRAME_break04 = 3
FRAME_break05 = 4
FRAME_break06 = 5
FRAME_break07 = 6
FRAME_break08 = 7
FRAME_break09 = 8
FRAME_break10 = 9
FRAME_break11 = 10
FRAME_break12 = 11
FRAME_break13 = 12
FRAME_break14 = 13
FRAME_break15 = 14
FRAME_break16 = 15
FRAME_break17 = 16
FRAME_break18 = 17
FRAME_break19 = 18
FRAME_break20 = 19
FRAME_break21 = 20
FRAME_break22 = 21
FRAME_break23 = 22
FRAME_break24 = 23
FRAME_break25 = 24
FRAME_break26 = 25
FRAME_break27 = 26
FRAME_break28 = 27
FRAME_break29 = 28
FRAME_break30 = 29
FRAME_break31 = 30
FRAME_break32 = 31
FRAME_death101 = 32
FRAME_death102 = 33
FRAME_death103 = 34
FRAME_death104 = 35
FRAME_death105 = 36
FRAME_death106 = 37
FRAME_death107 = 38
FRAME_drain01 = 39
FRAME_drain02 = 40
FRAME_drain03 = 41
FRAME_drain04 = 42
FRAME_drain05 = 43
FRAME_drain06 = 44
FRAME_drain07 = 45
FRAME_drain08 = 46
FRAME_drain09 = 47
FRAME_drain10 = 48
FRAME_drain11 = 49
FRAME_drain12 = 50
FRAME_drain13 = 51
FRAME_drain14 = 52
FRAME_drain15 = 53
FRAME_drain16 = 54
FRAME_drain17 = 55
FRAME_drain18 = 56
FRAME_pain101 = 57
FRAME_pain102 = 58
FRAME_pain103 = 59
FRAME_pain104 = 60
FRAME_pain105 = 61
FRAME_pain106 = 62
FRAME_pain107 = 63
FRAME_pain108 = 64
FRAME_pain109 = 65
FRAME_pain110 = 66
FRAME_pain111 = 67
FRAME_run01 = 68
FRAME_run02 = 69
FRAME_run03 = 70
FRAME_run04 = 71
FRAME_run05 = 72
FRAME_run06 = 73
FRAME_run07 = 74
FRAME_run08 = 75
FRAME_run09 = 76
FRAME_run10 = 77
FRAME_run11 = 78
FRAME_run12 = 79
FRAME_run13 = 80
FRAME_run14 = 81
FRAME_run15 = 82
FRAME_stand01 = 83
FRAME_stand02 = 84
FRAME_stand03 = 85
FRAME_stand04 = 86
FRAME_stand05 = 87
FRAME_stand06 = 88
FRAME_stand07 = 89
FRAME_stand08 = 90
FRAME_stand09 = 91
FRAME_stand10 = 92
FRAME_stand11 = 93
FRAME_stand12 = 94
FRAME_stand13 = 95
FRAME_stand14 = 96
FRAME_stand15 = 97
FRAME_stand16 = 98
FRAME_stand17 = 99
FRAME_stand18 = 100
FRAME_stand19 = 101
FRAME_stand20 = 102
FRAME_stand21 = 103
FRAME_stand22 = 104
FRAME_stand23 = 105
FRAME_stand24 = 106
FRAME_stand25 = 107
FRAME_stand26 = 108
FRAME_stand27 = 109
FRAME_stand28 = 110
FRAME_stand29 = 111
FRAME_stand30 = 112
FRAME_stand31 = 113
FRAME_stand32 = 114
FRAME_stand33 = 115
FRAME_stand34 = 116
FRAME_stand35 = 117

MODEL_SCALE = 1.000000



@TODO
def parasite_launch():
    pass


@TODO
def parasite_reel_in():
    pass


@TODO
def parasite_sight():
    pass


@TODO
def parasite_tap():
    pass


@TODO
def parasite_scratch():
    pass


@TODO
def parasite_search():
    pass


@TODO
def parasite_refidget():
    pass


@TODO
def parasite_stand():
    pass


parasite_frames_fidget = [
    mframe_t(ai_stand, 0, parasite_scratch),
    mframe_t(ai_stand, 0, None),
    mframe_t(ai_stand, 0, None),
    mframe_t(ai_stand, 0, parasite_scratch),
    mframe_t(ai_stand, 0, None),
    mframe_t(ai_stand, 0, None)
]
parasite_move_fidget = mmove_t(FRAME_stand22, FRAME_stand27, parasite_frames_fidget, parasite_refidget)

parasite_frames_end_fidget = [
    mframe_t(ai_stand, 0, parasite_scratch),
    mframe_t(ai_stand, 0, None),
    mframe_t(ai_stand, 0, None),
    mframe_t(ai_stand, 0, None),
    mframe_t(ai_stand, 0, None),
    mframe_t(ai_stand, 0, None)
]
parasite_move_end_fidget = mmove_t(FRAME_stand28, FRAME_stand35, parasite_frames_end_fidget, parasite_stand)


def parasite_end_fidget(_self):
    _self.monsterinfo.currentmove = parasite_move_end_fidget


def parasite_do_fidget(_self):
    _self.monsterinfo.currentmove = parasite_move_fidget


@TODO
def parasite_idle():
    pass


@TODO
def parasite_start_run():
    pass


@TODO
def parasite_run():
    pass


@TODO
def parasite_start_walk():
    pass


@TODO
def parasite_walk():
    pass


@TODO
def parasite_pain():
    pass


@TODO
def parasite_drain_attack_ok():
    pass


@TODO
def parasite_drain_attack():
    pass


@TODO
def parasite_attack():
    pass


@TODO
def parasite_dead():
    pass


@TODO
def parasite_die():
    pass


@TODO
def SP_monster_parasite():
    pass


from game.g_ai import ai_stand
