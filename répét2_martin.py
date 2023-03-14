
Clock.clear()

Clock.bpm = 70
Clock.bpm = linvar([70, 100], [32,inf], start=Clock.mod(4))

Clock.bpm = linvar([160,120], [32,inf], start=Clock.mod(4))


d1 >> blip(0, dur=[2/5,3/5], sus=1, amp=PRand(0,1), pan=1, oct=(2,3,4)).every(3,"stutter",2).fadein(16)

b1 >> bbass(0, dur=var([1/4,2],[2,7,3]), sus=4, amp=1, pan=1, oct=(P[3,4,5,6].stutter(3))).every(3,"stutter",2).fadeout(16)

k1 >> play(".{.v[vv]}", dur=var([1/3,1/2], 8), pan=1, rate=(1,PRand([3,4,5,6])), crush=16, bits=4, amp=0)

cc >> play("t", dur=1, pan=-1, amp=2)


cc >> play("c", dur=1, pan=-1)
cc >> play("c", dur=1, pan=-1)


# 1 - pechu pour annoncer

# 2 - on repart calme et lent (pad + nappes) = + de place pour jongler avec les subdivision

# 3 - 

# 4 - pechu rapide


- Martin aime bien faire des cymbales que je peux complémenter avec un kick
  - échanger kick aigu toute les 4 mesures

- globalement on  dire 