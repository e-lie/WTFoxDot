Clock.clear()

p1 >> gone(
    [0,5],
    dur=4,
    oct=[3,5,6,4],
    amp=.8,
    dull=linvar([0, 1], PRand(1, 8)),
    body=var([0,1,.2,.7],8),
    pitch=0,
    arp=linvar([0, 1], PRand(8, 32)),
).fadeout(32)

Root.default = var(PRand([2,4,5])[:16], 16)

d1 >> play(
    "/+i[++]",
    dur=P[.5, .5, .25, .5, .25, .5, .25, .5, .5, .25],
    rate=PWhite(.5, 2),
    sample = 4
)

a1 >> apad(
    [0, 2, 5, 2, -2, 1, 4],
    dur=4,
    oct=5,
    amp=.8,
    attack=.8,
    space=.5,
    thick_thin=0,
    detail=0,
)

k1 >> play(
    "v.x(c[.c])", output=12,
    rate = PWhite(.1,3),
    dur=P[.5, .5, .25, .5, .25, .5, .25, .5, .5, .25]
).fadein(8)

bpm_to(100)
change_bpm(100, True, 0.22)

Scale.default = Scale.majorPentatonic

p1.sfadeout(64)
p1.oct=P*(3,4,5)
p1.dur=.5
p1.fadeout(16)

p1 >> dakeys(
    [0, 2, 5, 2, -2, 1, 4],
    dur=var([.5, .25], [24,8]),
    oct=(4,6),
    amp=.8,
    pad=0,
    modelb=linvar([0, 1], 32),
    pluck=linvar([0,.5,0,1,.5], PRand(1,16)),
    space=.4,
)
