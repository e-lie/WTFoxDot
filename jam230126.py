Clock.clear()

from FoxDot import *
from FoxDot.preset import *

fordrip, gone = add_chains("fordrip1", "gone1")
apad, souls = add_chains("apad1", "souls1")
marimba, vibra = add_chains("marimba1", "vibra1")
darkpass, hpluck = add_chains("darkpass", "hpluck1")
dakeys, padarp = add_chains("dakeys1", "padarp1")
rdrum, bpiano = add_chains("rdrum1", "bpiano")
acidbb, bass303 = add_chains("acidbb", "bass303")

fordrip, gone = add_chains("fordrip1+", "gone1+")
apad, souls = add_chains("apad1+", "souls1+")
marimba, vibra = add_chains("marimba1+", "vibra1+")
darkpass, hpluck = add_chains("darkpass+", "hpluck1+")
dakeys, padarp = add_chains("dakeys1+", "padarp1+")
rdrum, bpiano = add_chains("rdrum1+", "bpiano+")
acidbb, bass303 = add_chains("acidbb+", "bass303+")

d1 >> darkpass([0,2], oct=3, rm=linvar([0,1],8), detune=linvar([0,1], 17), dur=2).span(srot(16))

d2 >> bass303(0, dur=[.25,.5], sus=[.1,.3], lpf_freq=linvar([.3,.8],16)).span(srot(12))

tt >> blip(0, dur=.5).mpan(mrot(6))

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.majorPentatonic
Scale.default = Scale.minor

Root.default = var([0,2,5,4], 16)
Root.default = var(PTri(12), 4)
Root.default = var([0,2], 32)
Root.default = 0

b1 >> blip([0,0,P*(0,0)], oct=PTri(4,7).stutter(2), dur=[.4,.3,.3], sus=var([.2,.5,2])).mpan(mrot(6)) + [0,2,0,0,-2,0,4]
b1 >> blip([0,0,P*(0,0)], oct=PTri(4,7).stutter(2), dur=[.4,.3,.3], sus=var([.2,.5,2])) + [0,2,0,0,-2,0,4]
b1 >> blip([0,0,P*(0,0)], oct=PTri(4,7).stutter(2), dur=Pvar([[.7,.3],[.4,.3,.3], [.5,.25,.25]]), sus=var([.2,.5,2])) + [0,2,0,0,-2,0,4]


tt >> blip(dur=.5, sus=.8).mpan([0,1,2,3,4,5])
t2 >> play("{x.xv.[xx]}.", rate=PWhite(.8,1.3), sample=0, dur=.5).mpan((0,1)).pause(16,32)

d2 >> play("<(v.)-->", dur=[.4,.3,.3], output=12, room2=10, rate=PWhite(1,4))

Clock.bpm=160

m1 >> vibra([0,0,1,3,5,2,-2,4], dur=[.25,.5], oct=P[5,6,4,7,6].stutter(2), vol=.8).span(srot(32))
m2 >> marimba([0,0,1,3,5,2,-2,4], dur=[.5,.75], oct=P[3,4,3,5].stutter(2), vol=.9).span(srot(24))
m3 >> blip([0,0,1,3,5,2,-2,4], dur=[.25,.5,.25], oct=P[4,7,5].stutter(2), sus=.5, amp=1.3, pan=PWhite(-.8,.8)).mpan(PRand(0,5))
d1 >> play("x{......V}x{.[xx]x}{.x.[VV].}", amp=PWhite(.9,1.2), output=12, lpf=300)
d1 >> play("x{......V}x{.[xx]x}{.x.[VV].}", amp=PWhite(.9,1.2), lpf=300).mpan(PRand(0,5))

a1 >> padarp(
    [0, 2],
    dur=[2,1.2,1.8],
    oct=6,
    amp=.8,
    detune=sinvar([0,1], PWhite(.2,3)[:16]),
    delay=1,
    reverb=1,
    expand=linvar([0, 1], 16),
).span(srot(12))

a2 >> padarp(
    [0, 2,0,5],
    # dur=[1.1,.9],
    dur=.5,
    oct= 4,
    amp=.8,
    # detune=sinvar([0,1], PWhite(.2,3)[:16]),
    delay=0,
    verb=.5,
    vol=.7,
    # expand=linvar([0, 1], 16),
).span(srot(12))

k1 >> play("c.{..c+}{vccc+}(v{vv+cc})", dur=[.4,.3,.3]).pause(0,24).mpan(PRand(0,1))
k2 >> play("{V[VV].x}{++[++]I}", output=12).pause(6,24).only()

b1 >> marimba(
    [0, 2, 1, -2],
    dur=[.25, .25, .3, .4, .4],
    sus=1,
    oct=P[3, 4, 6].stutter(8),
    amp=PWalk(start=30, seed=13)[:30] / 30
).span(srot(16))

k1.fadeout(32)

b1 >> marimba([0,2,1,-2], dur=[.25,.25,.3,.4,.4], sus=1, oct=P[3,4,6].stutter(8), amp=PWalk(start=30, seed=13)[:30]/30)
b2 >> marimba([4,4,5,6], dur=[.5,.3,.4,.4], sus=1, oct=P[4,5,7].stutter(7), amp=PWalk(start=30, seed=11)[:30]/30)

b1.stop()
b2.stop()

b2 >> marimba(
    [4, 4, 5, 6],
    dur=.25,
    sus=1,
    oct=P[4, 5, 7].stutter(7),
    amp=PWalk(start=30, seed=11)[:30] / 30
).span(srot(32))

change_bpm(110, True, 0.22)
change_bpm(100, True, 0.22)
change_bpm(200, True, 0.22)
bpm_to(110)

Clock.bpm = linvar([100,98,100,102], PRand(32,64)[:16])
Clock.bpm = linvar(P[100,90,100,110]*2, PRand(32,64)[:16])

a2.stop()


# fix lfo snippet
# fix padarp verb
# fix padard, dakeys etc draft
# add pan back to parameters !


print(PWalk(start=10)[:16]/10)

b1 >> blip(
    PWalk(start=0, seed=10)[:64] * 2,
    # dur=.25,
    dur=Pvar([P[.45, .55, .5, .5, .48, .52]/2, P[1 / 3, 2 / 3]/2], [12, 4]),
    sus=2,
    amp=PWalk(start=30, seed=10)[:64] / 30 + .5,
    oct=var([4,5,6,7,6,5],8),
    # pan=var([-1,.5,0,1,-.5], PRand(1,4)/2)
).mpan(PRand(0,5)) + [0, 0, 0, 1, 1, 0, -2, 0, 1]


b2 >> pluck(
    PWalk(start=0, seed=10)[:64] * 2,
    dur=[.5,.25],
    sus=2,
    amp=PWalk(start=30, seed=10)[:64] / 30 + .9,
    oct=var([4,5],8),
    pan=var([-1,.5,0,1,-.5], PRand(1,4)/2),
    lpf=500
).mpan(mrot(12)) + [0, 0, 1, -2, 0, 1]

d1 >> play(
    '<-{-[--]}{.-}><.(V++)>',
    sample=2,
    dur=Pvar([[.45, .55, .5, .5, .48, .52], [1 / 3, 2 / 3]], [12, 4]),
    output=12,
    # pan=var([-1,,..5,0,1,-.5], PRand(1,4)/2),
    pan=0,
).only()

k1 >> play("V.", output=12, lpf=500, rate=(0,linvar([1,1.5]))).pause(8,32)
k2 >> play(".(---[++])", sample=1, rate=PWhite(1,2), amp=3).mpan(mrot(16))

b1 >> blip([0,2,0,0,-2,2], dur=[.25,.5], oct=6, amp=[1,0,0,0,1,0]).mpan(0)
b2 >> blip([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,1,0,0,0,0]).mpan(1)
b2 >> marimba([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,1,0,0,0,0]).span(srot(16))
b3 >> blip([0,2,0,0,-2,2], dur=.5, oct=3, amp=[0,0,1,0,0,0]).mpan(2)
b4 >> blip([0,2,0,0,-2,2], dur=[.75,.5], oct=7, amp=[0,1,0,1,0,0]).mpan(3).pause(4,24,12)
b5 >> blip([0,2,0,0,-2,2], dur=.5, oct=5, amp=[0,0,0,0,1,0]).mpan(4)
b6 >> blip([0,2,0,0,-2,2], dur=.5, oct=4, amp=[0,0,1,0,0,1]).mpan(5).pause(4,16)

b_all.sus=linvar([.1,2],32)




b1 >> space(0, dur=.5, sus=[1], amp=[.5,1.2,1,2], oct=[4,4,5,5,3,4,5]).pause(8,32) + [P*(0,2),2,0,P*(0,5),0,2,-2]
b2 >> blip([0,2], dur=.5, sus=[2], amp=[.5,1.2,1,2], oct=[7,8,6]).pause(8,32) + [P*(0,2),2,0,P*(0,5),0,-2]


d1 >> play("v.[vv].", sample=0)

d2 >> play("--.{[++]i}", sample=1, amp=PWhite(.8,1.5))