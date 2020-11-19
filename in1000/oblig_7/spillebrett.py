from random import randint
from itertools import chain
from celle import Celle


# The class creates the game field and handles the cells' status
class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generation = 0
        self._rutenett = [[Celle() for i in range(kolonner)] for j in range(rader)]
        self.generer()

    # Print out the game field based on the dimensions
    def tegnBrett(self):
        for row in self._rutenett:
            print(''.join([j.hentStatusTegn() for j in row]))


    # Update the status of each cell based on the rules of the game
    def oppdatering(self):
        to_live = []
        to_die = []
        for row in range(self._rader):
            for col in range(self._kolonner):
                cell_state = self._rutenett[row][col].erLevende()
                live_neighbors = [cell.erLevende() for cell in self.finnNabo(col, row)].count(True)
                if cell_state and (live_neighbors < 2 or live_neighbors > 3):
                    to_die.append(self._rutenett[row][col])
                elif not cell_state and live_neighbors == 3:
                    to_live.append(self._rutenett[row][col])
        # Apply new status to the cells
        for cell in to_live:
            cell.settLevende()
        for cell in to_die:
            cell.settDoed()
        # Increment generation
        self._generation += 1

    # Find the number of live cells in the current generation
    def finnAntallLevende(self):
        # chain lets us iterate over the nested lists with one for-cycle, we could have used
        # more lengthy:
        # for row in rows:
        #   for cell in cells:
        #       do something...
        return len([cell.erLevende() for cell in chain(*self._rutenett) if cell.erLevende()])

    # Return the value of the variable self._generation
    def generation(self):
        return self._generation

    # Seed the 0 generation of the cells
    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand = randint(0, 3)
                if rand == 3:
                    self._rutenett[i][j].settLevende()

    # Find the neighbour cells of the cell
    def finnNabo(self, x, y):
        naboliste = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                naboX = x+i
                naboY = y+j
                if (naboX == x and naboY == y) != True:
                    if (naboX < 0 or naboY < 0 or naboX > self._kolonner-1 or naboY > self._rader-1) != True:
                        naboliste.append(self._rutenett[naboY][naboX])
        return naboliste
