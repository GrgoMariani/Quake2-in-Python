from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def CanDamage(targ, inflictor):
    pass


@TODO
def Killed(targ, inflictor, attacker, damage, point):
    pass


@TODO
def SpawnDamage(_type, origin, normal, damage):
    pass


@TODO
def CheckPowerArmor(ent, point, normal, damage, dflags):
    pass


@TODO
def CheckArmor(ent, point, normal, damage, te_sparks, dflags):
    pass


@TODO
def M_ReactToDamage(targ, attacker):
    pass


@TODO
def CheckTeamDamage(targ, attacker):
    pass


@TODO
def T_Damage(targ, inflictor, attacker, _dir, point, normal, damage, knockback, dflags, _mod):
    pass


@TODO
def T_RadiusDamage(inflictor, attacker, damage, ignore, radius, _mod):
    pass
