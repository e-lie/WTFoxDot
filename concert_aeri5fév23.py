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
Root.default = var([0,2,5,4], 16)
Root.default = var(PTri(12), 4)
Root.default = var([0,2], 32)

s1 >> space([0], dur=[.5,.25,.25], oct=5, amp=[.8,.7,.8,1.1]).mpan(0)

s1.mpan([0,2])

s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]

s1.mpan(P[0,2].stutter(3))

s1.mpan(P[0,2,3,1])

s1.oct=(4,5)

s1.mpan(mrot(6).shuffle().stutter(2))

s1.oct=(4,5,3)

s1.oct=P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3]

s2 >> blip([0], dur=[.5,.25,.25], oct=5, amp=P[.8,.7,.8,1.1]*2).mpan(0)

s2.sus=1.2

s2.mpan(P[0,2,3,1].stutter(9))

s2.dur=PDur(3,7)

s2.oct = P[5,5,5,6,4]


# TODO make all the multiparams progressive andd musical
a1 >> padarp(
    [0, 2],
    # dur=[2,1.2,1.8, 1],
    dur=[1,.5, 2],
    oct=3,
    amp=.8,
    # verb=0,
    verb=linvar([0,1], [32,inf], start=Clock.mod(4)),
    # delay=0,
    delay=linvar([0,1], [64,inf], start=Clock.mod(4)),
    detune=sinvar([0,1], PWhite(.2,3)[:16]),
    # expand=linvar([0, 1], 16),
    expand=0,
    vol=.7,
).span(expvar([0,1,-1,3,0,5], PRand(2,8)))

d1 >> play(
    "<x.><{~~-v}{--[--]}~(=~)>",
    dur=var([.5, .25, .5, .165], [6, 6, 3, 1]),
    amp=1.5,
    rate=P[1.2, 1.5, 1]*linvar([.7,2], 32),
    cut=.8,
    # cut=2,
    room2=0,
).mpan(mrot(32))

a2 >> padarp(
    [0, 2,0,5],
    # dur=[1.1,.9],
    dur=.5,
    oct= 4,
    amp=.8
)

## TODO Where to put that
Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.majorPentatonic

# k1 >> play("c.{..c+}{vccc+}(v{vv+cc})", dur=[.4,.3,.3], amp=2).pause(0,24).mpan(PRand(0,1))

b1 >> marimba(
    [0, 2, 1, -2],
    dur=[.25, .25, .25, .25, .3, .4, .4],
    sus=1,
    oct=P[3, 4, 6].stutter(8),
    amp=PWalk(start=30, seed=13)[:30] / 30,
    vol=.8,
).span(srot(16)).pause(12,16)

b1 >> marimba([0,2,1,-2], dur=[.25,.25,.3,.4,.4], sus=1, oct=P[3,4,6].stutter(8), amp=PWalk(start=30, seed=13)[:30]/30).span(srot(16))
b2 >> marimba([4,4,5,6], dur=[.5,.3,.4,.4], sus=1, oct=P[4,5,7].stutter(7), amp=PWalk(start=30, seed=11)[:30]/30).span(srot(16))

b1.stop()

d2 >> play(".---", sdb=1, sample=0, hpf=2000, dur=1/4, leg=3, amp=2).pause(2,7)

b1 >> blip(
    PWalk(start=0, seed=10)[:64] * 2,
    dur=.25,
    # dur=Pvar([P[.45, .55, .5, .5, .48, .52]/2, P[1 / 3, 2 / 3]/2], [12, 4]),
    sus=2,
    amp=PWalk(start=30, seed=10)[:64] / 30 + 1,
    oct=var([4,5,6,7,6,5],8),
    # pan=var([-1,.5,0,1,-.5], PRand(1,4)/2)
).mpan(PRand(0,5)) + [0, 0, 0, 1, 1, 0, -2, 0, 1]

a2.fadeout(32)

a1 >> apad([0,4,-2], dur=PRand(2,8), sus=PRand(4,12), vol=1.1).span(srot(12))

a1.apad_attack=.4
a1.apad_space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a1.apad_thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
a1.apad_detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a1.sampfadeout(32)

b2.stop()


a2 >> fordrip([0], dur=4, oct=3, fordrip_on=1, vol=linvar([0,.8,.2,.7], PRand(2,24), start=Clock.mod(4))).span(
    linvar(P[0,1,.4,.8,0,.6]*6,PRand(2,24), start=Clock.mod(4))
).fadein(64)

a2.oct=[2,3,5,7]

a_all.only()

a2.fordrip_bitcrush=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a2.fordrip_drip=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a2.fordrip_psy=1
a2.fordrip_ambiance=1

a2.fadeout(32)
a1.fadeout(32)

a4 >> gone([0], dur=4)
a4.gone_dull = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.gone_body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
# a4.gone_pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.gone_pitch = .5#linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.gone_pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.gone_arp = 0# linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.arp = 0
a4.gone_arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.oct=2
a4.span(srot(32))

a4.only()

b1.fadeout(32)

a1.sampfadeout(64)

a1.only()

a4.fadeout(64)

m1 >> marimba("ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]", oct=3, amp=linvar([.1,.9],16, bus2=.5), dur=.125).humz().span(srot(64)).fadein()

m3 >> marimba("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=5, amp=linvar([.1,.9],7), dur=cascara, bus4=.5).humz().span(srot(64))

m3.stop()

chords = var([0,5,2,3],[8,4,2,2])

b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=7).pause(4,16).mpan(mrot(16))

b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=5).pause(4,16,8).mpan(mrot(24))

b_all.only()

e3 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), rate=1, amp=.8).pause(4,16,12).mpan(mrot(32))

b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=6).pause(4,16).mpan(mrot(16)) + P(0,2)
b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=4).pause(4,16,8).mpan(mrot(24)) + P[0, 2, 0, P(0,2)]

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, lpf=800, hpf=200, rate=var([1,1.3]), sample=1).mpan(mrot(16))

k2 >> play("V.", dur=.5, amp=1, crush=8, bits=4, lpf=linvar([200,1000],32), output=12) #Ah le kick enfin
k1 >> kicker("<v.>", dur=.5, amp=1, crush=4, bits=16, rate=1, output=12)

k2 >> kicker("<(VVV(V[.V]V[VV]))(...V)>", dur=.5, amp=1, crush=8, bits=linvar([6,2],24, start=Clock.mod(4)), output=12)

d7 >> bbass(chords, dur=PSum(3,2), oct=(2,3), amp=1.5, output=12) + [0,0,2] + [0,0,0,0,-1]

d7.pitch = PRand(1,10)

bpm_to(140, 48)

b1.sampfadeout(32)
d7.only()

k2.stop()

bpm_to(130)

change_bpm(140)


e3.stop()

# k3 >> kicker("<X.o.><v...>", lpf=00, sample=(2,4), amp=1.5, sdb=1, dur=1/4)
t3 >> play(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=2, output=12)
t3.sample = var([1,4,0],48)
t3.lpf=200
t3.amp=2
t3.leg=0
t3.crush=linvar([0,32],16)
t3.bits=linvar([4,8],7)
t3.room2 = 1

k1.only()

d1 >> play("=.*.", sdb=1, sample=3, hpf=3000, triode=1, crush=1, pan=.4).mpan(mrot(32))
d2 >> play(".--(-*-[**])", sdb=1, sample=0, hpf=2000, dur=1/4, leg=10, pan=P[-1,0,1].stutter(3)).pause(2,7).mpan(mrot(24))

d1.only()

b_all.fadeout(16)

pitches = [0,2,2,1,-2,0,0,1]

b1 >> bass303(pitches, dur=[.25,.5], sus=b1.dur-0.04)
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

k4 >> play(".VVV", lpf=300, sample=7, amp=2, sdb=1, dur=1/4, room2=10).fadein(16)

k1 >> kicker(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=1.5, lpf=500)

k1 >> play(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sample=1, amp=1.5)

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, rate=var([1,1.3]), sample=1, amp=3).mpan(mrot(32))
b3 >> blip(pitches, dur=P[.5,.5,.25,.5,.25,.5,.25,.5,.5,.25]*1, sus=b1.dur-.04, amp=3).mpan(mrot(32))

d2 >> play(".---", sdb=1, sample=0, hpf=2000, dur=1/4, leg=3, amp=2).pause(2,7).mpan(mrot(32))

b3.sampfadeout(64)

b3.only()

k4.fadeout(64)

k1.only()


d3 >> play("<(-~)[~-]>", dur=.5, amplify=pa16_2).mpan(mrot(16))

k2 >> play("V", dur=clave23, sample=P[0,1,2].stutter(5), amplify=pa32, pan=[-1, 0, 1])

b2 >> bbass([0,2,4,-5,2], dur=cascara, oct=var([3,4,5,6,7]), amp=2) + P(0,2)

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)

k2 >> kicker("<V....V..>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=.8)
d7 >> play("<..O...o.>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=2).mpan(mrot(16))

b2 >> bbass(P[4,2,0].stutter(2), oct=(3,5), dur=[1,1,2], amplify=1)

d8 >> play("/", dur=16, pan=[-1, 0, -1]).mpan(mrot(32))

e1 >> play("*", sample=2, dur=1/4, amp=PRand(2)[:16], amplify=pa16_3).mpan(mrot(24))

d2 >> play("V", dur=clave23, sample=1, amp=1.5).mpan(mrot(32)).only()

l1 >> loop("200173-breakbeat5.wav", [0,2,2,0,0,2,2], rate=[1.35, 1.35, -1.35, -2.7], dur=[4,2,2, 1, 1, 1, 1])

Scale.default = Pvar([Scale.majorPentatonic, Scale.minor, Scale.minorPentatonic], [32, 64, 32])

e3 >> play("#", dur=8, bits=4, cut=1/4, room=1, crush=8, shape=0.5, pan=[-1,-1,1], slide=-1)

d1.only()

d1 >> play(
    '<-{-[--]}{.-}><.(V++)>',
    sample=2,
    dur=Pvar([[.45, .55, .5, .5, .48, .52], [1 / 3, 2 / 3]], [12, 4]),
    output=12,
    # pan=var([-1,,..5,0,1,-.5], PRand(1,4)/2),
    pan=0,
).mpan(mrot(32))

k1 >> play("V.", output=12, lpf=500, rate=(0,linvar([1,1.5]))).pause(8,32).mpan(mrot(16))
k2 >> play(".(---[++])", sample=1, rate=PWhite(1,2), amp=3).mpan(mrot(16))

k1.only()

b1 >> blip([0,2,0,0,-2,2], dur=[.25,.5], oct=6, amp=[1,0,0,0,1,0], sus=1).mpan(0)
b2 >> blip([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,1,0,0,0,0]).mpan(1)
b2 >> blip([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,1,0,0,0,0]).mpan(mrot(16))
b3 >> blip([0,2,0,0,-2,2], dur=.5, oct=3, amp=[0,0,1,0,0,0]).mpan(2)
b4 >> blip([0,2,0,0,-2,2], dur=[.75,.5], oct=7, amp=[0,1,0,1,0,0]).mpan(3).pause(4,24,12)
b5 >> blip([0,2,0,0,-2,2], dur=.5, oct=5, amp=[0,0,0,0,1,0]).mpan(4)
b6 >> blip([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,0,1,0,0,1]).mpan(5).pause(4,16)

# k3 >> kicker("<X.o.><v...>", lpf=00, sample=(2,4), amp=1.5, sdb=1, dur=1/4)
k3 >> kicker(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=1.5)
k3.sample = var([1,4,0],48)
k3.lpf=150
k3.amp=1.5
k3.leg=0
# k1.crush=linvar([0,32],16); k1.bits=linvar([4,8],7)
k3.room2 = 1
k3.mpan((0,1))


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

b3 >> blip(pitches, dur=P[.5,.5,.25,.5,.25,.5,.25,.5,.5,.25]*1, sus=linvar([.1,2],32), amp=3).mpan(mrot(16))

d2 >> play(".---", sdb=1, sample=0, hpf=2000, dur=1/4, leg=3, amp=2).pause(2,7)

pitches = [0,2,4,5,0,2,4]

k4 >> play(".VVV", lpf=300, sample=7, amp=2, sdb=1, dur=1/4, room2=10, output=12).fadein(16)

k1 >> kicker(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=1.5, lpf=500)

k1 >> play(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sample=1, amp=1.5).mpan([0,1])

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, rate=var([1,1.3]), sample=1, amp=3)

b3 >> blip(pitches, dur=P[.5,.5,.25,.5,.25,.5,.25,.5,.5,.25]*1, sus=b1.dur-.04, amp=3).mpan(mrot(64))

d2 >> play(".---", sdb=1, sample=0, hpf=2000, dur=1/4, leg=3, amp=2).pause(2,7)

bpm_to(60,32)

Clock.clear()
