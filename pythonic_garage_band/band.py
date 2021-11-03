# from _typeshed import Self
from abc import ABC , abstractmethod
from typing import Counter

class Band():
    instances = []
    def __init__(self,name ,members):
        self.name = name
        self.members = members
        # print(Band.bandsList)
        # print(name)
        # print(self.name)
        Band.instances.append(self)
        print(Band.instances[0])

    
    def play_solos(self):
        solo = []
        for i in self.members:
            instroment = i.get_instrument()
            if instroment == "guitar":
                solo.append("face melting guitar solo")
            elif instroment == "bass":
                solo.append("bom bom buh bom")
            else:
                solo.append("rattle boom crash")
        return solo

    @classmethod
    def to_list(cls):
        return cls.instances
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        # print(type(self.name))
        return self.name
    
    # print(__repr__())


class Musician():
    def __init__(self, name ):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

        
