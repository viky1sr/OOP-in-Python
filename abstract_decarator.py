from abc import ABC,abstractmethod

# Abstract yang mengunakan decarator

class Button(ABC):

    def __init__(self,set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    # wajib pertama mengunakan @property sprt conth di bawah
    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):

    def click(self):
        print('Go to : {}'.format(self.link))

    # wajib pertama megunakan Nama CLASS terlebih dahulu
    @Button.link.setter
    def link(self,input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link

tombol1 = PushButton('www.vikyganteng.id')

tombol1.click()