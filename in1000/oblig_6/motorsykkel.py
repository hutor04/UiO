# The is a class that describes motorcycles.


class Motorsykkel():
    # Initiate class with three variables
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self._brand = merke
        self._number = registreringsnummer
        self._mileage = kilometerstand

    # Increases milage by user input
    def kjor(self, km):
        self._mileage += km

    # Returns milage. It's not very pythonic to 'hide' instance variables begind setter or getter methods,
    # I created the method to satisfy the requirements of the task, and use 'property' decorator to keep working
    # with variables as I usually do
    @property
    def hentKilometerstand(self):
        return self._mileage

    # Prints out information about the instance
    def skrivUt(self):
        print('Merke: {}, Registreringsnummer: {}, Kilometerstand: {}.'.format(self._brand, self._number, self._mileage))

