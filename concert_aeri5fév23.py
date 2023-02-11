Clock.clear()

from FoxDot import *
from FoxDot.preset import *

fordrip, gone = add_chains("fordrip1+", "gone1+")
apad, souls = add_chains("apad1+", "souls1")
marimba, vibra = add_chains("marimba1+", "vibra1")
# darkpass, hpluck = add_chains("darkpass+", "hpluck1+")
dakeys, padarp = add_chains("dakeys1", "padarp1+")
# rdrum, bpiano = add_chains("rdrum1+", "bpiano+")
acidbb, bass303 = add_chains("acidbb", "bass303+")

change_bpm(110, True, 0.22)

Scale.default = Scale.minor

Root.default = 0

a1 >> apad(
    [0, 4, -2],
    dur=PRand(2, 8),
    sus=PRand(4, 12),
    vol=1.1,
    attack=.4,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
).span(.5).fadein(32).span(srot(64))

a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))

a1.oct=Pvar([5,(4,5),P*(4,6)])

a1.detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a1 + (0,12)

a1.fadeout(16, fvol=.7)

a4 >> gone([0], dur=4, dull=0, body=0, arp=0, pitch=0).span(srot(48)).fadein(32)

a4.dull = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
# a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.pitch = .5#linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.oct=3

a4.fadeout(64, fvol=.4)

a1.fadeout(16, ivol=.7)

a1.stop()

a4.stop()

s1 >> space([0], dur=[.5,.25,.25], oct=5, amp=P[.8,.7,.8,1.1]*1.5, sus=s1.dur+0.2).mpan(0)

s1.mpan([0,2])

s1.mpan(P[0,2].stutter(3))

a4.fadeout(8, ivol=.4)

a4.stop()

s1.oct=(4,5)

s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]

s1.mpan(mrot(6).shuffle().stutter(2))

s1.oct=(4,5,3)

s2 >> blip([0], dur=[.5,.25,.25], oct=5, amp=P[.8,.7,.8,1.1]*2).mpan(0)

s2.degree = [0,2]

s2.degree = PWalk()

s2.mpan(3)

s2.sus=linvar([.2,1.5], PRand(4,16))

s1.oct=P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3]

Root.default = var(PTri(12), 4, start=Clock.mod(4))

s1.oct=Pvar([P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3], [3,4,5,6], P(3,4,5,6)], 8)

s2.mpan(P[0,2,3,1].stutter(9))

bpm_to(120, 16)

change_bpm(120, True, 0.22)

Root.default = 12

s2.dur=PDur(3,7)

s2.oct = P[5,5,5,6,4]

Root.default = var(PTri(12), .25)

s1.mpan([0,1])

s2.mpan([3,5])

Root.default = var(PTri(12), 4)

s1.fadeout(16)

s2.only()

Root.default = 12

a1 >> padarp(
    [0, 2],
    dur=[1,.5],
    oct=3,
    amp=.8,
    verb=0,
    delay=0,
    detune=sinvar([0,1], PWhite(.2,3)[:16]),
    expand=0,
    vol=.7,
).span(expvar([0,1,-1,3,0,5], PRand(8,32))).fadein(16)

a1.dur=PDur(3,8)

a1.verb=linvar([0,1], [32,inf], start=Clock.mod(4)),

a1.delay=linvar([0,1], [64,inf], start=Clock.mod(4)),

a1.expand=linvar([0, 1], 16),

Root.default = 0

d1 >> play(
    ".~",
    dur=.5,
    amp=1.5*PWhite(.8,1.2),
    rate=.7,
    cut=2,
    room2=.3,
    crush=1,
    bits=5,
).mpan(mrot(64))

d1.degree = "(.i)~"
d1.dur = var([.5, .25], [7,1])

a2 >> padarp(
    [0, 2,0,5],
    # dur=[1.1,.9],
    dur=.5,
    oct= 6,
    amp=.8
)

Root.default = 0

d1.degree = "(.i)(~~[--]=)"

d1.dur=PDur(5,8)

k1 >> play(
    "x.",
    dur=.5,
    amp=PWhite(1,1.5, seed=3)[:7],
    rate=P[1.2, 1.5, 1]*linvar([.5,1], 32),
    # rate=1,
    cut=1,
    output=12,
    sample=3,
    pan=0,
)

k1.degree = "<([xx]xx.)(..x)>",

k1.degree = "x."

k1.pause(8,32)

k1.dur = PDur(3,8)

k1.bits = 5
k1.crush = linvar([0, 8], 24, start=Clock.mod(4))
d1.rate = linvar([.7,.5], 16, start=Clock.mod(4))
d1.crush = linvar([1, 8], 24, start=Clock.mod(4))

s1.fadeout(32)

s2.fadeout(32)

d1.crush = 0
k1.crush = 0

bpm_to(100, 16)

change_bpm(100, True, 0.22)

b1 >> blip(
    PWalk(start=0, seed=10)[:64] * 2,
    dur=.25,
    # dur=var([.25, 1/3, .5, 1/6], [6,2,6,2]),
    # dur=Pvar([P[.45, .55, .5, .5, .48, .52]/2, P[1 / 3, 2 / 3]/2], [12, 4]),
    sus=PWhite(.5,2),
    amp=PWalk(start=30, seed=10)[:64] / 30 + .8,
    oct=var([4,5,6,7,6,5],8),
    # pan=var([-1,.5,0,1,-.5], PRand(1,4)/2)
).mpan(PRand(0,5))

b1 + P[0, 0, 0, 1, 1, 0, -2, 0, 1]

b1 + P(0,2)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)

b2 >> marimba(
    [0, 2, 1, -2],
    dur=[.3, .4, .4],
    sus=1,
    oct=P[3, 4, 6].stutter(8),
    amp=PWalk(start=30, seed=13)[:30] / 30,
    vol=.8,
).span(srot(16)b2 >> marimba(
    [0, 2, 1, -2],
    dur=[.3, .4, .4],
    sus=1,
    oct=P[3, 4, 6].stutter(8),
    amp=PWalk(start=30, seed=13)[:30] / 30,
    vol=.8,
).span(srot(16))
)

k1.dur=.5

d1.fadeout(24)
d1.stop()

b2.dur=Pvar([[.4,.3,.3],.25],[12,4])

b1.dur=.5

d1.crush = linvar([8, 1], 24, start=Clock.mod(4))
d2.crush = linvar([8, 0], 24, start=Clock.mod(4))

b1.pause(12,16)

b1.stop()

m2 >> play(
    "---(-.)",
    sdb=1,
    sample=0,
    hpf=2000,
    dur=1 / 4,
    leg=3,
    amp=PWhite(1.5, 3),
    rate=var([1, 1.5, .4], 7)
).pause(2, 7)

m2.mpan(var([0,3,1,4,2,5], 7))

a2 >> fordrip(
    [0],
    dur=4,
    oct=3,
    vol=linvar([0, .8, .2, .7], PRand(2, 24), start=Clock.mod(4)),
    bitcrush = 0,
    drip = 0,
    psy = 0,
    ambiance = 0,
).span(linvar(P[0, 1, .4, .8, 0, .6] * 6, PRand(2, 24), start=Clock.mod(4))).fadein(64)

a2.oct=[2,3,5,7]

k1.stop()

a2.bitcrush=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a2.drip=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a2.psy=1
a2.ambiance=1

a2.sampfadeout(16)

a2.only()

m1 >> marimba("ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]", oct=3, amp=linvar([.1,.9],16, bus2=.5), dur=.125).humz().span(srot(64)).fadein()

m3 >> marimba("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=5, amp=linvar([.1,.9],7), dur=cascara, bus4=.5).humz().span(srot(64))

m1.degree = [0,2,4,2,-2]

m3.degree = [0,2,4,2,-2]

m3.stop()

d2.fadeout()

d2.stop()

Root.default = 0

k1.fadeout(16)

m_all.only()

chords = var([0,5,2,3],[8,4,2,2])

m1 + chords
m3 + chords

Scale.default = Scale.minor

m3.ampfadeout()

m3.stop()

a2.stop()

m2.stop()

b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=7).pause(4,16).mpan(mrot(16))

b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=5).pause(4,16,8).mpan(mrot(24))

k1.stop()

m1.fadeout(16)

m1.stop()


b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=6).pause(4,16).mpan(mrot(16)) + P(0,2)
b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=4).pause(4,16,8).mpan(mrot(24)) + P[0, 2, 0, P(0,2)]

d7 >> bbass(chords, dur=PSum(3,2), oct=(2,3), amp=1, output=12)

d7 + [0,0,2] + [0,0,0,0,-1]

k2 >> play("V.", dur=.5, amp=1, crush=8, bits=4, lpf=linvar([200,1000],32), output=12) #Ah le kick enfin
k1 >> kicker("<v.>", dur=.5, amp=1, crush=4, bits=16, rate=1, output=12)


bpm_to(140, 48)

change_bpm(140, True, 0.22)

Root.default = var(PTri(12), .25)

Root.default = 0

#overwrite preceding hh
m2 >> play(".--(-*-[**])", sdb=1, sample=0, hpf=2000, dur=1/4, leg=10, pan=P[-1,0,1].stutter(3)).pause(2,7).mpan(mrot(24))

e3 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), rate=1, amp=.8).pause(4,16,12).mpan(mrot(32))

d1 >> play("=.*.", sdb=1, sample=3, hpf=3000, triode=1, crush=1, pan=.4).mpan(mrot(32))

k2 >> kicker("<(VVV(V[.V]V[VV]))(...V)>", dur=.5, amp=1, crush=8, bits=linvar([6,2],24, start=Clock.mod(4)), output=12)

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

k3.sampfadeout(16)

k3.only()

k3.degree = Pvar(["<.X><.v>", '.', '<X.><v.>', '.'], [44, 4]),

k3.sample = var([1,4,0],48)
k3.room2 = linvar([0,1], 16, start=Clock.mod(4))
m2.room2 = linvar([0,1], 16, start=Clock.mod(4))

b_all.fadeout(16)

Root.default = 0

pitches = [0,2,2,1,-2,0,0,1]

b1 >> bass303(chords, dur=[.25,.5], sus=b1.dur-0.04)
b1 >> bass303(chords, dur=PDur(5,8), sus=b1.dur-0.04)
b1.span(srot(32))
b1.cutoff=0
b1.reso=0
b1.env_mod=1
b1.decay=0
b1.oct=5

b1.cutoff=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

b1.reso=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
b1.decay=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

b1.pause(8,48,40)

pitches = [0,2,4,5,0,2,4]

k4 >> play(".VVV", lpf=300, sample=7, amp=1, sdb=1, dur=1/4, room2=10, output=12).fadein(16)

b3 >> vibra(chords, dur=.25, sus=b1.dur-.04, amp=1, vol=1.5).span(srot(32))

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, rate=var([1,1.3]), sample=1, amp=3).mpan(mrot(32)).fadein()

b3 + pitches

k4.fadeout(32)

k4.stop()

k3.fadeout(16)

d3 >> play("<(-~)[~-]>", dur=.5, amplify=pa16_2).mpan(mrot(16))

k3 >> play("V", dur=clave23, sample=P[0,1,2].stutter(5), amplify=pa32, amp=1, output=12)

b2 >> bbass([0,2,4,-5,2], dur=cascara, oct=4), amp=2) + P(0,2)

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)

k3 >> kicker("<V....V..>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=2)
d7 >> play("<..O...o.>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=2).mpan(mrot(16))

d8 >> play("/", dur=16, pan=[-1, 0, -1]).mpan(mrot(32))

k3.sampfadeout(8)

b1 >> blip([0,2,0,0,-2,2], dur=[.25,.5], oct=6, amp=[1,0,0,0,1,0], sus=1).mpan(0)
b2 >> blip([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,1,0,0,0,0]).mpan(1)
b2 >> blip([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,1,0,0,0,0]).mpan(mrot(16))
b3 >> blip([0,2,0,0,-2,2], dur=.5, oct=3, amp=[0,0,1,0,0,0]).mpan(2)
b4 >> blip([0,2,0,0,-2,2], dur=[.75,.5], oct=7, amp=[0,1,0,1,0,0]).mpan(3).pause(4,24,12)
b5 >> blip([0,2,0,0,-2,2], dur=.5, oct=5, amp=[0,0,0,0,1,0]).mpan(4)
b6 >> blip([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,0,1,0,0,1]).mpan(5).pause(4,16)

b_all.amplify=3

# k3 >> kicker("<X.o.><v...>", lpf=00, sample=(2,4), amp=1.5, sdb=1, dur=1/4)
k3 >> kicker(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=1.5)
k3.sample = var([1,4,0],48)
k3.lpf=150
k3.amp=1.5
k3.leg=0
# k1.crush=linvar([0,32],16); k1.bits=linvar([4,8],7)
k3.room2 = 1
k3.mpan((0,1))


bpm_to()

k3.sampfadeout(32)
k3.only()

d1 >> play("=.*.", sdb=1, sample=3, hpf=3000, triode=1, crush=1, pan=.4).mpan(mrot(32))
d2 >> play(".--(-*-[**])", sdb=1, sample=0, hpf=2000, dur=1/4, leg=10, pan=P[-1,0,1].Astutter(3)).pause(2,7).mpan(mrot(24))


b_all.fadeout(16)

pitches = [0,2,2,1,-2,0,0,1]

b1 >> bass303(pitches, dur=[.25,.5], sus=b1.dur-0.04)
b1.span(srot(64))
b1.cutoff=0
b1.reso=0
b1.env_mod=1
b1.decay=0
b1.oct=5

b1.dur=.25

b1.cutoff=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

b1.reso=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
b1.decay=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

b1.pause(8,48,40)

pitches = [0,2,4,5,0,2,4]

k4 >> play(".VVV", lpf=300, sample=7, amp=2, sdb=1, dur=1/4, room2=10).fadeout(16)

k1 >> kicker(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=1.5, lpf=500)

k1 >> play(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sample=1, amp=1.5)

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, rate=var([1,1.3]), sample=1, amp=3)

d3.amplify=2

b3 >> blip(pitches, dur=P[.5,.5,.25,.5,.25,.5,.25,.5,.5,.25]*1, sus=linvar([.1,2],32), amp=3).mpan(mrot(16))

d2 >> play(".---", sdb=1, sample=0, hpf=2000, dur=1/4, leg=3, amp=2).pause(2,7)

pitches = [0,2,4,5,0,2,4]

k4 >> play(".VVV", lpf=300, sample=7, amp=2, sdb=1, dur=1/4, room2=10, output=12).fadein(16)

k1 >> kicker(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=1.5, lpf=500)

k1 >> play(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sample=1, amp=1.5).mpan([0,1])

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, rate=var([1,1.3]), sample=1, amp=3)

b3 >> blip(pitches, dur=P[.5,.5,.25,.5,.25,.5,.25,.5,.5,.25]*1, sus=b1.dur-.04, amp=3).mpan(mrot(64))

d2 >> play(".---", sdb=1, sample=0, hpf=2000, dur=1/4, leg=3, amp=2).pause(2,7)

bpm_to(160,32)

change_bpm(120, True, 0.22)

Clock.clear()

b1 >> blip(0, dur=.5).mpan(mrot(16)) + (P[0,2,-2,4] + P(0,2))

d1 >> play("(x[xx]).-c", dur=.25)



