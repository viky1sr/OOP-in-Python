class Dota2:

    def __init__(self,name,health,atp):
        self.__name = name
        self.__health = health
        self.__atp = atp


    # getter
    def getName(self):
        return self.__name

    def getHealt(self):
        return self.__health

    # Setter
    def diserang(self,damage):
        self.__health -= damage

    def changeName(self,newHero):
        self.__name = newHero

# Mulai game
mirana = Dota2('Mirana', 250, 50)

# Play game
mirana.changeName('Drow Ranger')
print(mirana.getName())
mirana.critical(75)
print(mirana.getHealt())