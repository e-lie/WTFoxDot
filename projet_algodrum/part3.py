Clock.clear()

Root.default = 0
Root.default = var([0,1,2], PRand([1,8]))
Root.default = var(PTri(12), 4, start=Clock.mod(4))
Root.default = var(PTri(12), 7, start=Clock.mod(7))
Root.default = var(PTri(12), .25)

Scale.default = Scale.minor
Scale.default = Scale.majorPentatonic
Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)

#############################################################

Clock.meter = (4,4)
Scale.default = Scale.minor

bpm_to(130,24)

Root.default = 0

def shift_clock(time, shift, factor=16):
    time *= factor
    shift *= factor
    return max(time-shift,0)
cshift = 0
mmelody = P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5]

@nextBar(shift_clock(0, cshift))
def a():
    pass
@nextBar(shift_clock(1, cshift))
def a():
    pass
@nextBar(shift_clock(2, cshift))
def a():
    m1 + (0,2)
    pass
@nextBar(shift_clock(3, cshift))
def a():
    pass
@nextBar(shift_clock(4, cshift))
def a():
    pass
@nextBar(shift_clock(5, cshift))
def a():
    pass
@nextBar(shift_clock(6, cshift))
def a():
    pass
@nextBar(shift_clock(7, cshift))
def a():
    pass
@nextBar(shift_clock(8, cshift))
def a():
    pass
@nextBar(shift_clock(9, cshift))
def a():
    pass
@nextBar(shift_clock(10, cshift))
def a():
    pass
@nextBar(shift_clock(11, cshift))
def a():
    pass
@nextBar(shift_clock(12, cshift))
def a():
    pass
@nextBar(shift_clock(13, cshift))
def a():
    pass
@nextBar(shift_clock(14, cshift))
def a():
    pass
@nextBar(shift_clock(15, cshift))
def a():
    pass
@nextBar(shift_clock(16, cshift))
def a():
    pass
@nextBar(shift_clock(17, cshift))
def a():
    pass
@nextBar(shift_clock(18, cshift))
def a():
    pass
@nextBar(shift_clock(19, cshift))
def a():
    pass
@nextBar(shift_clock(20, cshift))
def a():
    pass
@nextBar(shift_clock(21, cshift))
def a():
    pass
@nextBar(shift_clock(22, cshift))
def a():
    pass
@nextBar(shift_clock(23, cshift))
def a():
    pass
@nextBar(shift_clock(24, cshift))
def a():
    pass
@nextBar(shift_clock(25, cshift))
def a():
    pass
@nextBar(shift_clock(26, cshift))
def a():
    pass
@nextBar(shift_clock(28, cshift))
def a():
    pass
@nextBar(shift_clock(29, cshift))
def a():
    pass
@nextBar(shift_clock(30, cshift))
def a():
    pass
@nextBar(shift_clock(31, cshift))
def a():
    pass
@nextBar(shift_clock(32, cshift))
def a():
    pass
@nextBar(shift_clock(33, cshift))
def a():
    pass
@nextBar(shift_clock(34, cshift))
def a():
    pass
@nextBar(shift_clock(35, cshift))
def a():
    pass
@nextBar(shift_clock(36, cshift))
def a():
    pass
@nextBar(shift_clock(37, cshift))
def a():
    pass
@nextBar(shift_clock(38, cshift))
def a():
    pass
@nextBar(shift_clock(39, cshift))
def a():
    pass
@nextBar(shift_clock(40, cshift))
def a():
    pass
@nextBar(shift_clock(41, cshift))
def a():
    pass
@nextBar(shift_clock(42, cshift))
def a():
    pass
@nextBar(shift_clock(43, cshift))
def a():
    pass
@nextBar(shift_clock(44, cshift))
def a():
    pass
@nextBar(shift_clock(45, cshift))
def a():
    pass
@nextBar(shift_clock(46, cshift))
def a():
    pass
@nextBar(shift_clock(47, cshift))
def a():
    pass
@nextBar(shift_clock(48, cshift))
def a():
    pass
@nextBar(shift_clock(49, cshift))
def a():
    pass
@nextBar(shift_clock(50, cshift))
def a():
    pass
@nextBar(shift_clock(51, cshift))
def a():
    pass

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

d1.only()

d1.degree = "(.c)c"
d1.degree = "V~"
d1.sample = 2
d1.rate=1
d1.degree = "(.*)(cc[**]=)"
d1.degree = "(***~..[**~][~*][*~]..cccccc)"
d1.crush = PXhite(4,16)
d1.bits = 4
d1.dur=PDur(3,8)
d1.dur=1

d1.dur = var([.5, .25], [7,4])
d1.rate = PWhite(1,3)

################################################

Scale.default = Pvar([Scale.minor, Scale.major], 16)

p1 >> dakeys(
    # chords+P[0, 2, 5, 2, -2, 1, 4],
    P[0, 2, 5, 2, -2, 1, 4],
    # [0, 2, 4, 2, -2, 4],
    dur=.5,
    oct=(3,5,7),
    # oct=6,
    amp=.8,
    pad=0,
    modelb=0,
    pluck=1,
    space=.4,
    vol=1.5,
    # vol=1.0,
)
# p1.fadein(64)

p1.pad = linvar([0, .5], 12) 
p1.modelb = linvar([0,1],32)
p1.pluck = linvar([0,1],24)
p1.space = linvar([0,1],32)



k1 >> play(
    # degree="V...",
    degree = "<V.x.>",
    # degree = "<V.x.><..[(...X)X]>",
    # degree = "<V.x.><.(..[XV])[(...X)X]>",
    # degree = "<V.x.><.(..[XV])[(...X)X]>",
    # degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],[32,16], start=Clock.mod(4)),
    pdb=2,
    output=12,
    sample=2,
    # room2=3,
    room2=.1,
    lpf=800,
    amp=.8,
    # cut=.5,
)
k1.fadein(24)

a2 >> padarp(
    [0, 2,0,5],
    # dur=[1.1,.9],
    dur=.5,
    oct=3,
    amp=1,
    vol=1,
    # expand=0,
    expand=linvar([0,1], [32,inf], start=Clock.mod(4)),
    # verb=0,
    verb=linvar([0,1], [32,inf], start=Clock.mod(4)),
    detune=1,
    delay=0,
)
# a2.fadein()


s1 >> pharao(
    [0],
    # mmelody,
    dur=[.5, .25, .25],
    oct=5,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    sus=s1.dur + 0.2,
    # cutoff=.06,
    cutoff=linvar([.1,.5], [15*.25*15,inf], start=Clock.mod(15*.25)),
) + P(0, 2)

s1.sampfadeout(16)