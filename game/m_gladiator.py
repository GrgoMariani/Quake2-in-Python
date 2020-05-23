from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from .reference_import import gi
from wrapper_qpy.linker import LinkEmptyFunctions
from .m_flash import monster_flash_offset
from shared.QConstants import MZ2_GLADIATOR_RAILGUN_1


LinkEmptyFunctions(globals(), ["AngleVectors", "G_ProjectSource", "_VectorSubtract", "VectorNormalize"])


@TODO
def gladiator_idle():
    pass


@TODO
def gladiator_sight():
    pass


@TODO
def gladiator_search():
    pass


@TODO
def gladiator_cleaver_swing():
    pass


@TODO
def gladiator_stand():
    pass


@TODO
def gladiator_walk():
    pass


@TODO
def gladiator_run():
    pass


@TODO
def GaldiatorMelee():
    pass


@TODO
def gladiator_melee():
    pass


def GladiatorGun(_self):
    start = [0, 0, 0]
    _dir = [0, 0, 0]
    forward = [0, 0, 0]
    right = [0, 0, 0]
    AngleVectors(_self.s.angles, forward, right, None)
    G_ProjectSource(_self.s.origin, monster_flash_offset[MZ2_GLADIATOR_RAILGUN_1], forward, right, start)
    _VectorSubtract(_self.pos1, start, _dir)
    VectorNormalize(_dir)
    monster_fire_railgun(_self, start, _dir, 50, 100, MZ2_GLADIATOR_RAILGUN_1)


@TODO
def gladiator_attack():
    pass


@TODO
def gladiator_pain():
    pass


@TODO
def gladiator_dead():
    pass


@TODO
def gladiator_die():
    pass


@TODO
def SP_monster_gladiator():
    pass


from .q_shared import AngleVectors, _VectorSubtract, VectorNormalize
from .g_utils import G_ProjectSource
from .g_monster import monster_fire_railgun
