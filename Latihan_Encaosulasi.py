class Hero:

    __jumlah = 0

    def __init__(self,name, health, power, armor):
        self.__name = name
        self.__healhtAwal = health
        self.__powerAwal = power
        self.__armorAwal = armor
        self.__exp = 0
        self.__lv = 1

        self.__healthMax = self.__healhtAwal * self.__lv
        self.__powerMax = self.__powerAwal * 0.5 * self.__lv
        self.__armorMax = self.__armorAwal * self.__lv

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} : \nlevel {} \n\thealth = {}/{} \n\tpower = {} \n\tarmor = {} ".format(self.__name,self.__lv ,self.__health, self.__healthMax, self.__powerAwal,self.__armorAwal  )

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name, 'Level up')
            self.__lv += 1
            self.__exp -= 100

            self.__healthMax = self.__healhtAwal * self.__lv
            self.__powerMax = self.__powerAwal * 0.5 * self.__lv
            self.__armorMax = self.__armorAwal * self.__lv

    def attack(self,enemy):
        self.gainExp = 50

mirana = Hero('mirana', 150 , 20 , 5)
axe = Hero('mirana', 150 , 20 , 5)
print(mirana.info)
mirana.attack(axe)
mirana.attack(axe)
mirana.attack(axe)
print(mirana.gainExp)