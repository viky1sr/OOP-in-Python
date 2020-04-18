class Hero:

    # private class Variable
    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method hanya kusus Object
    def getJumlah(self):
        return Hero.__jumlah

    # method hanya kusus Class
    def getJumlah1():
        return Hero.__jumlah

    # method static (decorator) bisa di gunakan di Class & Object
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # method hanya kusus Object & Class Tetapi mengunakan Class bukan Name or Object
    # ketika di ubah nama class tidak perlu mengubah lagi hanay mengunakan (cls)
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

#     ini adalah object semua di python adalah Object
sniper = Hero('Sniper')

print(Hero.getJumlah3())
