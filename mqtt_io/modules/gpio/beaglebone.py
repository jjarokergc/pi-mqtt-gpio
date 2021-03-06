from . import GenericGPIO, PinDirection, PinPUD

REQUIREMENTS = ("Adafruit_BBIO",)

DIRECTIONS = None
PULLUPS = None


class GPIO(GenericGPIO):
    """
    Implementation of GPIO class for Beaglebone native GPIO.
    """

    def __init__(self, config):
        global DIRECTIONS, PULLUPS
        import Adafruit_BBIO.GPIO as gpio

        self.io = gpio
        DIRECTIONS = {PinDirection.INPUT: gpio.IN, PinDirection.OUTPUT: gpio.OUT}

        PULLUPS = {
            PinPUD.OFF: gpio.PUD_OFF,
            PinPUD.UP: gpio.PUD_UP,
            PinPUD.DOWN: gpio.PUD_DOWN,
        }

    def setup_pin(self, pin, direction, pullup, pin_config):
        direction = DIRECTIONS[direction]

        if pullup is None:
            pullup = PULLUPS[PinPUD.OFF]
        else:
            pullup = PULLUPS[pullup]

        initial = {None: -1, "low": 0, "high": 1}[pin_config.get("initial")]
        self.io.setup(pin, direction, pull_up_down=pullup, initial=initial)

    def set_pin(self, pin, value):
        self.io.output(pin, value)

    def get_pin(self, pin):
        return self.io.input(pin)

    def cleanup(self):
        self.io.cleanup()
