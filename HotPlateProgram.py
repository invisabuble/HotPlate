from HotPlate import *

class HotPlateProgram : 

    def __init__ (self, **increments) :
        self.increments = increments
        self.wait_per_degree = 1

    def run_program (self) :

        for T, (temp, duration, time_per_degree) in self.increments.items() :

            HP.set_temp(temp, time_per_degree)

            # Wait the time for the plate to get to temperature,
            # Plus the duration to hold the temp once it has been reached.
            time.sleep(duration)

        print("Program finished!")

        HP.set_temp(0)