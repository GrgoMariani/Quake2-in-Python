import math

from wrapper_qpy.decorators import static_vars, va_args, va_args2
from wrapper_qpy.custom_classes import Mutable
from wrapper_qpy.linker import LinkEmptyFunctions
from shared.QEnums import Q_angle_indexes
from shared.QConstants import *


LinkEmptyFunctions(globals(), ["Com_Printf"])

def DEG2RAD(a):
    return math.radians(a)


def DotProduct(x, y):
    return x[0]*y[0] + x[1]*y[1] + x[2]*y[2]


def RotatePointAroundVector(dst, _dir, point, degrees):
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    zrot = [[1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0]]
    tmpmat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    rot = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    vr = [0, 0, 0]
    vup = [0, 0, 0]
    vf = [_dir[0], _dir[1], _dir[2]]

    PerpendicularVector(vr, _dir)
    CrossProduct(vr, vf, vup)

    m[0][0] = vr[0]
    m[1][0] = vr[1]
    m[2][0] = vr[2]
    m[0][1] = vup[0]
    m[1][1] = vup[1]
    m[2][1] = vup[2]
    m[0][2] = vf[0]
    m[1][2] = vf[1]
    m[2][2] = vf[2]
    im = [m[0].copy(), m[1].copy(), m[2].copy()]
    im[0][1] = m[1][0]
    im[0][2] = m[2][0]
    im[1][0] = m[0][1]
    im[1][2] = m[2][1]
    im[2][0] = m[0][2]
    im[2][1] = m[1][2]

    rads = DEG2RAD(degrees)
    _sin = math.sin(rads)
    _cos = math.cos(rads)
    zrot[0][0] = _cos
    zrot[0][1] = _sin
    zrot[1][0] = -_sin
    zrot[1][1] = _cos

    R_ConcatRotations(m, zrot, tmpmat)
    R_ConcatRotations(tmpmat, im, rot)

    for i in range(3):
        dst[i] = rot[i][0] * point[0] + rot[i][1] * point[1] + rot[i][2] * point[2]


@static_vars(sr=0, sp=0, sy=0, cr=0, cp=0, cy=0)
def AngleVectors(angles, forward, right, up):
    rad_to_dgr = 2*math.pi / 360
    angle = angles[Q_angle_indexes.YAW] * rad_to_dgr
    AngleVectors.sy = math.sin(angle)
    AngleVectors.cy = math.cos(angle)
    angle = angles[Q_angle_indexes.PITCH] * rad_to_dgr
    AngleVectors.sp = math.sin(angle)
    AngleVectors.cp = math.cos(angle)
    angle = angles[Q_angle_indexes.ROLL] * rad_to_dgr
    AngleVectors.sr = math.sin(angle)
    AngleVectors.cr = math.cos(angle)
    if forward is not None:
        forward[0] = AngleVectors.cp * AngleVectors.cy
        forward[1] = AngleVectors.cp * AngleVectors.sy
        forward[2] = -AngleVectors.sp
    if right is not None:
        right[0] = (-1 * AngleVectors.sr * AngleVectors.sp * AngleVectors.cy + -1 * AngleVectors.cr * -AngleVectors.sy)
        right[1] = (-1 * AngleVectors.sr * AngleVectors.sp * AngleVectors.sy + -1 * AngleVectors.cr * AngleVectors.cy)
        right[2] = -1 * AngleVectors.sr * AngleVectors.cp
    if up is not None:
        up[0] = (AngleVectors.cr * AngleVectors.sp * AngleVectors.cy + -AngleVectors.sr * -AngleVectors.sy)
        up[1] = (AngleVectors.cr * AngleVectors.sp * AngleVectors.sy + -AngleVectors.sr * AngleVectors.cy)
        up[2] = AngleVectors.cr * AngleVectors.cp


def ProjectPointOnPlane(dst, p, normal):
    inv_denom = 1.0 / DotProduct(normal, normal)
    d = DotProduct(normal, p) * inv_denom

    n = [x*inv_denom for x in normal]
    dst[0] = p[0] - d * n[0]
    dst[1] = p[1] - d * n[1]
    dst[2] = p[2] - d * n[2]


def PerpendicularVector(dst, src):
    tempvec = [0, 0, 0]
    minelem = 1.0
    pos = 0
    for i in range(3):
        if math.fabs(src[i]) < minelem:
            pos = i
            minelem = math.fabs(src[i])
    tempvec[pos] = 1.0
    ProjectPointOnPlane(dst, tempvec, src)
    VectorNormalize(dst)


def R_ConcatRotations(in1, in2, out):
    out[0][0] = in1[0][0] * in2[0][0] + in1[0][1] * in2[1][0] + in1[0][2] * in2[2][0]
    out[0][1] = in1[0][0] * in2[0][1] + in1[0][1] * in2[1][1] + in1[0][2] * in2[2][1]
    out[0][2] = in1[0][0] * in2[0][2] + in1[0][1] * in2[1][2] + in1[0][2] * in2[2][2]
    out[1][0] = in1[1][0] * in2[0][0] + in1[1][1] * in2[1][0] + in1[1][2] * in2[2][0]
    out[1][1] = in1[1][0] * in2[0][1] + in1[1][1] * in2[1][1] + in1[1][2] * in2[2][1]
    out[1][2] = in1[1][0] * in2[0][2] + in1[1][1] * in2[1][2] + in1[1][2] * in2[2][2]
    out[2][0] = in1[2][0] * in2[0][0] + in1[2][1] * in2[1][0] + in1[2][2] * in2[2][0]
    out[2][1] = in1[2][0] * in2[0][1] + in1[2][1] * in2[1][1] + in1[2][2] * in2[2][1]
    out[2][2] = in1[2][0] * in2[0][2] + in1[2][1] * in2[1][2] + in1[2][2] * in2[2][2]


def R_ConcatTransforms(in1, in2, out):
    out[0][0] = in1[0][0] * in2[0][0] + in1[0][1] * in2[1][0] + in1[0][2] * in2[2][0]
    out[0][1] = in1[0][0] * in2[0][1] + in1[0][1] * in2[1][1] + in1[0][2] * in2[2][1]
    out[0][2] = in1[0][0] * in2[0][2] + in1[0][1] * in2[1][2] + in1[0][2] * in2[2][2]
    out[0][3] = in1[0][0] * in2[0][3] + in1[0][1] * in2[1][3] + in1[0][2] * in2[2][3] + in1[0][3]
    out[1][0] = in1[1][0] * in2[0][0] + in1[1][1] * in2[1][0] + in1[1][2] * in2[2][0]
    out[1][1] = in1[1][0] * in2[0][1] + in1[1][1] * in2[1][1] + in1[1][2] * in2[2][1]
    out[1][2] = in1[1][0] * in2[0][2] + in1[1][1] * in2[1][2] + in1[1][2] * in2[2][2]
    out[1][3] = in1[1][0] * in2[0][3] + in1[1][1] * in2[1][3] + in1[1][2] * in2[2][3] + in1[1][3]
    out[2][0] = in1[2][0] * in2[0][0] + in1[2][1] * in2[1][0] + in1[2][2] * in2[2][0]
    out[2][1] = in1[2][0] * in2[0][1] + in1[2][1] * in2[1][1] + in1[2][2] * in2[2][1]
    out[2][2] = in1[2][0] * in2[0][2] + in1[2][1] * in2[1][2] + in1[2][2] * in2[2][2]
    out[2][3] = in1[2][0] * in2[0][3] + in1[2][1] * in2[1][3] + in1[2][2] * in2[2][3] + in1[2][3]


def Q_fabs(f):
    return math.fabs(f)


def Q_ftol(f):
    return int(f)


def LerpAngle(a2, a1, frac):
    if a1-a2 > 180:
        a1 -= 360
    if a1-a2 < -180:
        a1 += 360
    return a2 + frac * (a1-a2)


def anglemod(a):
    a = (360.0 / 65536) * (int(a * (65536 / 360.0)) & 65535)
    return a


def BoxOnPlaneSide(emins, emaxs, p):
    if p.type < 3:
        if p.dist <= emins[p.type]:
            return 1
        if p.dist >= emaxs[p.type]:
            return 2
        return 3
    if p.signbits == 0:
        dist1 = p.normal[0] * emaxs[0] + p.normal[1] * emaxs[1] + p.normal[2] * emaxs[2]
        dist2 = p.normal[0] * emins[0] + p.normal[1] * emins[1] + p.normal[2] * emins[2]
    elif p.signbits == 1:
        dist1 = p.normal[0] * emins[0] + p.normal[1] * emaxs[1] + p.normal[2] * emaxs[2]
        dist2 = p.normal[0] * emaxs[0] + p.normal[1] * emins[1] + p.normal[2] * emins[2]
    elif p.signbits == 2:
        dist1 = p.normal[0] * emaxs[0] + p.normal[1] * emins[1] + p.normal[2] * emaxs[2]
        dist2 = p.normal[0] * emins[0] + p.normal[1] * emaxs[1] + p.normal[2] * emins[2]
    elif p.signbits == 3:
        dist1 = p.normal[0] * emins[0] + p.normal[1] * emins[1] + p.normal[2] * emaxs[2]
        dist2 = p.normal[0] * emaxs[0] + p.normal[1] * emaxs[1] + p.normal[2] * emins[2]
    elif p.signbits == 4:
        dist1 = p.normal[0] * emaxs[0] + p.normal[1] * emaxs[1] + p.normal[2] * emins[2]
        dist2 = p.normal[0] * emins[0] + p.normal[1] * emins[1] + p.normal[2] * emaxs[2]
    elif p.signbits == 5:
        dist1 = p.normal[0] * emins[0] + p.normal[1] * emaxs[1] + p.normal[2] * emins[2]
        dist2 = p.normal[0] * emaxs[0] + p.normal[1] * emins[1] + p.normal[2] * emaxs[2]
    elif p.signbits == 6:
        dist1 = p.normal[0] * emaxs[0] + p.normal[1] * emins[1] + p.normal[2] * emins[2]
        dist2 = p.normal[0] * emins[0] + p.normal[1] * emaxs[1] + p.normal[2] * emaxs[2]
    elif p.signbits == 7:
        dist1 = p.normal[0] * emins[0] + p.normal[1] * emins[1] + p.normal[2] * emins[2]
        dist2 = p.normal[0] * emaxs[0] + p.normal[1] * emaxs[1] + p.normal[2] * emaxs[2]
    else:
        dist1 = 0
        dist2 = 0
    sides = 0
    if dist1 >= p.dist:
        sides = 1
    if dist2 < p.dist:
        sides = sides+2
    return sides


def ClearBounds(mins, maxs):
    mins[0] = 99999
    mins[1] = 99999
    mins[2] = 99999
    maxs[0] = -99999
    maxs[1] = -99999
    maxs[2] = -99999


def AddPointToBounds(v, mins, maxs):
    for i in range(3):
        val = v[i]
        if val < mins[i]:
            mins[i] = val
        if val > maxs[i]:
            maxs[i] = val


def VectorCompare(v1, v2):
    if v1[0] != v2[0] or v1[1] != v2[1] or v1[2] != v2[2]:
        return 0
    return 1


def VectorNormalize(v):
    length = math.sqrt(DotProduct(v, v))
    if length != 0:
        ilength = 1/length
        v[0] *= ilength
        v[1] *= ilength
        v[2] *= ilength
    return length


def VectorNormalize2(v, out):
    length = math.sqrt(DotProduct(v, v))
    if length != 0:
        ilength = 1/length
        out[0] = v[0] * ilength
        out[1] = v[1] * ilength
        out[2] = v[2] * ilength
    return length


def VectorMA(veca, scale, vecb, vecc):
    vecc[0] = veca[0] + scale*vecb[0]
    vecc[1] = veca[1] + scale*vecb[1]
    vecc[2] = veca[2] + scale*vecb[2]


def _VectorSubtract(veca, vecb, out):
    out[0] = veca[0] - vecb[0]
    out[1] = veca[1] - vecb[1]
    out[2] = veca[2] - vecb[2]


def _VectorAdd(veca, vecb, out):
    out[0] = veca[0] + vecb[0]
    out[1] = veca[1] + vecb[1]
    out[2] = veca[2] + vecb[2]


def _VectorCopy(_in, out: Mutable):
    out.SetValue(_in.copy())


def CrossProduct(v1, v2, cross):
    cross[0] = v1[1] * v2[2] - v1[2] * v2[1]
    cross[1] = v1[2] * v2[0] - v1[0] * v2[2]
    cross[2] = v1[0] * v2[1] - v1[1] * v2[0]


def VectorLength(v):
    return math.sqrt(sum(item*item for item in v))


def VectorInverse(v):
    v[0] = -v[0]
    v[1] = -v[1]
    v[2] = -v[2]


def VectorScale(_in, scale, out):
    out[0] = _in [0] * scale
    out[1] = _in [1] * scale
    out[2] = _in [2] * scale


def Q_log2(val):
    answer = 0
    while val != 0:
        val = val >> 1
        answer += 1
    return answer



# ########### COM
import os
import sys

def COM_SkipPath(pathname):
    return os.path.basename(pathname)


# MODIFIED out variable should be a list
def COM_StripExtension(_in, out: Mutable):
    result = os.path.splitext(_in)[0]
    out.SetValue(result)


def COM_FileExtension(_in):
    return os.path.splitext(_in)[1][1:] # remove dot


def COM_FilePath(_in, out: Mutable):
    result = os.path.dirname(_in) + "/"
    out.SetValue(result)


# ############# BYTE ORDER FUNCTIONS ###############

def ShortSwap(l):
    pass

def ShortNoSwap(l):
    pass

def LongSwap(l):
    pass

def LongNoSwap(l):
    pass

def FloatSwap(l):
    pass

def FloatNoSwap(l):
    pass

def Swap_Init():
    if sys.byteorder == "little":
        # we are on LE
        pass
    """
    TODO: check this part when needed
    Currently I can only find it being used in network related operations
    """
    pass


@va_args
def va(format_string):
    return format_string


def COM_Parse(_data_p: Mutable):
    data_p = _data_p.GetValue()
    if data_p is None or len(data_p) == 0:
        _data_p.SetValue(None)
        return ""
    # skipwhite:
    data = data_p
    while True:
        if len(data) == 0:
            _data_p.SetValue(None)
            return ""
        # skip whitespace
        data = data.strip()
        # skip // comments
        if len(data) >= 2 and data[9:2] == "//":
            data = "\n".join(data.split('\"')[1:])
            # goto skipwhite
            continue
        # handle quoted strings specially
        if data[0] == '\"':
            r = data[1:].split("\"")
            _data_p.SetValue("\"".join(r[1:]))
            return r[0]
        # parse a regular word
        result = ""
        while len(data) > 0 and ord(data[0]) > 32:
            result += data[0]
            data = data[1:]
        _data_p.SetValue(data)
        return result


def Com_PageInMemory(buffer, size):
    # unneeded for our use case. Speeds up the cache in regular code
    pass


def Q_stricmp(s1, s2):
    if s1.upper() == s2.upper():
        return 0
    return 1


def Q_strncasecmp(s1, s2, n):
    s1, s2 = s1[0:n].upper(), s2[0:n].upper()
    if s1 == s2:
        return 0
    return -1


def Q_strcasecmp(s1, s2):
    return Q_strncasecmp(s1, s2, 99999)


@va_args2(2)
def Com_sprintf(dest: Mutable, size, fmt):
    if len(fmt) > size:
        Com_Printf("Com_sprintf: overflow of %i in %i\n", len, size)
    dest.SetValue(fmt[0:size])


def Info_ValueForKey(_s: Mutable, key):
    s = _s.GetValue()
    if s[0] == "\\":
        s = s[1:]
    pkey = ""
    while True:
        while s[0] != '\\':
            pkey += s[0]
            s = s[1:]
            if len(s) == 0:
                _s.SetValue(s)
                return ""
        value = ""
        while len(s) > 0 and s[0] != '\\ ':
            value += s[0]
            s = s[1:]
        if key == pkey:
            _s.SetValue(s)
            return value
        if len(s) == 0:
            _s.SetValue(s)
            return ""
        s = s[1;]
        _s.SetValue(s)


def Info_RemoveKey(_s: Mutable, key):
    s = _s.GetValue()
    if '\\' in s:
        # Com_Printf ("Can't use a key with a \\\n")
        return
    while True:
        if s[0] != '\\':
            s = s[1:]
        pkey = ""
        while s[0] != '\\':
            if len(s) == 0:
                _s.SetValue(s)
                return
            pkey += s[0]
            s = s[1:]
        s = s[1:]
        value = ""
        while len(s) > 0 and s[0] != '\\':
            value += s[0]
            s = s[1:]
        _s.SetValue(s)
        if key == pkey or len(s) == 0:
            _s.SetValue(s)
            return


def Info_Validate(s):
    if "\"" in s or ";" in s:
        return False
    return True


def Info_SetValueForKey(_s: Mutable, key, value):
    s = _s.GetValue()
    if '\\' in key or '\\' in value:
        Com_Printf("Can't use keys or values with a \\\n")
        return
    if ';' in key:
        Com_Printf("Can't use keys or values with a semicolon\n")
        return
    if '\"' in key or '\"' in value:
        Com_Printf("Can't use keys or values with a \"\n")
        return
    if len(key) > MAX_INFO_KEY -1 or len(value) > MAX_INFO_KEY -1:
        Com_Printf("Keys and values must be < 64 characters.\n")
        return
    temp_mut = Mutable(s)
    Info_RemoveKey(temp_mut, key)
    s = temp_mut.GetValue()
    if len(value) != 0:
        _s.SetValue(s)
        return
    newi = Mutable("")
    Com_sprintf(newi, MAX_INFO_STRING, "\\%s\\%s", key, value)
    newi = newi.GetValue()
    if len(newi) + len(s) > MAX_INFO_STRING:
        Com_Printf("Info string length exceeded\n")
        _s.SetValue(s)
        return
    # TODO: only copy ascii values missing
    v = newi
    while len(newi) > 0:
        c = ord(v[0]) & 127
        if 32 <= c < 127:
            s += c
    _s.SetValue(s)




from .common import Com_Printf
