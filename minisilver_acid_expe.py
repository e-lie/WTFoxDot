Clock.clear()

from FoxDot import *
from FoxDot.preset import *

minisilver, fordrip, gone = add_chains("bass/minisilver_1", "noise/fordrip_1", "pads/gone_1")

Scale.default = Scale.minor
Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)

bb >> minisilver(
    # [0, 0, 2, -2],
    Pvar([[0, 0, 2, -2],[0,0,2,4],[0,2,0,-2]],4),
    dur=.25,
    # dur=[.25,.5,.25,.25],
    # dur=var([.25,1/3],[4,2]),
    # dur=[.4,.3,.3],
    # sus=[.2,.5,.2,.2,.5],
    sus=linvar([.1,.3,.1,.4,.1,.26],1),
    # oct=var([3,4], PRand(1,2)),
    # oct=3,
    oct=var([3,4,3,5], PRand(1,2)),
    # cutoff=.2,
    # reso=.3,
    cutoff=linvar([0, 1], PRand(2,32)),
    reso=linvar([.4, .8], 12)
)#.fadein(32, ivol=.5)

bb.sampfadeout(16)

Clock.bpm=110

d1 >> play("<X(...[.X])>", sample=2, amp=1,)
d1 >> play("<X~>", sample=2, amp=1, lpf=10000, rate=var([1,.8,1.1,1.2], 2))
d1 >> play("<X~><.(..V[.X])>", sample=2, amp=1, lpf=10000, rate=var([1,.8,1.1,1.2], 2))

a4 >> gone([0], dur=4, body=0, arp=0, pitch=0, oct=3, dull=linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4)))
a4.fadein(32)