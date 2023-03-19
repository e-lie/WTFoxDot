Clock.clear()

Root.default = 0
Root.default = var(PTri(6)*2, 15*.25, start=Clock.mod(3.75))
Root.default = var(PTri(12), .25)
Scale.default = Pvar([Scale.majorPentatonic, Scale.minor, Scale.lydian, Scale.aeolian], 15*.25)

Scale.default = Scale.majorPentatonic
Scale.default = Scale.minor
Scale.default = Scale.lydian
Scale.default = Scale.aeolian

#############################################################

change_bpm(100, True, 0.22)

Clock.meter = (15,16)

# cc >> play("<(X----)-+>", dur=.25, output=14, amp=6)
cc >> play("<(t----)..>", dur=.25, output=14, amp=6)

m1 >> marimba(
    # "abfff...ffbafff",
    # P[0,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5].rotate(6),
    P[0,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5].rotate(6) + [0,1,-1,2],
    # P[0,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5].rotate(6) + P(0,2),
    # P[12,2,4,2,-2].stutter(3).shuffle(),
    amplify=var([1,0,1], [1,.75,2,2,.5,1.25]),
    # amplify=1,
    oct=6,
    # oct=([2, 5], [3, 4, 5], 6),
    amp=.8,
    # amp=linvar([.75, .45], 15*.25, start=Clock.mod(4)),
    # dur=Pvar([.25, cascara], [8, 4]),
    sus=.1,
    dur=.25,
    vol=1.2,
) 

m1.degree = "ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]"

m1 + (0,2)

m1 >> marimba("ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]", oct=3, amp=linvar([.1,.9],16), vol=1, dur=.5)

m1.oct = (var([4,5,4,3],5) + 6)

###############################################################

m3 >> vibra("ab[d][cc]a1b[aaaa]([cccc]d)[ff]", oct=[2,3,5], amp=linvar([.5,.9],7), dur=cascara, vol=1).fadein()

Root.default = var([0,2,-2],15)

m1.vol=.9

m1.degree = P[12,2,4,2,-2].stutter(3).shuffle()
m1.amplify = var([1,0,1], [1,.75,2,2,.5,1.25])

m3.degree + (0,2)

m3.degree = [0,2,4,2,-2,4]
m3.degree = var(P[0,2,5],1.25) + (0,2)

m3.only()

m3.fadeout(32)

m3.only()

m3.pause(5,15)

m3.oct = P[3,4,5] + P(0,2)

m1.pause(3,15, 5)

m3.only()

m1.fadeout(64)

m1.stop()

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

a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
a1.detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a1 + (0,2)


a1.oct=3

a1.stop()

###############################################################

k1 >> play(
    # "X(x.)",
    "X{.xX+}(X.)",
    dur=var([.25, .75],[15*0.25*2]),
    output=12,
    rate=1,
    pdb=2,
    sample=2,
    room2=5,
    amp=1.5,
    lpf=400,
)#.fadein(24)

k1.only()

k1.rate = var([1,3,1,2], 5)

k1.dur = 1.25

b1 >> padarp(
    # [0],
    # P[0] + [0,0,2,-2,0],
    # dur=[1.25, .5, .75],
    dur=[1.25, .5, .75, .5, .75],
    output=12,
    oct=(3,4,6),
    amp=1.5,
    release=0,
    reverb=1
)

m3.fadeout(fvol=.5)
m1.fadeout(fvol=.5)


m1.oct=6
m3.oct=7


b1.dur=P[.5].stutter(7)|[.25]

b1.reverb = 1
b1.drive = 0
b1.width = 0
b1.release = 0

b1.drive = linvar([0,1], 15*.25*3, start=Clock.mod(4))
b1.width = linvar([0,1], 15*.25*2, start=Clock.mod(4))
b1.release = linvar([0,1], 15*.25, start=Clock.mod(4))


b1.only()

b1.fadeout()

b1 >> bbass([0], dur=var([.25,.5],5), output=12, oct=3)


##### truc en binaire

s1 >> bbass([0], dur=[.5,.25,.25], oct=5, amp=P[.8,.7,.8,1.1]*1.5, sus=s1.dur+0.2, output=12) # + P(0,2)

s1.sampfadeout(32)


###### NOtes

- début part2 : mettre le click seulement pour un debut solo martin puis entrer avec nappes de marimba => attendre le signe
- fin part2 : ramener un truc en 4 binaire par dessus + entrer le kick part1 binaire
- pont house toujours à 100 binaire
- couper kick, bien mettre click puis accélération 130 avec juste synthé et drum de martin
