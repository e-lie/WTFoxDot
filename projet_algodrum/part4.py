Clock.clear()

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 4, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor

#########################################################################

bpm_to(160, 32)
change_bpm(160, True, 0.22)

Clock.meter(4,4)

chords = var([0,5,2,3],[8,4,2,2])
Root.default = 0
Scale.default = Scale.minor


a1 >> apad(
    # [0, 4, -2],
    [0],
    dur=PRand(2, 8),
    sus=PRand(4, 12),
    vol=1.1,
    attack=.4,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
    vol=.7,
)
a1 + (0,12)
a1.oct=4
a1 + chords

b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=6)

b2.pause(4,16)
b2.stop()

b1 >> blip(chords, dur=PDur(5,8), sus=linvar([.3, 3], 16), oct=5, pan=0)
b1.pause(4,16,8)

b1.only()

k1.stop()

m1.fadeout(16)

m1.stop()

b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=6).pause(4,16) + P(0,2)
b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=4).pause(4,16,8) + P[0, 2, 0, P(0,2)]
b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=(4,6)).pause(4,16,8) + P[0, 2, 0, P(0,2)]

b2 + pitches

b1.oct = (3,4)

b2.stop()

b2 + [0,1,2,1]

d7 >> bbass(chords, dur=PDur(3,8), oct=(2,3), amp=1.5)
d7 >> subbass(0, root=chords, dur=PDur(3,8), oct=5, amp=1.5, vol=1, room2=3)
d8 >> bbass(0, root=chords, dur=PDur(3,8), oct=4, amp=1.5, vol=1, room2=3)
b2 >> padarp(0).fadein()
d7 >> bbass(0, dur=PDur(3,8), oct=(2,3), amp=1.5).pause(8,32)

d7 + P[0,0,2] + P[0,0,0,0,-1]

d7.amp = 2

d7.sampfadeout(64)

d7.only()

d7.crush = 16
d7.bits = 6

b2.stop()

k2 >> play("V.", dur=.5, amp=1, crush=8, bits=4, lpf=linvar([200,1000],32), output=12) #Ah le kick enfin
k1 >> kicker("<v.>", dur=.5, amp=1, rate=1, output=12)
h2 >> play(".--(-*-[**])", sdb=1, sample=0, hpf=2000, dur=1/4, leg=10, pan=P[-1,0,1].stutter(3), amp=linvar([.8,1.6],16))

h2.pause(2,7)

e3 >> play(
    "*",
    dur=.25,
    sample=P[0, 1, 2].stutter(4),
    rate=PWhite(1.2, 1.5),
    amp=1,
    pan=P[-1, 0, .5, 0, 1, 0].stutter(4)
)
e3.pause(4,16,12)

d1 >> play("=.*.", sdb=1, sample=3, hpf=3000, triode=1, crush=1, pan=.4)

k2 >> kicker(
    "<(VVV(V[.V]V[VV]))(...V)>",
    # "<V...>",
    # "<V(x.)(.x).>",
    # "<V(x.)(.x)X>",
    dur=.5,
    amp=1,
    crush=8,
    bits=linvar([6, 2], 24, start=Clock.mod(4)),
    output=12,
)

k2.stop()

k1.fadeout()
k2.fadeout()

k1.stop()
k2.stop()

k3 >> play(
    '<X.><v.>',
    dur=1 / 2,
    sdb=1,
    sample=1,
    amp=2,
    output=12,
    lpf=300
)

k_all.only()

k3.stop()

k3.degree = Pvar(["<.X><.v>", '.', '<X.><v.>', '.'], [44, 4]),

k3.sample = var([1,4,0],48)
k3.room2 = linvar([0,1], 16, start=Clock.mod(4))
m2.room2 = linvar([0,1], 16, start=Clock.mod(4))

b_all.fadeout(16)

Root.default = 0

pitches = [0,2,2,1,-2,0,0,1]

b9 >> bass303(chords, dur=PDur(3,8), sus=b1.dur-0.1)
b9.cutoff=0
b9.reso=0
b9.decay=1
b9.env_mod=0

b9.cutoff=.5
b9.reso=.5
b9.decay=.6
b9.oct=5

b9.only()


b9.stop()


b9.cutoff=linvar([0,1,.5],32, start=Clock.mod(4))
b9.reso=linvar([0,1,.5],24, start=Clock.mod(4))
b9.decay=linvar([0,.6,.4,.7,0,.6],PRand(2,24), start=Clock.mod(4))

bs.cutoff=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
bs.reso=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
bs.decay=linvar([0,.6,.4,.7,0,.6],PRand(2,24), start=Clock.mod(4))

bs.pause(8,48,40)

b1.stop()

pitches = [0,2,4,5,0,2,4]

k4 >> play(".VxV", lpf=200, sample=4, amp=1, sdb=1, dur=1/4, room2=10, output=12, cut=.9).fadein(16)

k4.only()

k4.fadeout()

b3 >> vibra(chords, dur=[.5,.5], sus=b1.dur-.04, amp=1, vol=1)

b3 >> blip(chords, dur=.25, sus=1, amp=1.5, oct=[4,5,6,5,6,7])

b3 >> blip

# d3 >> play("<.c.c.c.cc><...(...*)><..(~).>", dur=1/4, rate=var([1,1.3]), sample=var([1,2], 8), amp=2)

a4.stop()

m3.stop()

b3 + pitches

k4.fadeout(32)

k4.stop()

k3.fadeout(16)

d3 >> play("<(-~)[~-]>", dur=.5, amplify=pa16_2, amp=2)

k1 >> play(
    "<V><x>",
    dur=clave23,
    sample=P[0, 1, 2].stutter(5),
    amplify=pa32,
    amp=1,
    output=12
)

k3.stop()

b2 >> bbass(chords, dur=cascara, oct=3, amp=2) + P(0,2)

b2.fadeout()

Root.default = 0

b2.stop()

b2 + [0,1,0,0,2]

b2.fadeout()

b2.stop()

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)

e3.stop()

k3.stop()

k_all.stop()

k4 >> kicker(
    "<V....V..>",
    dur=.5,
    sample=var([0, 1, 2], 32),
    rate=linvar([.8, 1.2], 16),
    amp=1,
    output=12
)

d6 >> play("<..*...*.>", dur=.5, sample=1, rate=(.8,1.2,1.6), amp=1.5)

k4.stop()

d8 >> play("/", dur=16, pan=[-1, 0, -1], amp=1.5)

Clock.bpm = linvar([120, 160], PRand(8,32))

Clock.bpm = 160

print(SynthDefs)
