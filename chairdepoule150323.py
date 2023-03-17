Clock.clear()

from FoxDot import *
from FoxDot.preset import *

fordrip, gone = add_chains("fordrip1+", "gone1+")
# apad, souls = add_chains("apad1+", "souls1")
marimba, vibra = add_chains("marimba1+", "vibra1")
# darkpass, hpluck = add_chains("darkpass", "hpluck1")
dakeys, padarp = add_chains("dakeys1", "padarp1+")
rdrum, bpiano = add_chains("rdrum1", "bpiano")
acidbb, bass303 = add_chains("acidbb", "bass303+")


change_bpm(100, True, 0.22)

b1 >> bpiano(0, dur=[.5,.25,.25,.75], amp=PWhite(.7,1)) + (P[0,1,0,0,1,2] + P[P(0,2), P(0,1), P(0,4)] + P(0,12))

b1.oct = [4,5,4,3,6]

Scale.default = Pvar([Scale.minor, Scale.major, Scale.majorPentatonic], 16)

Root.default = var([0,2,3,5,4], 7)

d1 >> play("<~><x..x.>", dur=var([.25, .5, 2]), rate=PWhite(1,2), amp=3, crush=16, bits=4)

bpm_to(40, 32)

# then I played the algodrum code and it was really nice and successfull



