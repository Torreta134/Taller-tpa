class Divisa:
    def __init__(self, ndivisa, vdivisa, vequivalente):
        self.ndivisa = ndivisa
        self.vdivisa = vdivisa
        self.vequivalente = vequivalente

    def equivalencia(self):
        
        valorfinal = (self.vdivisa/self.vequivalente)
        return valorfinal
