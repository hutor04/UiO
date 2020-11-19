# The class creates the cell, changes, and returns its state
class Celle:
    # Saves some memory
    __slots__ = ['_state']

    # Constructor
    def __init__(self):
        self._state = False

    # Change the state of the cell to 'dead'
    def settDoed(self):
        self._state = False

    # Change the state of the cell to 'live'
    def settLevende(self):
        self._state = True

    # Return the stateof the cell
    def erLevende(self):
        return self._state

    # Return the representation of the cell, we also change color
    def hentStatusTegn(self):
        return ('\033[91m.\033[00m', '\033[92mO\033[00m')[self._state]
