class Szamitogep:
    def __init__(self,sor, oprsz, ram):
        adatok = sor.strip().split(";")
        self.oprsz = adatok[0]
        self.ram = adatok[1]