#/∗
# ∗CSCI3180 Principles of Programming Languages
# ∗
# ∗--- Declaration ---
# ∗
# ∗I declare that the assignment here submitted is original except for source
# ∗material explicitly acknowledged. I also acknowledge that I am aware of
# ∗University policy and regulations on honesty in academic work, and of the
# ∗disciplinary guidelines and procedures applicable to breaches of such policy
# ∗and regulations, as contained in the website
# ∗http://www.cuhk.edu.hk/policy/academichonesty/
# ∗
# ∗Assignment 2
# ∗Name : YU Si Hong
# ∗Student ID : 1155141630
# ∗Email Addr : shyu0@cse.cuhk.edu.hk
# ∗/

from abc import abstractmethod


class Cell:
    def __init__(self, row=0, col=0):
        self._row = row
        self._col = col
        self._occupant = None
        self._color = None
        self._hours = 0

    # TODO: hours getter and setter
    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hr):
        self._hours = hr

    # TODO: occupant getter
    @property
    def occupant(self):
        return self._occupant

    def set_occupant(self, obj):
        # TODO: set occupant for the Plain cell
        #       return whether success or not
        # if self.occupant() != None:
        #     print (obj.name()+" meets "+self.occupant().name())
        if self.occupant == None or self.occupant.interact_with(obj):
            self._occupant = obj
            # print("Cell [%d][%d] is occupied by %s"%(self._row, self._col, self._occupant.name))
            return True
        else:
            # print("Cell [%d][%d] is unavailable")
            return False
        # END TODO

    def remove_occupant(self):
        # TODO: remove the occupant
        self._occupant = None
        # END TODO

    def display(self):
        # TODO: print a string to display the cell
        #       and the occupant in the cell
        # print("reach here")
        if self.occupant == None:
            print("%s   \033[0m   " % (self._color), end='')
        else:
            print("%s %s%s \033[0m   " % (self._color,
                  self.occupant.display(), self._color), end='')
        # END TODO


class Plain(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;32;42m'
        self._hours = 1


class Mountain(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;37;47m'

    def set_occupant(self, obj):
        # TODO: return False
        # print("Player cannot set occupant in mountain!!!")
        return False
        # END TODO


class Swamp(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;34;44m'
        self._hours = 2
