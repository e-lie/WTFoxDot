Clock.clear()

from FoxDot import *
from FoxDot.preset import *

fordrip, gone = add_chains("noise/fordrip_1", "pads/gone_1")
apad, souls = add_chains("pads/apad_1", "pads/souls_1")
marimba, vibra = add_chains("mallets/marimba_1", "mallets/vibra_1")
lavitar, pharao, sahara = add_chains("synth_keys/lavitar_1", "synth_keys/pharao_1","synth_keys/sahara_1")
dakeys, padarp, bass303 = add_chains("synth_keys/dakeys_1", "synth_keys/padarp_1", "bass/bass303_1")
# darkpass, hpluck, acidbb = add_chains("darkpass", "hpluck1")
# rdrum, bpiano = add_chains("drum/rdrum_1", "synth_keys/bpiano_1")

def shift_clock(time, shift, factor=16):
    time *= factor
    shift *= factor
    return max(time-shift,0)
cshift = 0

Clock.latency = .5
Clock.midi_nudge = -.235

################################################################

Clock.bpm=110
cc >> play("t", dur=1, rate=[1], pan=0, amp=[8], output=14)
cc.always_on = True

Root.default = 0
Scale.default = Scale.major

######################################

@nextBar(shift_clock(0, cshift))
def a():
    Clock.bpm=110
    Root.default = 0
    Scale.default = Scale.major
    s1 >> pharao(
        [0],
        # pitches,
        # chords2,
        dur=1,
        # dur=[1,.5],
        # dur=.5,
        # dur=[.5, .25, .25],
        oct=4,
        amp=P[.8, .7, .8, 1.1] * 1.5,
        # sus=s1.dur + 0.2,
        # room2=3,
        cutoff = .1,
        # cutoff=linvar([.1,.5],16, start=Clock.mod(4)),
    )
    s1.fadein(16)
@nextBar(shift_clock(1, cshift))
def a():
    a1 >> apad(
        P[0, 4, -2],
        dur=PRand(2, 8)[:16],
        # dur=4,
        vol=1,
        attack=.5,
        space=0,
        detail=0,
        thick_thin=0,
        oct=5,
    )
    a1.fadein(16)
@nextBar(shift_clock(2, cshift))
def a():
    a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
    a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
    a1.detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
@nextBar(shift_clock(3, cshift))
def a():
    a1.degree = P[0,4,-2] + P(0,4,5)
@nextBar(shift_clock(5, cshift))
def a():
    a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=5, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
    a4.fadein(32)
@nextBar(shift_clock(6, cshift))
def a():
    a1.fadeout(16, ivol=1, fvol=.8)
@nextBar(shift_clock(7, cshift))
def a():
    a4.oct = 3
@nextBar(shift_clock(8, cshift))
def a():
    a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
@nextBar(shift_clock(9, cshift))
def a():
    a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
    a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
@nextBar(shift_clock(10, cshift))
def a():
    a4.fadeout(32, ivol=1, fvol=.8)
@nextBar(shift_clock(11, cshift))
def a():
    a1.oct=Pvar([5,(4,5),P*(4,6)], 16)
    a1.degree = Pvar([P[0, 4, -2], P[0, 4, -2]+P(0,4,5)], 16)
@nextBar(shift_clock(12, cshift))
def a():
    s1.dur = .5
    s1 + P(0,5)
@nextBar(shift_clock(13, cshift))
def a():
    pitches = [0, 2, 5, 2, 0, -2, 5, 4]
    s1.degree = pitches
    s1.dur = [.5,.25,.25] 
@nextBar(shift_clock(14, cshift))
def a():
    pass
@nextBar(shift_clock(14, cshift))
def a():
    k1 >> play(
        degree="V...",
        # degree = "<V.x.>",
        # degree = "<V.x.><..[(...X)X]>",
        # degree = "<V.x.><.(..[XV])[(...X)X]>",
        # degree = "<V.x.><.(..[XV])[(...X)X]>",
        # degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4)),
        pdb=2,
        output=12,
        sample=4,
        # room2=3,
        room2=.1,
        lpf=700,
        amp=.7,
        # cut=.5,
    )
    k1.fadein(24)
@nextBar(shift_clock(15, cshift))
def a():
    k1.lpf = linvar([300,800], [32,inf], start=Clock.mod(4))
    k1.degree = "<V.x.>"
@nextBar(shift_clock(16, cshift))
def a():
    k1.degree = "<V.x.><..[(...X)X]>"
@nextBar(shift_clock(17, cshift))
def a():
    k1.degree = "<V.x.><.(..[XV])[(...X)X]>"
@nextBar(shift_clock(18, cshift))
def a():
    pass
@nextBar(shift_clock(19, cshift))
def a():
    s1.cutoff=linvar([.1,.5],16, start=Clock.mod(4))
    s1.oct=(5,6)
    s1.level=.8
@nextBar(shift_clock(20, cshift))
def a():
    a4.pitch = 0
    a4.arp = 0
@nextBar(shift_clock(21, cshift))
def a():
    Scale.default = Scale.minor
@nextBar(shift_clock(22, cshift))
def a():
    a4.fadeout(16)
    s1 + (0,2)
@nextBar(shift_clock(23, cshift))
def a():
    k1.degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4))
    k1.pause(8,48)
@nextBar(shift_clock(24, cshift))
def a():
    s2 >> blip(
        [0],
        dur=P[.5, .25, .25],
        amp=P[.8, .7, .8, 1.1] * 2,
        pan=[-1,0,1,0],
        # oct=[5, 7, 6],
        oct=[5, 7, 6, 7],
        sus=linvar([.3, 2], [48], start=Clock.mod(4)),
    )
    s2.fadein(16, fvol=1)
@nextBar(shift_clock(25, cshift))
def a():
    s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]
@nextBar(shift_clock(26, cshift))
def a():
    s1.oct=Pvar([(4,5), 3, (3,4,5)], [2,4,3,3])
@nextBar(shift_clock(27, cshift))
def a():
    s2.dur = var([.25, .5, 1/3], [10,4,2])
@nextBar(shift_clock(28, cshift))
def a():
    a1.fadeout()
@nextBar(shift_clock(29, cshift))
def a():
    k1.degree = "<V.x.>"
@nextBar(shift_clock(30, cshift))
def a():
    Scale.default = Scale.major
@nextBar(shift_clock(31, cshift))
def a():
    Root.default = var(PTri(12), 8, start=Clock.mod(4))
@nextBar(shift_clock(32, cshift))
def a():
    degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4)),
@nextBar(shift_clock(33, cshift))
def a():
    Root.default = var(PTri(12), .25)
@nextBar(shift_clock(34, cshift))
def a():
    s2.degree = pitches
    Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
@nextBar(shift_clock(35, cshift))
def a():
    Root.default = 0
@nextBar(shift_clock(36, cshift))
def a():
    thegroup = Group(k1,s1)
    thegroup.solo()
    s2.stop()
@nextBar(shift_clock(36.5, cshift))
def a():
    thegroup = Group(k1,s1)
    thegroup.solo(0)
@nextBar(shift_clock(38, cshift))
def a():
    pass
@nextBar(shift_clock(39, cshift))
def a():
    a4.fadein(32)
@nextBar(shift_clock(40, cshift))
def a():
    a1.fadein(32)
    k1.fadeout(16)
    s1 >> space(
        pitches,
        # chords2,
        # dur=[1,.5],
        # dur=.5,
        dur=[.5, .25, .25],
        amp=P[.8, .7, .8, 1.1] * 1.5,
        # sus=s1.dur + 0.2,
        room2=.5,
        oct=Pvar([(4,5), 3, (3,4,5)], [2,4,3,3]),
    )
@nextBar(shift_clock(41, cshift))
def a():
    pass
@nextBar(shift_clock(42, cshift))
def a():
    s2 >> blip(
        [0,2],
        dur=P[.5, .25, .25],
        amp=P[.8, .7, .8, 1.1] * 2,
        pan=[-1,0,1,0],
        # oct=[5, 7, 6],
        oct=[5, 7, 6, 7],
        sus=linvar([.3, 2], [48], start=Clock.mod(4)),
    )
    s2.fadein(16, fvol=1)
@nextBar(shift_clock(43, cshift))
def a():
    s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]
@nextBar(shift_clock(44, cshift))
def a():
    p2 >> padarp(
        [0, 2],
        dur=[1,.5],
        oct=3,
        amp=.8,
        verb=0,
        delay=0,
        # detune=sinvar([0,1], PWhite(.2,3)[:16]),
        detune=0,
        expand=0,
        vol=1.2,
    )
    p2.verb=linvar([0,1], [32,inf], start=Clock.mod(4))
    p2.delay=linvar([0,1], [64,inf], start=Clock.mod(4)),
    p2.expand=linvar([0, 1], 16),
@nextBar(shift_clock(45, cshift))
def a():
    k1 >> play(
        "X{.xXx}(X.)",
        output=12,
        sample=0,
        pdb=0,
        amp=1.5,
        # dur=.5,
        dur=Pvar([PDur(3, 8), .25, .5, PDur(5, 8)], PRand(2, 8)),
    )
    k1.fadein()
    k1.rate = PWhite(.8,1.6)
@nextBar(shift_clock(46, cshift))
def a():
    k1.pause(8,32)
    k1.lpf=4000
    k1.crush = PWhite(0,8)
    k1.bits = PWhite(3,8)
@nextBar(shift_clock(47, cshift))
def a():
    Root.default = var(PTri(12), 8, start=Clock.mod(4))
@nextBar(shift_clock(48, cshift))
def a():
    pass
@nextBar(shift_clock(49, cshift))
def a():
    Root.default = var(PTri(12), .25, start=Clock.mod(4))
@nextBar(shift_clock(37, cshift))
def a():
    Scale.default = Scale.minor
    Root.default = 0
    bpm_to(100, 128)
@nextBar(shift_clock(50, cshift))
def a():
    pass
@nextBar(shift_clock(52, cshift))
def a():
    a4.sampfadeout(24)






@nextBar(shift_clock(37, cshift))
def a():
    pass
@nextBar(shift_clock(37, cshift))
def a():
    pass
@nextBar(shift_clock(37, cshift))
def a():
    pass
@nextBar(shift_clock(37, cshift))
def a():
    pass
@nextBar(shift_clock(37, cshift))
def a():
    pass
@nextBar(shift_clock(37, cshift))
def a():
    pass








a1.fadeout(16, ivol=1, fvol=.8)



a4.sampfadeout(32)

a4.only()


a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.pitch = .5

a4.vol=.8
a1.vol=.8

pitches = [0, 2, 5, 2, 0, -2, 5, 4]

s1 >> pharao(
    # [0],
    pitches,
    # chords2,
    # dur=1,
    # dur=[1,.5],
    # dur=.5,
    dur=[.5, .25, .25],
    oct=4,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    sus=s1.dur + 0.2,
    room2=3,
    # cutoff = .1,
    cutoff=linvar([.1,.5],16, start=Clock.mod(4)),
)
# s1.fadein(16)
s1 + P(0, 5)

# pharao

s1.sampfadeout(16)

s2.fadeout(24)

Root.default = var([0,2,-2], 16, start=Clock.mod(4))

################################################


s1.oct=[3,4,5,4]
s1.oct=Pvar([(4,5), 3, (3,4,5)], [2,4,3,3])

s1 + (0,2)

s1.fadeout(32)

s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]

s1.pause(8,32)

s1.dur=PDur(5,8)

s1 + P[0,1,0,0,2,-2]

a1.stop()

a1.fadeout(32)

###################################################



s2.degree = pitches


s_all.ampfadeout(64)

s2.dur = var([.25, .5, 1/3], [10,4,2])

s2.degree = [0,2,0,4,1,5,0,5,3]
s2.degree = var(pitches,.5)

s2.oct=P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3]+1

s2.oct=(5,7)

s2.oct=Pvar([P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3], [3,4,5,6], P(3,4,5,6)], 8)

s2.pause(8,32, 16)

s2.amp=2

s2.fadeout(16)

#################################################

k1 >> play(
    # degree="V...",
    # degree = "<V.x.>",
    # degree = "<V.x.><..[(...X)X]>",
    # degree = "<V.x.><.(..[XV])[(...X)X]>",
    # degree = "<V.x.><.(..[XV])[(...X)X]>",
    degree = Pvar(["V.x.","<V.x.><.(..[XV])[(...X)X]>"],16, start=Clock.mod(4)),
    pdb=2,
    output=12,
    sample=4,
    # room2=3,
    room2=.1,
    lpf=700,
    amp=.7,
    # cut=.5,
)
# k1.fadein(24)

k1.pause(8,64)
k1.amplify=linvar([1,1,0,0],[40,16,8,0], start=Clock.mod(4))


##################################################

s1.fadeout(32)

p2 >> padarp(
    [0, 2],
    dur=[1,.5],
    oct=3,
    amp=.8,
    verb=0,
    delay=0,
    # detune=sinvar([0,1], PWhite(.2,3)[:16]),
    detune=0,
    expand=0,
    vol=1.2,
)

p2.verb=linvar([0,1], [32,inf], start=Clock.mod(4))
p2.delay=linvar([0,1], [64,inf], start=Clock.mod(4)),
p2.expand=linvar([0, 1], 16),

############################################################

k1 >> play(
    "X{.xXx}(X.)",
    output=12,
    sample=0,
    pdb=0,
    amp=1.5,
    # dur=.5,
    dur=Pvar([PDur(3, 8), .25, .5, PDur(5, 8)], PRand(2, 8)),
)
k1.fadein()

k1.pause(8,32)
k1.rate = PWhite(.8,1.6)
k1.dur = Pvar([PDur(3,8), .25, .5, PDur(5,8)], PRand(2,8))

k1.lpf=4000
k1.crush = PWhite(0,8)
k1.bits = PWhite(3,8)

############################################################

h2 >> play(".--(-*-[**])", sdb=1, sample=0, hpf=2000, dur=1/4, leg=10, pan=P[-1,0,1].stutter(3), amp=2)
h2.pause(12,32,8)

h2.stop()

############################################################

a4.sampfadeout(64)
a1.sampfadeout(64)

a1.only()

a4.only()

a1.stop()

a4.fadeout()

bpm_to(100, 128)

cc >> play("t", dur=1, rate=[1], pan=0, amp=[2], output=14)