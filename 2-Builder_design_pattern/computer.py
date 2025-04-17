""" 
what are the things computer have,  depending on the requirement we can get which ever computer we want
either it's
 - gmaing comuter 
 - office computer 
 - home computer

"""
 
class Computer:
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.power_supply = 0
        self.storage = 0

    # we are adding setter method not passing as a parameter becuase we have so much optionsal parameter 
    def set_ram(self,ram):
        self.ram = ram

    def set_cpu(self,cpu):
        self.cpu = cpu

    def set_gpu(self,gpu):
        self.gpu = gpu

    def set_storage(self,stogae):
        self.storage = stogae

    def set_power_suply(self,power_supply):
        self.power_supply = power_supply  