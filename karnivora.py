from animals import animal

class karnivora(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_gigi, jenis_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_gigi = jenis_gigi
        self.jenis_tubuh = jenis_tubuh
    def info_karnivora(self):
        super().info_animal(),
        print("jenis_gigi \t\t\t: ", self.jenis_gigi,
              "\njenis_tubuh \t\t\t: ", self.jenis_tubuh)
Harimau = karnivora("harimau", "daging", "darat", "melahirkan", "taring", "berotot")
Harimau.info_karnivora()