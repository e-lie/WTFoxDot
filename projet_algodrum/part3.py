
Clock.clear()

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 4, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor

Clock.meter = (4,4)

bpm_to(130,24)
change_bpm(130, True, 0.22)

d1 >> play(
    ".c",
    dur=.5,
    amp=1*PWhite(.8,1.2),
    rate=1.7,
    cut=2,
    room2=.3,
    crush=0,
    bits=5,
    pan=0
)

d1.pause(16,32,8)

d1.pause(8,32,16)
d1.degree = "(.c)c"
d1.degree = "(.*)(cc[**]=)"
d1.degree = "(***~..[**~][~*][*~]..cccccc)"
d1.crush = 16
d1.bits = 3
d1.dur=PDur(3,8)
d1.dur = var([.5, .25], [7,4])
d1.rate = PWhite(1,3)

################################################

Scale.default = Pvar([Scale.minor, Scale.major], 16)

p1 >> dakeys(
    [0, 2, 5, 2, -2, 1, 4],
    # [0, 2, 4, 2, -2, P4],
    dur=.5,
    oct=(3,5,7),
    # oct=6,
    amp=.8,
    # pad=0,
    # modelb=0,
    # pluck=1,
    # space=.4,
    vol=1.5,
    # vol=1.0,
).fadein(16)

s2.fadeout(64)

p1.oct=(3,5,7)

p1.pad = linvar([0, .5], 12) 
p1.modelb = linvar([0,1],32)
p1.pluck = linvar([0,1],24)
p1.space = linvar([0,1],32)

p1.fadeout(64)

p1.sampfadeout(32)

p1.only()

p1.stop()

p1.stop()

a2 >> padarp(
    [0, 2,0,5],
    # dur=[1.1,.9],
    dur=.5,
    oct=4,
    amp=1.5,
    vol=1.5,
)
a2.fadein()

a2.fadeout(64)

s2.stop()

k1.stop()