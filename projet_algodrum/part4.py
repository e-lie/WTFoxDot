Clock.clear()

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 4, start=Clock.mod(4))
Root.default = var(PTri(12), 16, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor

#########################################################################

k_all.stop()

Clock.bpm = 140

bpm_to(140, 32)
change_bpm(120, True, -0.235)

Clock.meter(4,4)

Root.default = 0
Scale.default = Scale.major

chords = var([0,5,2,3],[8,4,2,2])
chords2 = var([0,2,5,4],[8,4,2,2])
chords3 = var([2,0,3,4],[8,4,2,2])

d6 >> play("<..*...*.>", dur=.5, sample=1, rate=(.8,1.2,1.6), amp=1.5)

d8 >> play("/", dur=16, pan=[-1, 0, -1], amp=1.5)

k3.sampfadeout()

bb >> bbass(
    chords,
    # chords2,
    # chords3,
    dur=PDur(3, 8),
    # dur=cascara,
    # oct=(2,3,4),
    oct=(2,3,4),
    amp=1.5,
    room2=0,
    sus=linvar([.5,2], 32),
    pan=var([-.5, 0, .5], 4)
)#.pause(8, 32)


bb.only()


k1 >> kicker(
    "<V....V..>",
    dur=.5,
    # sample=var([0, 1, 2], 32),
    sample=2,
    # rate=linvar([.8, 1.2], 16),
    lpf=500,
    rate=1,
    amp=1.2,
    output=12
).stop()

l_all.degree = chords2
a_all.degree = chords2
b_all.degree = chords2

l1 >> blip(
    # chords,
    # chords2 + P(0,2),
    # chords2 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2),
    # chords2,
    chords3,
    # dur=clave23,
    # dur=.25,
    dur=PDur(5,8),
    # dur=Pvar([.5, .25, 1/3, PDur(5,8)], 8),
    sus=linvar([.4, 6], 16),
    oct=6,
    # room2=3,
    # pan=[-1, 0, 0, 1, 1, 0],
    pan=var([-1, 0, 1, 0])
).pause(4, 16)

y5 >> pharao(
    # chords,
    chords3 + P[0, 2, 0, P(0, 2)],
    # chords2,
    # chords3,
    # dur=cascara,
    dur=PDur(3,8),
    sus=linvar([.3, 3], 16),
    oct=(4,6),
    # oct=4,
    cutoff=.1,
    room2=1,
    pan=[-1, 0, 1],
).pause(4, 16, 8)

a1 >> apad(
    chords3,
    # chords + P(0,12),
    dur=PRand(2, 8),
    sus=PRand(4, 12),
    attack=.4,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
    # vol=.7,
    vol=1.1,
)
a1.fadein()

##### PART CCCC
br >> space(chords3, oct=(3,4,6,7), amp=3, dur=[.25,.25,.5])

bb >> bass303(
    chords3,
    dur=PDur(3, 8),
    # dur=cascara,
    sus=bb.dur-.1,
    oct=4,
    amp=2,
    room2=0,
    pan=[-1, 0, 1],
    # cutoff=0,
    cutoff=linvar([0,1],32),
    reso=linvar([0,1],24),
    decay=linvar([0,1],48),
)
bb.fadein()

k1 >> kicker("<v.>", dur=.5, amp=1, rate=1, output=12)

k2 >> play(
    # "V.",
    "(VVV[VV]).",
    dur=.5,
    amp=1,
    # crush=8,
    # bits=4,
    lpf=linvar([200, 1000], 32),
    output=12,
    rate=1,
    # rate=(1,6),
).fadein()

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

l_all.stop()

k2.stop()

bb.stop()

k1.fadeout()
k2.fadeout()

k1.stop()
k2.stop()

##### PART CCCC
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



##### PART CCCC
s1 >> pharao(
    [0],
    dur=[.5, .25, .25],
    oct=5,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    sus=s1.dur + 0.2,
    output=12,
    # cutoff=.06,
    # cutoff=linvar([.06,.5], [15*.25*15,inf], start=Clock.mod(15*.25)),
    cutoff=linvar([.06,.5], [15*.25*15], start=Clock.mod(15*.25)),
) + P(0, 2)


##### PART CCCC
n1 >> padarp(
    # chords,
    chords3 + P(0,2),
    # chords2 + P[0,2,0,-2,0,3,0,5,4,0] + P(0,2),
    # chords2,
    # chords3,
    # dur=clave23,
    # dur=.25,
    dur=PDur(5,8),
    # dur=Pvar([.5, .25, 1/3, PDur(5,8)], 8),
    sus=linvar([.4, 6], 16),
    oct=6,
    # room2=3,
    # pan=[-1, 0, 0, 1, 1, 0],
    pan=var([-1, 0, 1, 0]),
    expand=linvar([0,1], [32,inf], start=Clock.mod(4)),
    # verb=0,
    verb=linvar([0,1], [32,inf], start=Clock.mod(4)),
).pause(4, 16)

n2 >> dakeys(
    # chords,
    # chords + P[0, 2, 0, P(0, 2)],
    # chords2,
    chords3,
    # dur=cascara,
    dur=PDur(5,8),
    sus=linvar([.3, 3], 16),
    oct=(4,5),
    # oct=4,
    room2=1,
    pan=[-1, 0, 1]
).pause(4, 16, 8)



b9 >> bass303(
    chords,
    dur=PDur(3, 8),
    # sus=b1.dur - 0.1,
    # cutoff=linvar([0, 1, .5], 32, start=Clock.mod(4))
).only()

b9.cutoff=0
b9.reso=0
b9.decay=0
b9.env_mod=0

b9.sus=.5

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

k_all.stop()

k4 >> play(".VxV", lpf=200, sample=4, amp=1, sdb=1, dur=1/4, room2=10, output=12, cut=.9).fadein(16)

k4.fadeout()

d3 >> play("<(-~)[~-]>", dur=.5, amplify=pa16_2, amp=2)

k1 >> play(
    "<V><x>",
    dur=clave23,
    sample=P[0, 1, 2].stutter(5),
    amplify=pa32,
    amp=1,
    output=12
)

e3 >> play(
    "#",
    dur=8,
    bits=4,
    cut=1 / 4,
    room=1,
    crush=8,
    shape=0.5,
    pan=[-1, -1, 1],
    slide=-1
)

e3.stop()


Clock.bpm = linvar([120, 160], PRand(8,32))


bpm_to(60, 32)
