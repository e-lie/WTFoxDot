Clock.clear()

k1 >> play(
    # "X{.xX+}(X.)",
    "+",
    dur=Pvar([1, /3, 1/5], 8),
    output=12,
    sample=1, #PRand(0, 2),
    # rate=linvar([0, 10], 16)
).pause(0, 32)

d1 >> play("+", dur=1, sample=1)

change_bpm(100)

d1 >> play("Xx{x[XX][vv]}", dur=1, amp=[1,.7,.7,.7])
d1 >> play("X", dur=1, amp=[1,.7,.7,.7])
d2 >> play("++[++]", dur=4/3, sample=1, amp=[1,.7,.7])
d2 >> play("+", dur=4/3, sample=1, amp=[1,.7,.7])
d3 >> play("++[**]", dur=4/5, sample=2, amp=[1, .7, .7, .7, .7]), 
d3 >> play("*", dur=4/5, sample=2, amp=[1, .7, .7, .7, .7]), 

b1 >> bbass([0,2,0,0,2,0,0,0,2,-2], dur=var([2/3, 2/5, ], PRand(1,8)), oct=P[3,4,5].stutter(3), amp=PWhite(.8,1.2))

b7 >> blip(0, dur=4/5, amp=PRand([0,1.5,2])/2) + [0,P*(0,4,2),-2,0,P*(0,2,-2)]

b1 + [0, P*(0,2), 2, (0,2)]

Scale.default = Pvar([Scale.minor, Scale.majorPentatonic, Scale.lydian])

g1 >> play("<~><[~.~~.]><xct>", dur=4/3)
g1 >> play("<~>", dur=4/3)
g3 >> play("*iii", dur=1, sample=1)
g4 >> blip([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dur=1/15, sus=.1)


h1 >> play("<~><[(~i)(i~)(i~)(~i)(~i)]>", dur=1).only()
h1 >> play("<+><[-----]>", sample=1, dur=1)
g2 >> play("<o++++><[...]>", dur=4/5, sample=1)

change_bpm(60)

d_all.rate = PWhite(.8,2)

d2 >> play("")

k3.fadeout(32)



k3.stop()

bpm_to(32)

Scale.default = Scale.major

f1 >> bbass(chords, dur=PDur(3,8), oct=3, amp=1) + [0,1,0,2,0,3]

k1.dur = Pvar([PDur(3,8), PDur(5,16), .25])

f1.dur = [.4, .3, .3]

f1.oct=[3,3,4,4,5]

p1 >>  dakeys(
    [0, 2, 5, 2, -2, 1, 4],
    dur=[1, .5],
    oct=[4,5,6],
    amp=.8,
    pad=0,
    modelb=linvar([0, 1], 16),
    pluck=linvar([0, 1], PRand(1, 8)),
    space=linvar([0, 1], PRand(1, 8)),
).sampfadeout(64)



change_bpm(100, True, 0.22)

g1 >> play("i", dur=[.4,.3,.3]).ampfadein(16)

f1.only()
f1.sampfadeout(32)

b1 >> blip(0, dur=cascara, sus=linvar([.3,3],16), oct=(3,6), amp=PWhite(1,2)).pause(4,16,8).mpan(mrot(24))

b2.fadeout(32)

b2 >> blip(0, dur=clave23, sus=linvar([.3,3],16), oct=5, amp=2).pause(4,16,8).mpan(mrot(24))

b2.pan = -1
b1.pan = 1

b1.sampfadeout()

b1.only()

ggg = Group(d1, k4, k1)

ggg.only()

Root.default = var(PTri(6)*2, PRand(1,8))

b1.amp=2

b1 + PWalk()

Scale.default = Scale.majorPentatonic




d1 >> play("+.+++[++]++", sample=1, rate=PWhite(.1,.3), dur=PDur(7,12)*[.4,.3,.3]*4).stop()

k1 >> play("V+", output=12, dur=Pvar([PDur(3,8)/2, .25], 12))

k2 >> play("-[--]", dur=PDur(5,8))

change_bpm(90)

print(PDur(7,12)*P[.4,.3,.3]*4)
print(PDur(7,12)*1.5)


b1 >> blip([0,2,2,0,3], dur=P[2,1,1,2,1,1,1,1]*PDur(3,8)/2, oct=(3,4))