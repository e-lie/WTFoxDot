Clock.clear()

from FoxDot import *
from FoxDot.preset import *

a2 >> apad(0, dur=.5)

a2.attack=0

a2.oct=PRand(3,6)

a3 >> gone(0)

a3.pitch = linvar([0,1,.4,.8,0,.6],PRand(2,24), start=Clock.mod(4))

a3.stop()

b2 >> play('[xx]1.2VV', dur=.5, rate=(.1,1), crush=0, bits=6, room2=5).pause(24,32)

b2.stop()

k1 >> kicker("v(...v)XX", lpf=400, dur=.25).pause(8,32)
d1 >> play("{Ooo[ii]}", lpf=20000, dur=PSum(3,2), amp=3)

b2 >> blip(0, dur=[.25,.25,1,5], sus=PWhite(.1,2), oct=PRand(3,4))
b1 >> blip(0, dur=[.25,.25,1,5], sus=PWhite(.1,2), oct=PRand(7,8))

b1 >> blip(0, dur=[.25], sus=PWhite(.1,2), oct=linvar([3,7],16))
b1 >> blip(0, dur=PSum(3,2), sus=PWhite(.1,2), oct=linvar([3,7],16))

b3 >> gone([0,1,2],oct=7, dur=.5)
b3.pitch = 0
b3.fadein(16)

a2.fadeout(32)

bpm_to(90, 32)

change_bpm(120)


b4 >> blip(0, dur=.25, sus=linvar([.2,2], 32)) + [0,2,4,-2]
b5 >> blip(0, dur=.125, sus=linvar([.2,2], 32), oct=[3,4,3]) + P[0,2,4,5,7]

b5 >> blip(0, oct=(3,4,7), sus=2, amp=3, dur=.5) + PRand([0,2,-2])
b5.stop()

Scale.default = Pvar([Scale.major, Scale.minor, Scale.chromatic])
