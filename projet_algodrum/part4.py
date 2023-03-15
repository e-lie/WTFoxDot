
Clock.clear()

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 4, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor

#########################################################################

change_bpm(140, True, 0.22)

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
