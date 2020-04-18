class Hero:

    def __init__(self,name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_lawan ):
        print(self.name + ' di serang ' + lawan.name)
        attack_diterima = attack_lawan/self.armor
        print('serangan di terima : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisah ' + str(self.health))
        if self.health <= mati :
            print('Anda telah di bunuh oleh ' + lawan.name)

mati = 0

mirana = Hero('Mirana', 100 , 100 , 2)
dr = Hero('Drow Ranger', 100 , 100 , 1)

mirana.serang(dr)
print('\n')
dr.serang(mirana)
