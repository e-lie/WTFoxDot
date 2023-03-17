Clock.clear()

from FoxDot import *
from FoxDot.preset import *

# fordrip, gone = add_chains("fordrip1+", "gone1+")
apad, souls = add_chains("apad1+", "souls1")
marimba, vibra = add_chains("marimba1+", "vibra1")
# darkpass, hpluck = add_chains("darkpass", "hpluck1")
dakeys, padarp = add_chains("dakeys1", "padarp1+")
rdrum, bpiano = add_chains("rdrum1", "bpiano")
acidbb, bass303 = add_chains("acidbb", "bass303+")


Scale.default = Scale.lydianMinor
Scale.default = Scale.major

chords = var([0,2,3,0,5,4],8)

Clock.bpm = linvar([120,115,122],[15,27])

b1 >> bpiano(
    chords + [0, 2, 1, 0],
    dur=Pvar([[.5, .25, .25], 1 / 3, .25, [1 / 3]], [8, 2, 4, 2]),
    amp=(P[.8, .9, .7, .9, .8] + PWhite(.1,.2)[:17]) * linvar([.8,1], PRand(1,4)[:17]*4 ),
    oct=var([5,4,5,6], [.5,1,2]),
) 

b1 + P[(0, 2), (3), P*(0, 4)]


b2 >> bpiano(
    chords,
    dur=2,
    # dur=.25,
    amp=(P[.8, .9, .7, .9, .8] + PWhite(.1,.2)[:15]) * linvar([.8,1], PRand(1,4)[:17]*4),
    # oct=var([4,3], [4]),
    oct=3,
) + [0,2,5,2,4]


d1 >> play("<c..c...c..c.c...><[--]-><(vv[vv].).>", rate=PWhite(.5,1), output=12, amp=.8)
