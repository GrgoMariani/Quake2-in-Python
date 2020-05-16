from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable


@TODO
def GL_SetTexturePalette(palette):
    pass


@TODO
def GL_EnableMultitexture(enable):
    pass


@TODO
def GL_SelectTexture(texture):
    pass


@TODO
def GL_TexEnv(mode):
    pass


@TODO
def GL_Bind(texnum):
    pass


@TODO
def GL_MBind(target, texnum):
    pass


@TODO
def GL_TextureMode(string):
    pass


@TODO
def GL_TextureAlphaMode(string):
    pass


@TODO
def GL_TextureSolidMode(string):
    pass


@TODO
def GL_ImageList_f():
    pass


@TODO
def Scrap_AllocBlock(w, h, x: Mutable, y: Mutable):
    pass


@TODO
def Scrap_Upload():
    pass


@TODO
def LoadPCX(filename, pic, palette, width: Mutable, height: Mutable):
    pass


@TODO
def LoadTGA(name, pic, width: Mutable, height: Mutable):
    pass


@TODO
def R_FloodFillSkin(skin, skinwidth, skinheight):
    pass


@TODO
def GL_ResampleTexture(_in, inwidth, inheight, out, outwidth, outheight):
    pass


@TODO
def GL_LightScaleTexture(_in, inwidth, inheight, only_game):
    pass


@TODO
def GL_MipMap(_in, width, height):
    pass


@TODO
def GL_BuildPalettedTexture(paleetted_texture, scaled, scaled_width, scald_height):
    pass


@TODO
def GL_Upload32(data, width, height, mipmap):
    pass


@TODO
def GL_Upload8(data, width, height, mipmap, is_sky):
    pass


@TODO
def GL_LoadPic(name, pic, width, height, _type, bits):
    pass


@TODO
def GL_LoadWal(name):
    pass


@TODO
def GL_FindImage(name, _type):
    pass


@TODO
def R_RegisterSkin(name):
    pass


@TODO
def GL_FreeUnusedImages():
    pass


@TODO
def Draw_GetPalette():
    pass


@TODO
def GL_InitImages():
    pass


@TODO
def GL_ShutdownImages():
    pass
