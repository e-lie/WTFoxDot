Clock.clear()

from FoxDot import *
from FoxDot.preset import *

fordrip, gone = add_chains("fordrip1+", "gone1+")
apad, souls = add_chains("apad1+", "souls1")
marimba, vibra = add_chains("marimba1+", "vibra1")
darkpass, hpluck = add_chains("darkpass", "hpluck1")
dakeys, padarp = add_chains("dakeys1", "padarp1+")
rdrum, bpiano = add_chains("rdrum1", "bpiano")
acidbb, bass303 = add_chains("acidbb", "bass303+")



b1 >> blip(0, dur=.5).mpan(mrot(6))
b2 >> blip(4, dur=3/5).mpan(1)


bb >> play("<x>", dur=PDur(3,8)).mpan(0)

print(PDur(7,12))

p1 = Pattern()

Clock.bpm = 120

