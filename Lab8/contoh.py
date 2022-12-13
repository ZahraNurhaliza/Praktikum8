class person():
    def __init__(selfself, nim, nama):
        print("construct", nama)
        self.nama = nama
        self.__umur = 0

    @property
    def umur(self):
        return self.__umur
    @umur.setter
    def umur(self, value):
        self.__umur = self.__(value)

    def __cek(self, x):
        return x in range(20, 30, 1)

    def cetak (self):
        print(self.nama, self.__umur, sep=", ")

class Mahasiswa(person):
        def __init__(self, name, nim ):         # overriding construct
            print("Construct class Mahasiswa")
            Person.__init__(self, nama)                    # call parent construct
            self.nim = nim

        # overriding method
        def cetak(self):
            print(self.nom, end =", ")
            person.cetak(self)                          # call parent method

ob1 = person()
ob1.nama = "Riko"
ob1.umur = 20
ob1.cetak()

ob2 = person("Dika")
ob2.nama = "Dika Andara"
ob2.umur = 34
ob2.cetak()

print(type(ob1))
print(type(ob2))