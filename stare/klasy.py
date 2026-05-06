class Pojazd:
    kolor = 'biały'

opel = Pojazd()
print(opel.kolor)

class Pojazd:
    def __init__(self, marka, kolor):
        self.marka = marka
        self.kolor = kolor

auto = Pojazd("Kia","czerwony")

print("Pojazd marki:", auto.marka,"ma kolor:",auto.kolor)


