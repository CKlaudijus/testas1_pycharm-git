"""CREATING A CLASS AND DEFINING IT"""
class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print('Sukurtas auto', metai, modelis, kuro_tipas)