
Clock.clear()

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 4, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor

###############################################

change_bpm(110, True, 0.22)

d1 >> play(
    ".c",
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
d1.degree = "(.*)c"
d1.degree = "(.*)(cc[**]=)"
d1.degree = "(***~..[**~][~*][*~]..cccccc)"
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

a2 >> padarp(
    [0, 2,0,5],
    # dur=[1.1,.9],
    dur=.5,
    oct= (3,6),
    amp=.8
)

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