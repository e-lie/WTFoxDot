
################################################################

Root.default = 0
Root.default = var(PTri(6), [16]*6+[inf], start=Clock.mod(4))
Root.default = var(PTri(12), .25)

Scale.default = Pvar([Scale.minor, Scale.major, Scale.minor, Scale.majorPentatonic, Scale.major], PRand(1,4)[:32]*4)
Scale.default = Scale.minor
Scale.default = Scale.majorPentatonic

################################################################



################################################################



################################################################