import random
from wrapper_qpy.decorators import TODO
from wrapper_qpy.custom_classes import Mutable
from .reference_import import gi
from wrapper_qpy.linker import LinkEmptyFunctions
from shared.QEnums import SOUND_ATTN_VALUES, SOUND_CHANNELS
from shared.QClasses import mmove_t, mframe_t
from .global_vars import level, skill
from .m_flash import monster_flash_offset
from shared.QConstants import MZ2_MAKRON_RAILGUN_1


LinkEmptyFunctions(globals(), ["ai_move", "AngleVectors", "G_ProjectSource", "_VectorSubtract", "VectorNormalize",
                               "monster_fire_railgun"])


FRAME_attak101 = 0
FRAME_attak102 = 1
FRAME_attak103 = 2
FRAME_attak104 = 3
FRAME_attak105 = 4
FRAME_attak106 = 5
FRAME_attak107 = 6
FRAME_attak108 = 7
FRAME_attak109 = 8
FRAME_attak110 = 9
FRAME_attak111 = 10
FRAME_attak112 = 11
FRAME_attak113 = 12
FRAME_attak114 = 13
FRAME_attak115 = 14
FRAME_attak116 = 15
FRAME_attak117 = 16
FRAME_attak118 = 17
FRAME_attak201 = 18
FRAME_attak202 = 19
FRAME_attak203 = 20
FRAME_attak204 = 21
FRAME_attak205 = 22
FRAME_attak206 = 23
FRAME_attak207 = 24
FRAME_attak208 = 25
FRAME_attak209 = 26
FRAME_attak210 = 27
FRAME_attak211 = 28
FRAME_attak212 = 29
FRAME_attak213 = 30
FRAME_death01 = 31
FRAME_death02 = 32
FRAME_death03 = 33
FRAME_death04 = 34
FRAME_death05 = 35
FRAME_death06 = 36
FRAME_death07 = 37
FRAME_death08 = 38
FRAME_death09 = 39
FRAME_death10 = 40
FRAME_death11 = 41
FRAME_death12 = 42
FRAME_death13 = 43
FRAME_death14 = 44
FRAME_death15 = 45
FRAME_death16 = 46
FRAME_death17 = 47
FRAME_death18 = 48
FRAME_death19 = 49
FRAME_death20 = 50
FRAME_death21 = 51
FRAME_death22 = 52
FRAME_death23 = 53
FRAME_death24 = 54
FRAME_death25 = 55
FRAME_death26 = 56
FRAME_death27 = 57
FRAME_death28 = 58
FRAME_death29 = 59
FRAME_death30 = 60
FRAME_death31 = 61
FRAME_death32 = 62
FRAME_death33 = 63
FRAME_death34 = 64
FRAME_death35 = 65
FRAME_death36 = 66
FRAME_death37 = 67
FRAME_death38 = 68
FRAME_death39 = 69
FRAME_death40 = 70
FRAME_death41 = 71
FRAME_death42 = 72
FRAME_death43 = 73
FRAME_death44 = 74
FRAME_death45 = 75
FRAME_death46 = 76
FRAME_death47 = 77
FRAME_death48 = 78
FRAME_death49 = 79
FRAME_death50 = 80
FRAME_pain101 = 81
FRAME_pain102 = 82
FRAME_pain103 = 83
FRAME_pain201 = 84
FRAME_pain202 = 85
FRAME_pain203 = 86
FRAME_pain301 = 87
FRAME_pain302 = 88
FRAME_pain303 = 89
FRAME_pain304 = 90
FRAME_pain305 = 91
FRAME_pain306 = 92
FRAME_pain307 = 93
FRAME_pain308 = 94
FRAME_pain309 = 95
FRAME_pain310 = 96
FRAME_pain311 = 97
FRAME_pain312 = 98
FRAME_pain313 = 99
FRAME_pain314 = 100
FRAME_pain315 = 101
FRAME_pain316 = 102
FRAME_pain317 = 103
FRAME_pain318 = 104
FRAME_pain319 = 105
FRAME_pain320 = 106
FRAME_pain321 = 107
FRAME_pain322 = 108
FRAME_pain323 = 109
FRAME_pain324 = 110
FRAME_pain325 = 111
FRAME_stand01 = 112
FRAME_stand02 = 113
FRAME_stand03 = 114
FRAME_stand04 = 115
FRAME_stand05 = 116
FRAME_stand06 = 117
FRAME_stand07 = 118
FRAME_stand08 = 119
FRAME_stand09 = 120
FRAME_stand10 = 121
FRAME_stand11 = 122
FRAME_stand12 = 123
FRAME_stand13 = 124
FRAME_stand14 = 125
FRAME_stand15 = 126
FRAME_stand16 = 127
FRAME_stand17 = 128
FRAME_stand18 = 129
FRAME_stand19 = 130
FRAME_stand20 = 131
FRAME_stand21 = 132
FRAME_stand22 = 133
FRAME_stand23 = 134
FRAME_stand24 = 135
FRAME_stand25 = 136
FRAME_stand26 = 137
FRAME_stand27 = 138
FRAME_stand28 = 139
FRAME_stand29 = 140
FRAME_stand30 = 141
FRAME_stand31 = 142
FRAME_stand32 = 143
FRAME_stand33 = 144
FRAME_stand34 = 145
FRAME_stand35 = 146
FRAME_stand36 = 147
FRAME_stand37 = 148
FRAME_stand38 = 149
FRAME_stand39 = 150
FRAME_stand40 = 151
FRAME_stand41 = 152
FRAME_stand42 = 153
FRAME_stand43 = 154
FRAME_stand44 = 155
FRAME_stand45 = 156
FRAME_stand46 = 157
FRAME_stand47 = 158
FRAME_stand48 = 159
FRAME_stand49 = 160
FRAME_stand50 = 161
FRAME_stand51 = 162
FRAME_walk01 = 163
FRAME_walk02 = 164
FRAME_walk03 = 165
FRAME_walk04 = 166
FRAME_walk05 = 167
FRAME_walk06 = 168
FRAME_walk07 = 169
FRAME_walk08 = 170
FRAME_walk09 = 171
FRAME_walk10 = 172
FRAME_walk11 = 173
FRAME_walk12 = 174
FRAME_walk13 = 175
FRAME_walk14 = 176
FRAME_walk15 = 177
FRAME_walk16 = 178
FRAME_walk17 = 179
FRAME_walk18 = 180
FRAME_walk19 = 181
FRAME_walk20 = 182
FRAME_walk21 = 183
FRAME_walk22 = 184
FRAME_walk23 = 185
FRAME_walk24 = 186
FRAME_walk25 = 187
FRAME_active01 = 188
FRAME_active02 = 189
FRAME_active03 = 190
FRAME_active04 = 191
FRAME_active05 = 192
FRAME_active06 = 193
FRAME_active07 = 194
FRAME_active08 = 195
FRAME_active09 = 196
FRAME_active10 = 197
FRAME_active11 = 198
FRAME_active12 = 199
FRAME_active13 = 200
FRAME_attak301 = 201
FRAME_attak302 = 202
FRAME_attak303 = 203
FRAME_attak304 = 204
FRAME_attak305 = 205
FRAME_attak306 = 206
FRAME_attak307 = 207
FRAME_attak308 = 208
FRAME_attak401 = 209
FRAME_attak402 = 210
FRAME_attak403 = 211
FRAME_attak404 = 212
FRAME_attak405 = 213
FRAME_attak406 = 214
FRAME_attak407 = 215
FRAME_attak408 = 216
FRAME_attak409 = 217
FRAME_attak410 = 218
FRAME_attak411 = 219
FRAME_attak412 = 220
FRAME_attak413 = 221
FRAME_attak414 = 222
FRAME_attak415 = 223
FRAME_attak416 = 224
FRAME_attak417 = 225
FRAME_attak418 = 226
FRAME_attak419 = 227
FRAME_attak420 = 228
FRAME_attak421 = 229
FRAME_attak422 = 230
FRAME_attak423 = 231
FRAME_attak424 = 232
FRAME_attak425 = 233
FRAME_attak426 = 234
FRAME_attak501 = 235
FRAME_attak502 = 236
FRAME_attak503 = 237
FRAME_attak504 = 238
FRAME_attak505 = 239
FRAME_attak506 = 240
FRAME_attak507 = 241
FRAME_attak508 = 242
FRAME_attak509 = 243
FRAME_attak510 = 244
FRAME_attak511 = 245
FRAME_attak512 = 246
FRAME_attak513 = 247
FRAME_attak514 = 248
FRAME_attak515 = 249
FRAME_attak516 = 250
FRAME_death201 = 251
FRAME_death202 = 252
FRAME_death203 = 253
FRAME_death204 = 254
FRAME_death205 = 255
FRAME_death206 = 256
FRAME_death207 = 257
FRAME_death208 = 258
FRAME_death209 = 259
FRAME_death210 = 260
FRAME_death211 = 261
FRAME_death212 = 262
FRAME_death213 = 263
FRAME_death214 = 264
FRAME_death215 = 265
FRAME_death216 = 266
FRAME_death217 = 267
FRAME_death218 = 268
FRAME_death219 = 269
FRAME_death220 = 270
FRAME_death221 = 271
FRAME_death222 = 272
FRAME_death223 = 273
FRAME_death224 = 274
FRAME_death225 = 275
FRAME_death226 = 276
FRAME_death227 = 277
FRAME_death228 = 278
FRAME_death229 = 279
FRAME_death230 = 280
FRAME_death231 = 281
FRAME_death232 = 282
FRAME_death233 = 283
FRAME_death234 = 284
FRAME_death235 = 285
FRAME_death236 = 286
FRAME_death237 = 287
FRAME_death238 = 288
FRAME_death239 = 289
FRAME_death240 = 290
FRAME_death241 = 291
FRAME_death242 = 292
FRAME_death243 = 293
FRAME_death244 = 294
FRAME_death245 = 295
FRAME_death246 = 296
FRAME_death247 = 297
FRAME_death248 = 298
FRAME_death249 = 299
FRAME_death250 = 300
FRAME_death251 = 301
FRAME_death252 = 302
FRAME_death253 = 303
FRAME_death254 = 304
FRAME_death255 = 305
FRAME_death256 = 306
FRAME_death257 = 307
FRAME_death258 = 308
FRAME_death259 = 309
FRAME_death260 = 310
FRAME_death261 = 311
FRAME_death262 = 312
FRAME_death263 = 313
FRAME_death264 = 314
FRAME_death265 = 315
FRAME_death266 = 316
FRAME_death267 = 317
FRAME_death268 = 318
FRAME_death269 = 319
FRAME_death270 = 320
FRAME_death271 = 321
FRAME_death272 = 322
FRAME_death273 = 323
FRAME_death274 = 324
FRAME_death275 = 325
FRAME_death276 = 326
FRAME_death277 = 327
FRAME_death278 = 328
FRAME_death279 = 329
FRAME_death280 = 330
FRAME_death281 = 331
FRAME_death282 = 332
FRAME_death283 = 333
FRAME_death284 = 334
FRAME_death285 = 335
FRAME_death286 = 336
FRAME_death287 = 337
FRAME_death288 = 338
FRAME_death289 = 339
FRAME_death290 = 340
FRAME_death291 = 341
FRAME_death292 = 342
FRAME_death293 = 343
FRAME_death294 = 344
FRAME_death295 = 345
FRAME_death301 = 346
FRAME_death302 = 347
FRAME_death303 = 348
FRAME_death304 = 349
FRAME_death305 = 350
FRAME_death306 = 351
FRAME_death307 = 352
FRAME_death308 = 353
FRAME_death309 = 354
FRAME_death310 = 355
FRAME_death311 = 356
FRAME_death312 = 357
FRAME_death313 = 358
FRAME_death314 = 359
FRAME_death315 = 360
FRAME_death316 = 361
FRAME_death317 = 362
FRAME_death318 = 363
FRAME_death319 = 364
FRAME_death320 = 365
FRAME_jump01 = 366
FRAME_jump02 = 367
FRAME_jump03 = 368
FRAME_jump04 = 369
FRAME_jump05 = 370
FRAME_jump06 = 371
FRAME_jump07 = 372
FRAME_jump08 = 373
FRAME_jump09 = 374
FRAME_jump10 = 375
FRAME_jump11 = 376
FRAME_jump12 = 377
FRAME_jump13 = 378
FRAME_pain401 = 379
FRAME_pain402 = 380
FRAME_pain403 = 381
FRAME_pain404 = 382
FRAME_pain501 = 383
FRAME_pain502 = 384
FRAME_pain503 = 385
FRAME_pain504 = 386
FRAME_pain601 = 387
FRAME_pain602 = 388
FRAME_pain603 = 389
FRAME_pain604 = 390
FRAME_pain605 = 391
FRAME_pain606 = 392
FRAME_pain607 = 393
FRAME_pain608 = 394
FRAME_pain609 = 395
FRAME_pain610 = 396
FRAME_pain611 = 397
FRAME_pain612 = 398
FRAME_pain613 = 399
FRAME_pain614 = 400
FRAME_pain615 = 401
FRAME_pain616 = 402
FRAME_pain617 = 403
FRAME_pain618 = 404
FRAME_pain619 = 405
FRAME_pain620 = 406
FRAME_pain621 = 407
FRAME_pain622 = 408
FRAME_pain623 = 409
FRAME_pain624 = 410
FRAME_pain625 = 411
FRAME_pain626 = 412
FRAME_pain627 = 413
FRAME_stand201 = 414
FRAME_stand202 = 415
FRAME_stand203 = 416
FRAME_stand204 = 417
FRAME_stand205 = 418
FRAME_stand206 = 419
FRAME_stand207 = 420
FRAME_stand208 = 421
FRAME_stand209 = 422
FRAME_stand210 = 423
FRAME_stand211 = 424
FRAME_stand212 = 425
FRAME_stand213 = 426
FRAME_stand214 = 427
FRAME_stand215 = 428
FRAME_stand216 = 429
FRAME_stand217 = 430
FRAME_stand218 = 431
FRAME_stand219 = 432
FRAME_stand220 = 433
FRAME_stand221 = 434
FRAME_stand222 = 435
FRAME_stand223 = 436
FRAME_stand224 = 437
FRAME_stand225 = 438
FRAME_stand226 = 439
FRAME_stand227 = 440
FRAME_stand228 = 441
FRAME_stand229 = 442
FRAME_stand230 = 443
FRAME_stand231 = 444
FRAME_stand232 = 445
FRAME_stand233 = 446
FRAME_stand234 = 447
FRAME_stand235 = 448
FRAME_stand236 = 449
FRAME_stand237 = 450
FRAME_stand238 = 451
FRAME_stand239 = 452
FRAME_stand240 = 453
FRAME_stand241 = 454
FRAME_stand242 = 455
FRAME_stand243 = 456
FRAME_stand244 = 457
FRAME_stand245 = 458
FRAME_stand246 = 459
FRAME_stand247 = 460
FRAME_stand248 = 461
FRAME_stand249 = 462
FRAME_stand250 = 463
FRAME_stand251 = 464
FRAME_stand252 = 465
FRAME_stand253 = 466
FRAME_stand254 = 467
FRAME_stand255 = 468
FRAME_stand256 = 469
FRAME_stand257 = 470
FRAME_stand258 = 471
FRAME_stand259 = 472
FRAME_stand260 = 473
FRAME_walk201 = 474
FRAME_walk202 = 475
FRAME_walk203 = 476
FRAME_walk204 = 477
FRAME_walk205 = 478
FRAME_walk206 = 479
FRAME_walk207 = 480
FRAME_walk208 = 481
FRAME_walk209 = 482
FRAME_walk210 = 483
FRAME_walk211 = 484
FRAME_walk212 = 485
FRAME_walk213 = 486
FRAME_walk214 = 487
FRAME_walk215 = 488
FRAME_walk216 = 489
FRAME_walk217 = 490

MODEL_SCALE = 1.000000


sound_pain4 = 0
sound_pain5 = 0
sound_pain6 = 0
sound_death = 0
sound_step_left = 0
sound_step_right = 0
sound_attack_bfg = 0
sound_brainsplorch = 0
sound_prerailgun = 0
sound_popup = 0
sound_taunt1 = 0
sound_taunt2 = 0
sound_taunt3 = 0
sound_hit = 0


@TODO
def makron_taunt():
    pass


@TODO
def makron_stand():
    pass


@TODO
def makron_hit():
    pass


@TODO
def makron_popup():
    pass


@TODO
def makron_step_left():
    pass


@TODO
def makron_step_right():
    pass


@TODO
def makron_brainsplorch():
    pass


@TODO
def makron_prerailgun():
    pass


@TODO
def makron_walk():
    pass


@TODO
def makron_run():
    pass


makron_frames_pain6 = [
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, makron_popup),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, makron_taunt),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None)
]

makron_move_pain6 = mmove_t(FRAME_pain601, FRAME_pain627, makron_frames_pain6, makron_run)

makron_frames_pain5 = [
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None)
]

makron_move_pain5 = mmove_t(FRAME_pain501, FRAME_pain504, makron_frames_pain5, makron_run)

makron_frames_pain4 = [
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None),
    mframe_t(ai_move, 0, None)
]

makron_move_pain4 = mmove_t(FRAME_pain401, FRAME_pain404, makron_frames_pain4, makron_run)


@TODO
def makronBFG():
    pass


@TODO
def MakronSaveloc():
    pass


def MakronRailgun(_self):
    start = [0, 0, 0]
    _dir = [0, 0, 0]
    forward = [0, 0, 0]
    right = [0, 0, 0]
    AngleVectors(_self.s.angles, forward, right, None)
    G_ProjectSource(_self.s.origin, monster_flash_offset[MZ2_MAKRON_RAILGUN_1], forward, right, start)
    _VectorSubtract(_self.pos1, start, _dir)
    VectorNormalize(_dir)
    monster_fire_railgun(_self, start, _dir, 50, 100, MZ2_MAKRON_RAILGUN_1)


@TODO
def MakronHyperblaster():
    pass


def makron_pain(_self, other, kick, damage):
    if _self.health < (_self.max_health/2):
        _self.skinnum = 1
    if level.time < _self.pain_debounce_time:
        return
    if damage <= 25 and random.uniform(0, 1) < 0.2:
        return
    _self.pain_debounce_time = level.time + 3
    if skill.value == 3:
        return

    if damage <= 40:
        gi.sound(_self, SOUND_CHANNELS.CHAN_VOICE, sound_pain4, 1, SOUND_ATTN_VALUES.ATTN_NONE, 0)
        _self.monsterinfo.currentmove = makron_move_pain4
    elif damaga <= 110:
        gi.sound(_self, SOUND_CHANNELS.CHAN_VOICE, sound_pain5, 1, SOUND_ATTN_VALUES.ATTN_NONE, 0)
        _self.monsterinfo.currentmove = makron_move_pain5
    else:
        if damage <= 150:
            gi.sound(_self, SOUND_CHANNELS.CHAN_VOICE, sound_pain6, 1, SOUND_ATTN_VALUES.ATTN_NONE, 0)
            _self.monsterinfo.currentmove = makron_move_pain6
        else:
            if random.uniform(0, 1) <= 0.35:
                gi.sound(_self, SOUND_CHANNELS.CHAN_VOICE, sound_pain6, 1, SOUND_ATTN_VALUES.ATTN_NONE, 0)
                _self.monsterinfo.currentmove = makron_move_pain6


@TODO
def makron_sight():
    pass


@TODO
def makron_attack():
    pass


@TODO
def makron_torso_think():
    pass


@TODO
def makron_torso():
    pass


@TODO
def makron_dead():
    pass


@TODO
def makron_die():
    pass


@TODO
def Makron_CheckAttack():
    pass


@TODO
def MakronPrecache():
    pass


@TODO
def SP_monster_makron():
    pass


@TODO
def MakronSpawn():
    pass


@TODO
def MakronToss():
    pass


from game.g_ai import ai_move
from .q_shared import AngleVectors, _VectorSubtract, VectorNormalize
from .g_utils import G_ProjectSource
from .g_monster import monster_fire_railgun
