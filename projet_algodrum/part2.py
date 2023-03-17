Clock.clear()

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 5, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.majorPentatonic

#############################################################

change_bpm(100, True, 0.22)

bpm_to(100, 16)

cc >> play("<(t----)..>", dur=.25, output=14)

m1 >> marimba("a", oct=P(3,4,5), amp=linvar([.1,.9],16, bus2=.5), dur=.125)

m1 >> marimba(
    "abfff...ffbafff",
    oct=([2, 5], [3, 4, 5], 6),
    # oct=4,
    # amp=linvar([.3, .9], 16),
    amp=.5,
    # dur=Pvar([.125, cascara / 2], [8, 4])
    dur=.25,
    vol=1.2,
)

a4.fadeout(16)

m1.degree = "ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]"

m1 + (0,2)

m1 >> marimba("ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]", oct=3, amp=linvar([.1,.9],16), vol=1.2, dur=.5)

###############################################################

m3 >> vibra("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=[2,3,5], amp=linvar([.5,.9],7), dur=cascara)

Root.default = var([0,2,-2],15)

m1.degree = [0,2,4,2,-2]

m3.degree = [0,2,4,2,-2]

m3.fadeout(32)

m3.pause(5,15)

m3.oct = P[3,4,5] + P(0,2)

m1.pause(3,15, 5)

m3.only()

m1.fadeout(64)

m1.stop

###############################################################

a1 >> apad(
    # [0, 4, -2],
    [0],
    dur=PRand(1,3)[:15]*2.5,
    vol=1.1,
    attack=.4,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
)
a1.fadein(32)

a1 + 12

a1.oct=3

a1.stop()

###############################################################

k1 >> play("X{.xX+}(X.)", dur=Pvar([.25, 1.25],10), output=12, rate=2)

k1.only()

k1.rate = var([1,3,1,2], 5)

k1.dur = 1.25

b1 >> bbass([0], dur=[1.25, .5, .75], output=12, oct=(3,4), amp=1.5) + [0,0,2,1,0]

b1.fadeout()

b1 >> bbass([0], dur=var([.25,.5],5), output=12, oct=3)


###### NOtes

- début part2 : mettre le click seulement pour un debut solo martin puis entrer avec nappes de marimba => attendre le signe
- fin part2 : ramener un truc en 4 binaire par dessus + entrer le kick part1 binaire
- pont house toujours à 100 binaire
- couper kick, bien mettre click puis accélération 130 avec juste synthé et drum de martin
