from FoxDot import *
from FoxDot.preset import *

acidbb, dakeys = add_chains("acidbb","dakeys1")

Clock.clear()

Root.default = var([0,5,4,0,2], [4,8])

Scale.default = Pvar([Scale.major, Scale.minor, Scale.aeolian], [4,8])

Clock.bpm = linvar([70,130], 4)

b1 >> acidbb(
    [0,2,2,2],
    # var([0, 5, 3, 2], [1, .5]),
    # dur=Pvar([.25, .5, [.25, .5]]),
    dur=.25,
    # oct=var([3, 4, 5], .5),
    oct=6,
    # sus=var([.2, .5, 2], 1),
    pan=P[-1, 0, 1].stutter(2),
    cutoff=linvar([0,1], 4),
    # pad=0,
    sus=b1.dur/2
)

tt >> blip([0,2,2,2], dur=1, oct=7)

print(tt.metro.latency)

tt.metro.latency = .5
Clock.midi_nudge = -.235
Clock.bpm=70

b2 >> blip(
    # 0,
    var([0, 5, 3, 2], [1, .5, .5]),
    dur=Pvar([.25, .5, [.25, .5]], 3),
    oct=var([4, 5, 6], .5),
    sus=var([.2, .5, 2], 1),
    pan=P[-1, 0, 1].stutter(2)
)

b1.always_on = True


b2.only()

b3 >> bbass(
    var([0, 5, 3, 2], [1, .5, .5]),
    dur=[1,2],
    oct=3,
    amp=1.5,
)

d1 >> play(
    "x{X..[vx]}(-~)",
    room2=3,
    pan=P[-1, (-1, 1), 0, (0, 1)],
    dur=Pvar([.25, .5, [.25, .5]]),
    rate=PWhite(1, 1.5),
    sample=var([0,2,3],[1,3,4,2])
)

b1 >> blip(0, dur=.25, oct=var([5,6],16), sus=linvar([0.1, 2], 32)) + [0,2,-2,5,2]

k1 >> play("<(VVV(V[VV]V[.V])).>", amp=1, lpf=300, output=12, pan=-.2, sample=var([0,2],64))
d2 >> play("<-[--]-><~..*.>", rate=linvar([1.5, 2], 32), pan=.4, amp=linvar([1.5, 2], 32), crush=linvar([0,1,6], [16,16,16]), bits=4)


Clock.bpm=130