"""CREATING A CLASS AND DEFINING IT"""
class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print('Sukurtas auto', metai, modelis, kuro_tipas)

"""ENHANCING CLASS WITH DEFINITIONS"""
    def automobilis_vaziuoja(self):
        print("Važiuoja")

    def automobilis_stovi(self):
        print("Stovi")

    def auto_degalu_pildymas(self):
        print("Degalai įpilti")