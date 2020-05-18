from wrapper_qpy.decorators import TODO
from wrapper_qpy.linker import LinkEmptyFunctions


LinkEmptyFunctions(globals(), [])


@TODO
def CL_ClearLightStyles():
    pass


@TODO
def CL_RunLightStyles():
    pass


@TODO
def CL_SetLightstyle():
    pass


@TODO
def CL_AddLightStyles():
    pass


@TODO
def CL_ClearDlights():
    pass


@TODO
def CL_AllocDlight():
    pass


@TODO
def CL_NewDlight():
    pass


@TODO
def CL_RunDLights():
    pass


@TODO
def CL_ParseMuzzleFlash():
    pass


@TODO
def CL_ParseMuzzleFlash2():
    pass


@TODO
def CL_AddDLights():
    pass


@TODO
def CL_ClearParticles():
    pass


@TODO
def CL_ParticleEffect(org, _dir, color, count):
    pass


@TODO
def CL_ParticleEffect2(org, _dir, color, count):
    pass


@TODO
def CL_ParticleEffect3(org, _dir, color, count):
    pass


@TODO
def CL_TeleporterParticles(ent):
    pass


@TODO
def CL_LogoutEffect(org, type):
    pass


@TODO
def CL_ItemRespawnParticles(org):
    pass


@TODO
def CL_ExplosionParticles(org):
    pass


@TODO
def CL_BigTeleportParticles(org):
    pass


@TODO
def CL_BlasterParticles(org, _dir):
    pass


@TODO
def CL_BlasterTrail(start, end):
    pass


@TODO
def CL_QuadTrail(start, end):
    pass


@TODO
def CL_FlagTrail(start, end, color):
    pass


@TODO
def CL_DiminishingTrail(start, end, old, flags):
    pass


@TODO
def MakeNormalVectors(forward, right, up):
    pass


@TODO
def CL_RocketTrail(start, end, old):
    pass


@TODO
def CL_RailTrail(start, end):
    pass


@TODO
def CL_IonripperTrail(start, ent):
    pass


@TODO
def CL_BubbleTrail(start, end):
    pass


@TODO
def CL_FlyParticles(origin, count):
    pass


@TODO
def CL_FlyEffect(ent, origin):
    pass


@TODO
def CL_BfgParticles(ent):
    pass


@TODO
def CL_TrapParticles(ent):
    pass


@TODO
def CL_BFGExplosionParticles(org):
    pass


@TODO
def CL_TeleportParticles(org):
    pass


@TODO
def CL_AddParticles():
    pass


@TODO
def CL_EntityEvent(ent):
    pass


def CL_ClearEffects():
    CL_ClearParticles()
    CL_ClearDlights()
    CL_ClearLightStyles()
