#buatlah class animal parent class. class animal mempunyai properti 4 properti (Name, makanan, hidup, berkembang biak)

class animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print("Nama hewan \t\t\t :", self.name,
                "\nmakanan \t\t\t :", self.makanan,
                "\nhidup \t\t\t\t :", self.hidup,
                "\nberkembang \t\t\t :", self.berkembang_biak)


#hewan = animal("kucing", "daging", "darat", "melahirkan")
#hewan.info_animal()

#membuat minimal 3 class child(amphibi , carnivora , mamalia dll) setiap 