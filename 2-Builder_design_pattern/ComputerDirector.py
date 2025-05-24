class ComputerDirector:
    """
    Director will talk to Builder, depending on the requirement
    let user want gaming computer
    than director will connect to GamingComputer Builder
    but,
     if we directly bound director to GamingComputerbuilder 
      it is tighly coupled as we have other typer of computer as well
    it voitets/ breaks dependdency Inversion Principle (DI)

    so, we have to bound it with computerBuilder not the specific type of computer 
    Now,
      director will tell the to computer builder to build the computer
    """
    def __init__(self, ComputerBuilder): #director will tell the to computer builder to build the computer
        self.ComputerBuilder = ComputerBuilder

    def construct(self):
        # this method set the value as per user pass in the parameter let use here dirctly 
        self.ComputerBuilder.set_cpu(1)
        self.ComputerBuilder.set_ram(2)
        # self.ComputerBuilder.set_gpu(2)
        self.ComputerBuilder.set_storage(2)
        self.ComputerBuilder.set_power_supply(5)

# once everything is done call the build method to build the computer 

    def get_computer(self):
        return self.ComputerBuilder.build()