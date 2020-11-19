class Minefield:
    def __init__(self, N: int, M: int):
        self.N = N  # Rows
        self.M = M  # Columns
        self.map = [[0 for x in range(M)] for y in range(N)]
    
    def load_field(self, field):
        self.field = field
    
    def find_neighbours(self, x, y): # col, row
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                X = x+i
                Y = y+j
                if (X == x and Y == y) != True:
                    if (X < 0 or Y < 0 or X > self.M-1 or Y > self.N-1) != True:
                        neighbours.append(self.field[Y][X])
        return neighbours
    
    def count_mines(self, neighbours, mine='*'):
        count = 0
        for i in neighbours:
            if i == mine:
                count += 1
        return count
    
    def generate_map(self):
        for idx_i, i in enumerate(self.field):
            for idx_j, j in enumerate(i):
                if j == '*':
                    self.map[idx_i][idx_j] = '*'
                else:
                    neighbours = self.find_neighbours(idx_j, idx_i)
                    self.map[idx_i][idx_j] = self.count_mines(neighbours)


if __name__ == '__main__':
    f = Minefield(3, 4)
    mines = [['*','.','.','.'],
             ['.','.','*','.'],
             ['.','.','.','.']]
    f.load_field(mines)
    f.generate_map()
    print(f.map)