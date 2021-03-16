class Car:
    def __init__(self, make, model, kph, hp):
        self.make = make
        self.model = model
        self.kph = kph
        self.hp = hp
   
    #make
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, make):
        self.__make = make

    #model
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    #kph
    @property
    def kph(self):
        return self.__kph

    @kph.setter
    def kph(self, kph):
        self.__kph = kph
    
    #hp
    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp
