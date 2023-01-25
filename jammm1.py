

# Yolo

Scale.default = Scale.minor
Scale.default = Pvar([Scale.major, Scale.minor], 16)

Root.default = var([4,3,0,5,2,0], [32])

a1 >> apad([0,0,2,-2], dur=2).span(srot(64))
a1 >> apad([0,4,-2], dur=PRand(2,8), sus=PRand(4,12), vol=1.1, apad_on = 1).span(srot(64))
a1.fadein(16)

a1.apad_space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4 >> gone([0,0,2], dur=4)

a1.apad_thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))

a4.gone_body = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a4.gone_pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

d3 >> play("*", dur=PWhite(.25,1), sample=P[0,1,2].stutter(4), rate=PRand(2,5), amp=.8, pan=var([-1,0,1],2)).pause(4,16,12)

d3.ampfadeout(32)

a2.ampfadeout(32)

bpm_to(160,64)

b2 >> blip(chords, dur=clave23, sus=linvar([1,10], 16), oct=6, pan=PWhite(-1,1)).pause(4,16) + P(0,2)
b1 >> blip(chords, dur=cascara, sus=linvar([.3,3],16), oct=4, pan=linvar([-1,1],16)).pause(4,16,8) + P[0, 2, 0, P(0,2)]
c5 >> blip(chords, dur=.25, sus=linvar([.3,3],16), oct=8, pan=linvar([-1,1],16)).pause(4,16,8) + P[0, 2, 0, P(0,2)]

c5.ampfadeout(64)

k2 >> kicker("V.", dur=.5, amp=1, crush=8, bits=4, lpf=linvar([200,1000],32)) #Ah le kick enfin
k2.pause(8,32)


k2.ampfadeout(64)

b1.ampfadeout(32)
b2.ampfadeout(32)

k1.ampfadeout(64)

k1.amplify=0

d3 >> play("<...c...c.><...(...*)><..(i).>", dur=1/4, lpf=800, hpf=200, rate=var([1,1.3]), sample=1)

k4.ampfadeout(32)


d3.sampfadeout(32)


d5 >> kicker("x.")

