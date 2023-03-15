
Clock.clear()

Root.default = var([0,1,2], PRand([1,8]))
Root.default = 0
Root.default = var(PTri(12), 4, start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor

#############################################################

change_bpm(70, True, 0.22)

d1 >> play("<(V----)..>", dur=.125)

m1 >> marimba("a", oct=P(3,4,5), amp=linvar([.1,.9],16, bus2=.5), dur=.125)

m1 >> marimba(
    "abfff...ffbafff",
    oct=([2, 5], [3, 4, 5], 7),
    amp=linvar([.3, .9], 16),
    dur=Pvar([.125, cascara / 2], [8, 4])
)


m1 >> marimba("ab[d][cc]a.........b[aaaa]([c]a[cccc]d)[ff]", oct=3, amp=linvar([.1,.9],16, bus2=.5, vol=1.2, dur=.5), dur=.125).humz().span(srot(64))

###############################################################

m3 >> vibra("ab[d][cc]a.b[aaaa]([cccc]d)[ff]", oct=[2,3,5], amp=linvar([.5,.9],7), dur=cascara, bus4=.5)

Root.default = var([0,2,12])

m1.degree = [0,2,4,2,-2]

m3.degree = [0,2,4,2,-2]

###############################################################

p1 >> souls(
    [0, 2, 5, 2, -2, 1, 4],
    dur=.5,
    oct=6,
    amp=.8,
    rot=0,
    rumor=0,
    linger=0,
    burn=0,
)

###############################################################