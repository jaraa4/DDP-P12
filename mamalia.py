from animals import animal

class mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit
    def info_mamalia(self):
        super().info_animal(),
        print("name \t\t\t :" , self.name,
                "makanan \t\t :" , self.makanan,
                "hidup \t\t :" , self.hidup,
                "berkembang biak \t :", self.berkembang_biak,
                "ukuran tubuh \t :" , self.ukuran_tubuh,
                "jenis kulit \t :" , self.jenis_kulit)

Gajah = mamalia("gajah", "tumbuhan", "darat", "melahirkan", "kecil", "berbulu")
Gajah.info_mamalia()