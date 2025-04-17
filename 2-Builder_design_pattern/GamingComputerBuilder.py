# Implimantaion of Gaming Computer 

from computer import Computer
from ComputerBuilder import ComputerBuilder

"""
here GamingComupter is a child class of ComputerBuilder
we have created abstract methods and now we have to impliment it 
also apply velidation where it required..
"""

class GamingComputerBuilder(ComputerBuilder):  # is a child class of computer builder
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.storate = 0
        self.power_supply = 0

    def set_ram(self, ram):
        self.ram = ram

    def set_cpu(self, cpu):
        if cpu < 2:
            raise ValueError("CPU must be at least 2")
        self.cpu = cpu

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_power_supply(self, power_supply):
        self.set_power_supply = power_supply

    def set_storage(self, storage):
        self.storage = storage


    # implementation to create the computer and return the object 
    def build(self):
        # crete the object of computer class and pass all the parameter here

        # c= Computer(self.ram, self.cpu, self.gpu, self.storage, self.power_supply)
    #    let use getter and setter as we have so much parameter 
        c = Computer() 
        c.set_cpu(self.cpu)
        c.set_ram(self.ram)
        c.set_gpu(self.gpu)
        c.set_power_suply(self.power_supply)
        c.set_storage(self.storage)
        return c
    

    