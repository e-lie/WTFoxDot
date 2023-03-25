Clock.clear()

Root.default = 0
Root.default = var(PTri(6)*2, 15*.25, start=Clock.mod(3.75))
Root.default = var(PTri(12), .25)
Root.default = var(PTri(6)*2, .75)


Scale.default = Pvar([Scale.majorPentatonic, Scale.minor, Scale.lydian, Scale.aeolian], 15*.25)
Scale.default = Scale.majorPentatonic
Scale.default = Scale.minor
Scale.default = Scale.lydian
Scale.default = Scale.aeolian

#############################################################

Clock.meter = (15*.25,1)

Clock.bpm=100

# cc >> play("<(X----)-+>", dur=.25, output=14, amp=6)
cc >> play("<(t----)..>", dur=.25, output=14, amp=3)
cc.always_on = True


mmelody = P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5]
m1 >> marimba(
    # "abfff...ffbafff",
    mmelody,
    # P[-12,0,-2,0,5,-2,0,0,-2,5,0,-2,0,0,5] + P(0,2),
    # P[12,2,4,2,-2].stutter(3).shuffle(),
    # amplify=var([1,0,1], [1,.75,2,2,.5,1.25]),
    amplify=1,
    # oct=6,
    oct=[4,5,6,5,4],
    # oct=([2, 5], [3, 4, 5], 6),
    amp=.8,
    # amp=linvar([.75, .45], 15*.25, start=Clock.mod(4)),
    # dur=Pvar([.25, cascara], [8, 4]),
    sus=.1,
    dur=.25,
    vol=1,
)

###############################################################

m3 >> lavitar(
    # "ab[d][cc]a1b[aaaa]([cccc]d)[ff]",
    # P[12,2,4,2,-2].stutter(3).shuffle(),
    P[12,2,4,2,-2].stutter(3),
    # P[12,2,4,2,-2].stutter(3) + P(0,m1.degree),
    # oct=P[7,3,5,4,3],
    oct=P[7,3,5,4,3] + P(0,m1.oct),
    # amp=linvar([.5, .9], 7),
    amp=.7,
    dur=.25,
    vol=1,
    # cutoff=.1,
    level=1,
    cutoff=linvar([.1,1], [15*.25*15,inf], start=Clock.mod(15*.25)),
    # cutoff=linvar([1,.3], [15*.25*15,inf], start=Clock.mod(15*.25)),
    reso=1,
)
m3.fadein(15*.25*3)

m3

m3.only()

m1.fadein(15*.25*72)

m1.fadeout(15*.25*5)

m3.only()

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
    P[0, 4, -2] + (0,2),
    # [0],
    dur=PRand(1,3)[:15]*2.5,
    vol=1.1,
    attack=.4,
    space=0,
    detail=0,
    thick_thin=0,
    oct=5,
)
# a1.fadein(15*.25*9)

a1.space=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))
a1.thick_thin=linvar([0,1,.4,.8,0,.6], PRand(2,24), start=Clock.mod(4))
a1.detail=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a1 + (0,2)

a1.fadeout(15*.25)


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
    room2=.3,
    amp=1.5,
    lpf=400,
)
# k1.fadein(15*.25*3)
k1.fadeout(15*.25*3)

k1.only()

k1.rate = var([1,3,1,2], 5)

k1.dur = 1.25

b1 >> padarp(
    # [0],
    P[0] + [0,0,2,-2,0],
    # dur=[1.25, .5, .75],
    dur=[1.25, .5, .75, .5, .75],
    output=12,
    oct=(3,4),
    amp=1.5,
    # expand=1,
    expand=linvar([0,1], [32,inf], start=Clock.mod(4)),
    verb=0,
    detune=1,
    delay=0,
)
# b1.fadein(15*.25*3)

m3.fadeout()

m3.fadeout(15*.25*3, ivol=1, fvol=.5)
m3.fadein(15*.25*3,ivol=.5, fvol=1)








##### truc en binaire

s1 >> pharao(
    [0],
    # mmelody,
    dur=[.5, .25, .25],
    oct=5,
    amp=P[.8, .7, .8, 1.1] * 1.5,
    sus=s1.dur + 0.2,
    output=12,
    # cutoff=.06,
    cutoff=linvar([.06,.5], [15*.25*15,inf], start=Clock.mod(15*.25)),
) + P(0, 2)

s1.only()

s1.sampfadeout(64)

s1.only()

s1.stop()