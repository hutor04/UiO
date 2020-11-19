# The class Hund
class Hund():
    # Initiate the instance with 2 positional variables, one variable has a default value
    def __init__(self, alder, vekt, metthet=10):
        self._age = alder
        self._vekt = vekt
        self._hunger = metthet

    # Returns age of the dog
    @property
    def alder(self):
        return self._age

    # Returns weight of the dog
    @property
    def vekt(self):
        return self._vekt

    # The method affects the variables of the instance
    def spring(self):
        self._hunger -= 1
        if self._hunger < 5:
            self._vekt -= 1

    # The method affects the variables of the instance
    def spis(self, food):
        self._hunger += food
        if self._hunger > 7:
            self._vekt += 1
