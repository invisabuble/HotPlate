from HotPlate import *

class HotPlateProgram : 

    def __init__ (self, **increments) :
        self.increments = increments
        self.wait_per_degree = 3

    def run_program (self) :

        print("Running program...")

        for T, (temp, duration) in self.increments.items() :

            print(f"Setting temperature to {temp}. Will hold for {duration}")

            wait_time = abs(temp - HP.current_temp) * self.wait_per_degree

            HP.set_temp(temp)

            # Wait the time for the plate to get to temperature,
            # Plus the duration to hold the temp once it has been reached.
            time.sleep(wait_time + duration)

        print("Program finished!")

        HP.zero_temp()