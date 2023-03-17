Clock.clear()

from FoxDot import *
from FoxDot.preset import *

fordrip, gone = add_chains("fordrip1", "gone1")
apad, souls = add_chains("apad1", "souls1")
marimba, vibra = add_chains("marimba1", "vibra1")
darkpass, hpluck = add_chains("darkpass", "hpluck1")
dakeys, padarp = add_chains("dakeys1", "padarp1")
# rdrum, bpiano = add_chains("rdrum1", "bpiano")
acidbb, bass303 = add_chains("acidbb", "bass303")

Root.default = var([0,1,2], PRand([1,8]))
Root.default = var([0,2,-2], 8)

Root.default = 0
Root.default = var(PTri(12), 8, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor
Scale.default = Scale.major
Scale.default = Scale.majorPentatonic

cc >> play("t", dur=1, rate=[1], pan=0, amp=[6], output=14)

change_bpm(110, True, 0.24)

bpm_to(130,48)

######################################

a1 >> apad(
    [0, 4, -2],
    # [0],
    dur=PRand(2, 8),
    # dur=4,
    # sus=8,
    vol=1.1,
    # attack=1,
    # space=0,
    # detail=0,
    thick_thin=0,
    oct=5,
)
a1.fadein(16)

a1.stop()

a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
a1.detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a1 + (0,12)
a1 + (0,4,5)

a1.oct=Pvar([5,(4,5),P*(4,6)])

a1.sampfadeout(32)
a1.only()

#########################################

a4 >> gone([0], dur=4, dull=0, body=0, arp=0, pitch=0)
a4.fadein(32)

a4.stop()
a4.oct = 3
a4.oct = (3,6)

a4.sampfadeout(32)

a4.only()

a4.dull = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.pitch = .5
a4.vol=.8
a1.vol=.8

################################################

s1 >> space([0], dur=[.5,.25,.25], oct=5, amp=P[.8,.7,.8,1.1]*1.5, sus=s1.dur+0.2, output=12) # + P(0,2)
s1 >> bbass([0], dur=[.5,.25,.25], oct=5, amp=P[.8,.7,.8,1.1]*1.5, sus=s1.dur+0.2, output=12) # + P(0,2)
s1.oct=Pvar([(4,5), 3, (3,4,5)], [2,4,3,3])
s1.oct=[4,5]

s1 + (0,2)

s1.fadeout(32)

a4.fadedout(dur=16,fvol=.5)
a1.fadedout(dur=16,fvol=.5)
a1.fadeout(32)

s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]

s1.oct=P(5,3)
s1.pause(8,32)

s1.dur=PDur(5,8)

s1 + P[0,1,0,0,2,-2]

###################################################

s2 >> blip(
    [0],
    dur=P[.5, .25, .25],
    sus=linvar([0, 2], [16, 32, 64]),
    oct=[5, 8, 6],
    amp=P[.8, .7, .8, 1.1] * 2,
    pan=[-1,0,1,0]
)

s1.stop()

s1.sampfadeout(32)

s1.only()

s2.dur = var([.25,.5,2/5],4)
s2.dur = var([.25, .5, 1/3], [10,4,2])

s2.degree = [0,2,0,4,1,5,0,5,3]
s2.degree = PWalk()
s2.mpan(0)
s2.sus=2
s2.sus=linvar([.2,1.5], PRand(4,16))

s2.oct=P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3]

s2.oct=Pvar([P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3], [3,4,5,6], P(3,4,5,6)], 8)
s2.pause(8,32, 16)

s2.amp=2

s2.dur=PDur(3,7)/2

s2.fadeout(16)

#################################################

k1 >> play("V...", pdb=2, output=12, sample=4)

k1.degree = "<V.x.>"
k1.degree = "<V.x.><..[(...X)X]>"
k1.degree = "<V.x.><.(..[XV])[(...X)X]>"

k1.stop()

k1.pause(8,24)

k1.dur=.5
k1.pause(0,16)

k1.sample=1

s1.fadeout()

s2.sampfadeout(32)

s2.only()

##################################################

p2 >> padarp(
    [0, 2],
    dur=[1,.5],
    oct=3,
    amp=.8,
    verb=0,
    delay=0,
    detune=sinvar([0,1], PWhite(.2,3)[:16]),
    expand=0,
    vol=1.2,
).span(.5)

p2.vol=1.2

p2.verb=linvar([0,1], [32,inf], start=Clock.mod(4))
p2.delay=linvar([0,1], [64,inf], start=Clock.mod(4)),
p2.expand=linvar([0, 1], 16),

############################################################

k1 >> play("X{.xX+}(X.)", dur=PDur(3,8), output=12, sample=0, pdb=0, amp=1.5)
k1.fadein()

k1.pause(8,32)
k1.rate = PWhite(.8,1.6)
k1.dur = Pvar([PDur(3,8), .25, .5, PDur(5,8)], PRand(2,8))

k1.crush = PWhite(0,8)
k1.bits = PWhite(3,8)

############################################################

h2 >> play(".--(-*-[**])", sdb=1, sample=0, hpf=2000, dur=1/4, leg=10, pan=P[-1,0,1].stutter(3), amp=2)
h2.pause(12,32,8)

h2.stop()

############################################################

a4.sampfadeout(64)

a4.only()

k1.stop()

a4.fadeout()