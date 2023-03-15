Clock.clear()

from FoxDot import *
from FoxDot.preset import *

fordrip, gone = add_chains("fordrip1+", "gone1+")
apad, souls = add_chains("apad1+", "souls1")
marimba, vibra = add_chains("marimba1+", "vibra1")
darkpass, hpluck = add_chains("darkpass", "hpluck1")
dakeys, padarp = add_chains("dakeys1", "padarp1+")
rdrum, bpiano = add_chains("rdrum1", "bpiano")
acidbb, bass303 = add_chains("acidbb", "bass303+")

#####################################

cc >> play("t", dur=1, pan=-1, amp=2)

#####################################

change_bpm(50, True, 0.22)
change_bpm(100, True, 0.22)

Scale.default = Scale.minor

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 4, start=Clock.mod(4))
Root.default = var(PTri(12), .25)
Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)

######################################

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
)

a1.stop()

a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
a1.oct=Pvar([5,(4,5),P*(4,6)])
a1.detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a1 + (0,12)
a1 + (0,4,5)

#########################################

a4 >> gone([0], dur=4, dull=0, body=0, arp=0, pitch=0)
a4.fadein(32)

a4.oct = 3
a4.oct = (3,2,6)

a4.dull = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.arp = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a4.pitch = .5

##########################################

b2 >> marimba(
    [0, 2, 1, -2],
    dur=1/3,
    sus=1,
    oct=P[3, 4, 6].stutter(8),
    amp=PWalk(start=30, seed=13)[:30] / 30,
    vol=.8,
)

################################################

s1 >> space([0], dur=[.5,.25,.25], oct=5, amp=P[.8,.7,.8,1.1]*1.5, sus=s1.dur+0.2, pan=1) + P*(0,2)
s1.oct=Pvar([(4,5), 3, (3,4,5)], [2,4,3,3])
s1.oct=[3,4,5]

s1 + (0,2,)

s1.dur=P[P[.5, .5, .5, P*(.25,.25)],.25,.25]


s1.oct=(4,5,3)
s1.pause(8,32)

###################################################

s2 >> blip([0], dur=P[.5,.25,.25], sus=linvar([0,2], [16,32,64]), oct=[5,8,6], amp=P[.8,.7,.8,1.1]*2, pan=.5)

s1.stop()

s2.dur = var([.25,.5,2/5],4)

s2.degree = [0,2,0,4,1,5,0,5,3]
s2.degree = PWalk()
s2.mpan(0)
s2.sus=2
s2.sus=linvar([.2,1.5], PRand(4,16))

s2.oct=P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3]

s2.oct=Pvar([P[P(4,5,3,6), (4,5), (3,6), 5, 6, 3], [3,4,5,6], P(3,4,5,6)], 8)
s2.pause(8,32, 16)

s2.dur=PDur(3,7)/2

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

###############################################

d1 >> play(
    ".~",
    dur=.5,
    amp=3*PWhite(.8,1.2),
    rate=.7,
    cut=2,
    room2=.3,
    crush=1,
    bits=5,
    pan=1
)

d1.pause(8,32,16)
d1.degree = "(.i)~"
d1.degree = "(.i)(~~[--]=)"
d1.degree = "(iiii..[iii][ii][ii]..IIIII)"
d1.crush = 16
d1.bits = 3
d1.dur=PDur(5,8)
d1.dur = var([.5, .25], [7,1])

################################################

p1 >> dakeys(
    [0, 2, 5, 2, -2, 1, 4],
    dur=.5,
    # oct=(3,6),
    oct=6,
    amp=.8,
    pad=0,
    modelb=0,
    pluck=0,
    space=.4,
)

################################################

a2 >> padarp(
    [0, 2,0,5],
    # dur=[1.1,.9],
    dur=.5,
    oct= (3,6),
    amp=.8
)

################################################


k1 >> play(
    # "x{Vv}",
    "[VV]",
    # "{VVV[VV]V[VVV]}",
    # "<xVXv><*>",
    # dur=PDur(3,8),
    dur=.5,
    # dur=var([.125,.25],[.5,1]),
    # dur=PRand([2,4])/6,
    rate=P[1.2, 1.5, 1]*linvar([.5,1], 8),
    # rate=1,
    cut=1,
    output=12,
    sample=3,
    pan=0,
)

k1.pause(8,16,4)
k1.pause(0,16,4)

k1.every(.5,"stutter",2)
k1.fadeout()
k1.degree = "<([xx]xx.)(..x)>",

k1.degree = "x."
k1.degree = "(xxx[xx])"

k1.rate = PWhite([.8,1])
k1.amp = PWhite([1,1.2])

k1.pause(8,32)

k1.dur = PDur(3,8)

k1.bits = 5
k1.crush = linvar([0, 8], 24, start=Clock.mod(4))

###################################################

b1 >> blip(
    PWalk(start=0, seed=10)[:64] * 2,
    dur=var([.5,.25,1/3], [8]),
    # dur=.5,
    # dur=var([.25, 1/3, .5, 1/6], [6,2,6,2]),
    # dur=Pvar([P[.45, .55, .5, .5, .48, .52]/2, P[1 / 3, 2 / 3]/2], [12, 4]),
    sus=PWhite(.5,2),
    # amp=PWalk(start=30, seed=10)[:64] / 30 + .8,
    oct=var([4,5,6,7,6,5],8),
    # pan=var([-1,.5,0,1,-.5], PRand(1,4)/2)
    pan=1,
    amp=3
)

b1.fadeout(32)

b1 + P[0, 0, 0, 1, 1, 0, -2, 0, 1]
b1 + P(0,2)

b1.stop()

#####################################################

b2 >> marimba(
    [0, 2, 1, -2],
    dur=1/3,
    sus=1,
    oct=P[3, 4, 6].stutter(8),
    amp=PWalk(start=30, seed=13)[:30] / 30,
    vol=.8,
)

b2 + P(0,2)
b2.oct = (3,5,6)

d1.fadeout(24)
d1.stop()

b2.dur=Pvar([[.4,.3,.3],.25],[12,4])

#########################################################

d3 >> play(
    "---(-.)",
    sdb=1,
    sample=0,
    hpf=2000,
    dur=1/4,
    leg=3,
    amp=3,
    rate=var([1, 1.5, .4], 7),
    pan=1,
).pause(2, 7)

############################################################

k1 >> play("X{.xX+}(X.)", dur=PDur(3,8), output=12)
k1.fadein()
k1.pause(24,32)
k1.rate = PWhite(.8,2)
k1.dur = Pvar([PDur(3,8), .25, .5, PDur(5,8)], PRand(2,8))

k1.crush = PWhite(0,8)
k1.bits = PWhite(3,8)

###########################################################

a2 >> fordrip(
    [0],
    dur=4,
    oct=3,
    vol=linvar([0, .8, .2, .7], PRand(2, 24), start=Clock.mod(4)),
    bitcrush = 0,
    drip = 0,
    psy = 0,
    ambiance = 0,
)

a2.span(linvar(P[0, 1, .4, .8, 0, .6] * 6, PRand(2, 24), start=Clock.mod(4)))
a2.fadein(24)

a2.oct=[2,3,5,7]
a2.bitcrush=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a2.drip=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a2.psy=1
a2.ambiance=1
a2.only()
a2.stop()

##############################################################

change_bpm(70, True, 0.22)

m1 >> marimba("a", oct=P(3,4,5), amp=linvar([.1,.9],16, bus2=.5), dur=.125)

m1 >> marimba(
    "abfff...ffbafff",
    oct=([2, 5], [3, 4, 5], 7),
    amp=linvar([.3, .9], 16),
    dur=Pvar([.125, cascara / 2], [8, 4])
)

d1 >> play("<(V----)..>", dur=.125)

m1 >> marimba("ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]", oct=3, amp=linvar([.1,.9],16, bus2=.5, vol=1.2, dur=.5), dur=.125).humz().span(srot(64))

m3 >> vibra("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=[2,3,5], amp=linvar([.5,.9],7), dur=cascara, bus4=.5)

Root.default = var([0,2,12])

m3.stop()

m1.degree = [0,2,4,2,-2]

m3.degree = [0,2,4,2,-2]

m3.stop()
m1.stop()


m3.stop()

d2.fadeout()

d2.stop()

Root.default = 0

k1.fadeout(16)

m_all.only()

chords = var([0,5,2,3],[8,4,2,2])

Root.default = 0

Root.default = chords

m1 + chords
m3 + chords

Scale.default = Scale.minor

m1.ampfadeout()

m3.stop()

a2.stop()

m2.stop()

b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=7)
b2.pause(4,16)

b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=5, pan=0)
b1.pause(4,16,8)

b1.only()

k1.stop()

m1.fadeout(16)

m1.stop()

b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=6).pause(4,16).mpan(mrot(16)) + P(0,2)
b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=4).pause(4,16,8).mpan(mrot(24)) + P[0, 2, 0, P(0,2)]
b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=(4,6)).pause(4,16,8).mpan(mrot(24)) + P[0, 2, 0, P(0,2)]

b2.stop()

b2 + [0,1,2,1]

d7 >> bbass(chords, dur=PDur(5,8), oct=(2,3), amp=1, output=12)

d7 + [0,0,2] + [0,0,0,0,-1]

d7.sampfadeout(64)

d7.only()

k2 >> play("V.", dur=.5, amp=1, crush=8, bits=4, lpf=linvar([200,1000],32), output=12) #Ah le kick enfin
k1 >> kicker("<v.>", dur=.5, amp=1, crush=4, bits=16, rate=1, output=12)

k_all.only()

bpm_to(100, 48)

change_bpm(160, True, 0.22)

Root.default = var(PTri(12), .25)

Root.default = var([0,2,4], 16)

Root.default = 0

d7.pause(8,32,16)

#overwrite preceding hh
h2 >> play(".--(-*-[**])", sdb=1, sample=0, hpf=2000, dur=1/4, leg=10, pan=P[-1,0,1].stutter(3))

h2.pause(2,7)

e3 >> play("*", dur=.25, sample=P[0,1,2].stutter(4), rate=1, amp=2)
e3.pause(4,16,12)

d1 >> play("=.*.", sdb=1, sample=3, hpf=3000, triode=1, crush=1, pan=.4)

k2 >> kicker("<(VVV(V[.V]V[VV]))(...V)>", dur=.5, amp=1, crush=8, bits=linvar([6,2],24, start=Clock.mod(4)), output=12)

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

b1 >> bass303(chords, dur=[.25,.5], sus=b1.dur-0.04)
b1 >> bass303(chords, dur=PDur(5,8), sus=b1.dur-0.04)
b1.span(srot(32))
b1.cutoff=0
b1.reso=0
b1.env_mod=1
b1.decay=0
b1.oct=5


b1.stop()

b1.cutoff=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

b1.reso=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
b1.decay=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

b1.pause(8,48,40)

b1.stop()

pitches = [0,2,4,5,0,2,4]

k4 >> play(".VVV", lpf=300, sample=7, amp=1, sdb=1, dur=1/4, room2=10, output=12).fadeout()

k4.fadeout()

b3 >> vibra(chords, dur=[.5,.5], sus=b1.dur-.04, amp=1, vol=1.5).span(srot(32))

b3 >> blip(chords, dur=.25, sus=b1.dur-.04, amp=1, vol=1.5).span(srot(32))

b3 >> blip

d3 >> play("<.c.c.c.cc><...(...*)><..(i).>", dur=1/4, rate=var([1,1.3]), sample=var([1,2], 8), amp=3).mpan(mrot(32)).stop()

a4.stop()

m3.stop()

b3 + pitches

k4.fadeout(32)

k4.stop()

k3.fadeout(16)

d3 >> play("<(-~)[~-]>", dur=.5, amplify=pa16_2).mpan(mrot(16))

k3 >> play("<V><x>", dur=clave23, sample=P[0,1,2].stutter(5), amplify=pa32, amp=2, output=12)

b2 >> bbass(chords, dur=cascara, oct=4, amp=2) + P(0,2)

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

k4 >> kicker("<V....V..>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=2)
d7 >> play("<..O...o.>", dur=.5, sample=var([0,1,2], 32), rate=linvar([.8,1.2], 16), amp=2).mpan(mrot(16))

k4.stop()

d8 >> play("/", dur=16, pan=[-1, 0, -1]).mpan(mrot(32))

Clock.bpm = linvar([120, 160], PRand(8,32))

Clock.bpm = 160

k4.sampfadeout(24)

k3.only()

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
k3.stop()

d1 >> play("=.*.", sdb=1, sample=3, hpf=3000, triode=1, crush=1, pan=.4).mpan(mrot(32))
d2 >> play(".--(-*-[**])", sdb=1, sample=0, hpf=2000, dur=1/4, leg=10, pan=P[-1,0,1].Astutter(3)).pause(2,7).mpan(mrot(24))

d1.stop()


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

k_all.stop()

k4 >> play(".VVV", lpf=300, sample=7, amp=2, sdb=1, dur=1/4, room2=10).fadeout(16)

k1 >> kicker(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=1.5, lpf=500)

k1 >> play(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sample=1, amp=1.5)

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, rate=var([1,1.3]), sample=1, amp=3)

d3.amplify=2

b3 >> blip(pitches, dur=P[.5,.5,.25,.5,.25,.5,.25,.5,.5,.25]*1, sus=linvar([.1,2],32), amp=3).mpan(mrot(16))

d2 >> play(".---", sdb=1, sample=0, hpf=2000, dur=1/4, leg=3, amp=2).pause(2,7)

pitches = [0,2,4,5,0,2,4]

k4 >> play(".VVV", lpf=300, sample=7, amp=2, sdb=1, dur=1/4, room2=10, output=12).fadeout(16)

k1 >> kicker(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sdb=1, sample=1, amp=1.5, lpf=500)

k1 >> play(Pvar(["<.X><.v>",'.','<X.><v.>','.'], [44,4]), dur=1/2, sample=1, amp=1.5).mpan([0,1])

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, rate=var([1,1.3]), sample=1, amp=3)

b3 >> blip(pitches, dur=P[.5,.5,.25,.5,.25,.5,.25,.5,.5,.25]*1, sus=b1.dur-.04, amp=3).mpan(mrot(64))

d2 >> play(".---", sdb=1, sample=0, hpf=2000, dur=1/4, leg=3, amp=2).pause(2,7)

bpm_to(260,64)

change_bpm(60, True, 0.22)

Clock.clear()

b1 >> blip(0, dur=.5, amp=3).mpan(mrot(16)) + (P[0,2,-2,4] + P(0,2))

d1 >> play("(x[xx]).-c", dur=.25)


bpm_to(60, 64)
