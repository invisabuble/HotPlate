import RPi.GPIO as GPIO
import time


class HotPlate:

    def __init__ (self, **buttons) :

        self.buttons      = buttons
        self.press_timer  = 0.5
        self.debounce     = 0.1
        self.current_temp = 0

        GPIO.setmode(GPIO.BCM)

        for key, button in buttons.items() :
            GPIO.setup(button, GPIO.OUT)
            GPIO.output(button, GPIO.LOW)


    def press (self, button) :
        # Press a passed button.

        GPIO_NUM = self.buttons[button]

        if (button == "up") :
            self.current_temp += 1
        if (button == "down") :
            self.current_temp -= 1

        GPIO.output(GPIO_NUM, GPIO.HIGH)
        time.sleep(self.debounce)
        GPIO.output(GPIO_NUM, GPIO.LOW)
        time.sleep(self.press_timer)


    def change_temp (self, dT) :
        # Change temperature by a passed amount.

        self.press("set")

        up = dT > 0

        for T in range(abs(dT)) :

            if (up) :
                self.press("up")
            else : 
                self.press("down")

            if (self.current_temp < 0) :
                self.current_temp = 0
                break

        self.press("ent")


    def set_temp (self, T) :
        # Set the hotplate to a given temp.
        T = abs(T)

        dT = T - self.current_temp

        self.change_temp(dT)


    def calibrate (self) :
        self.current_temp = 400
        self.set_temp(0)


HP = HotPlate(
    set  = 6,
    ent  = 5,
    up   = 13,
    down = 12
)