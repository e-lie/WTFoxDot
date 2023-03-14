
Clock.clear()

from FoxDot import *
from FoxDot.preset import *

fordrip, gone = add_chains("fordrip1+", "gone1+")
apad, souls = add_chains("apad1+", "souls1")
marimba, vibra = add_chains("marimba1+", "vibra1")
darkpass, hpluck = add_chains("darkpass+", "hpluck1+")
dakeys, padarp = add_chains("dakeys1", "padarp1+")
rdrum, bpiano = add_chains("rdrum1+", "bpiano+")
acidbb, bass303 = add_chains("acidbb", "bass303+")


p1 >> bpiano([0,8,P*(5,3),1,(2,3),P*(5,4)], dur=1, )
p2 >> rdrum([0], dur=[1, .5, 1, .25, .25, .5])

p1 >> bass303(
    [0, 2, 5, 2, -2, 1, 4],
    dur=.5,
    oct=6,
    amp=.8,
    detune=0,
    delay=.4,
    reverb=.3,
    expand=0,
)

p1.dur = var([1, .5, .25], PRand(2,32))

p1.amp = (PWalk()[:20] + 20)/ 20

p1.amp = PWhite(1,.7)

Root.default = var([0,-8,8], [1, 2, 3, 4])

p2.only()

p4 >> blip([0,2,-2,1,3,5,7], dur=[2, 1], amp=PWhite(.7,1)) + [P(0,2), P*(0,4), P(0,1)]

p4.sus=2

p4.oct = [3,5,6]

p4.amplify = 1

d1 >> rdrum([4, 1, 1, 2], amp=1.2, root=0, dur=[1, .5, 1, 1, .25, .25])

d2 >> play("~~([~~]I)")

a = MidiInputHandler(target=ControlTarget(20, 0))

@swim
def pluck(d=0.25):
    D('pluck', midinote=a.get()).out()
    a(pluck, d=0.25)

# Tu déclares un contrôle MIDI (ControlTarget)
midi_in = MidiInHandler(
    target=ControlTarget(control=71, channel=0),
    port=str(config.midi)
)
# Tu l'ajoutes au bowl
bowl.add_handler(midi_in)

# Dans cette fonction on reçoit
@swim
def baba(p=0.5, i=0):
    value = midi_in.get()
    print(value)
    again(baba, p=0.1, i=i+1)

# Et là on ping avec une valeur au pif 
CC(ctrl=71, chan=1, value='50~120')

print(midi_in.get())


@swim
def baba(p=0.5, i=0):
    durr=int(midi_in.get()/16)*0.25
    b1 >> blip(0,dur=durr) + [0,2,-2,4,3]
    again(baba, p=0.1, i=i+1)


d1 >> play("x~")

Clock.clear()

silence()

