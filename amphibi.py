from animals import animal

class amphibi(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernafas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernafas
    
    def info_amphibi(self):
        super().info_animal(),
        print("Jenis air \t\t\t:", self.jenis_air,
              "\nBerenapas \t\t\t:", self.bernapas)
        
Amphibi = amphibi("katak", "serangga", "dua alam" , "bertelur", "tawar", "kulit dan paru-paru")
Amphibi.info_amphibi()
