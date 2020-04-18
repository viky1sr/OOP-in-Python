class Hero:
    # class Variable (Static)
    jumlah_hero = 0
    # magic keyword def __init__(self,value)
    def __init__(self,name,health,damega):
        # instance variable
        self.name = name
        self.health = health
        self.damega = damega
        Hero.jumlah_hero += 1

        # void function (method tanpa return)
        def siapa(self):
            print('My name is: ' + self.name)

        def healthUp(self,up):
            self.health += up

hero1 = Hero('Mirana', 570, 65)
hero2 = Hero('Sven', 770, 85)
# __dict__ untuk mengabil semua value

hero1.siapa()
hero1.healthUp(10)

print(hero1.health)

