from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from .reference_import import gi
from wrapper_qpy.linker import LinkEmptyFunctions
from shared.QEnums import MONSTER_AI_FLAGS
from .global_vars import level


LinkEmptyFunctions(globals(), [])


actor_names = [
    "Hellrot",
    "Tokay",
    "Killme",
    "Disruptor",
    "Adrianator",
    "Rambear",
    "Titus",
    "Bitterman"
]
MAX_ACTOR_NAMES = len(actor_names)

@TODO
def actor_stand():
    pass


@TODO
def actor_walk():
    pass


@TODO
def actor_run():
    pass


@TODO
def actor_pain():
    pass


@TODO
def actorMachineGun():
    pass


@TODO
def actor_dead():
    pass


@TODO
def actor_die():
    pass


def actor_fire(_self):
    actorMachineGun(_self)
    if level.time >= _self.monsterinfo.pausetime:
        _self.monsterinfo.aiflags &= ~MONSTER_AI_FLAGS.AI_HOLD_FRAME
    else:
        _self.monsterinfo.aiflags &= MONSTER_AI_FLAGS.AI_HOLD_FRAME


@TODO
def actor_attack():
    pass


@TODO
def actor_use():
    pass


@TODO
def SP_misc_actor():
    pass


@TODO
def target_actor_touch():
    pass


@TODO
def SP_target_actor():
    pass
