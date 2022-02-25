from Cell import Cell


class Map:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._cells = [[Cell() for x in range(cols)] for y in range(rows)]
    
    #TODO: rows getter
    def rows(self):
        return self._rows
    
    #TODO: cols getter
    def cols(self):
        return self._cols
    
    def get_cell(self, row, col):
        # TODO: check whether the position is out of boundary 
        #       if not, return the cell at (row, col)
        #       return None otherwise 
        if self._rows<=row or 0>row or self._cols<=col or 0>col: 
            print("\033[1;31;46mNext move is out of boundary!\033[0;0m")
            return None 
        else:
            # return a cell 
            return Cell(row, col)
        # END TODO 

    def build_cell(self, row, col, cell):
        # TODO: check whether the position is out of boundary 
        #       if not, add a cell (row, col) and return True
        #       return False otherwise 
        if self._rows<=row or 0>row or self._cols<=col or 0>col: 
            print("\033[1;31;46mThe position (%d, %d) is out of boundary!\033[0;0m" %(row, col))
            return False 
        else:
            # return a cell 
            self._cells[row][col] = cell
            return True
        # END TODO

    # return a list of cells which are neighbours of cell (row, col) 
    def get_neighbours(self, row, col):
        return_cells = []
        # TODO: return a list of neighboring cells of cell (row, col)
        for i in range(max(0, row-1), min(row+1, self._rows-1)+1):
            for j in range(max(0, col-1), min(col+1, self._cols-1)+1):
                return_cells.append(self._cells[i][j])
        return return_cells
        # END TODO
        

    def display(self):
        # TODO: print the map by calling diplay of each cell 
        print("   ", end='')
        for i in range(self._cols):
            print("%d     "%(i), end='')
        print()
        for i in range(self._rows):
            print("%d "%(i), end='')
            for j in range(self._cols):
                self._cells[i][j].display
            print()
            print()
        # END TODO
