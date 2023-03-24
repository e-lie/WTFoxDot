

##################################"

Clock.bpm = 90 

tt >> lavitar([0,2,0,-2], vol=.7, dur=.25, cutoff=linvar([.2,1],16), reso=linvar([.5,1],12), oct=[3,4,5])
t2 >> blip([0,2,0,-2], dur=.25, cutoff=linvar([.2,1],16), reso=linvar([.5,1],12), oct=[5,6,7])

d1 >> play("<v.><x(**[**][.O])>", )


Root.default = var([0,1,2], PRand([1,8]))

a1 >> apad(
    [0, 4, -2],
    dur=PRand(2, 8),
    vol=1,
    thick_thin=0,
    oct=5,
)
a1.fadein(16)