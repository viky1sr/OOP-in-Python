class Hero:

    # ini adalah Getter dan Setter Bawaan dari Python dengan mengunakan @property

    def __init__(self,name ,health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    @property
    def info(self):
        return "name : {} \n\thealth : {}".format(self.__name,self.__health)

    @property
    def attack(self):
        pass

    @attack.getter
    def attack(self):
        return self.__attack

    # untk mengeset (mengubah) value menjadi simple Variable tidak mengunakan method
    @attack.setter
    def attack(self,input):
        self.__attack = input

    @attack.deleter
    def attack(self):
        print('Attack berhasil di delete')
        self.__attack = None

mirana = Hero('Mirana', 150, 25)
print(mirana.attack)
mirana.attack = 50
print(mirana.attack)
print('Delete attack')
del mirana.attack
print(mirana.__dict__)