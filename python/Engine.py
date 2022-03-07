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

from Map import Map
from Cell import Plain, Mountain, Swamp
from GameCharacter import Player, Goblin


class Engine:
    def __init__(self, data_file):
        self._actors = []
        self._map = None
        self._player = None
        with open(data_file, "r") as fp:
            line = fp.readline()
            if not line:
                return None
            else:
                buf = line.split()
                if len(buf) != 5:
                    print("INVALID DATA FILE.")
                    return None
                num_of_row = int(buf[0])
                num_of_col = int(buf[1])
                p_ox = int(buf[2])
                p_hp = int(buf[3])
                num_of_goblins = int(buf[4])

            self._map = Map(num_of_row, num_of_col)

            # TODO: initialize each cell of the map object
            #       using the build_cell method
            for i in range(num_of_row):
                tempstr = fp.readline()
                if not tempstr:
                    return None
                else:
                    buf = tempstr.split()
                    if len(buf) != num_of_col:
                        print("INVALID DATA FILE.")
                        return None
                    for j in range(num_of_col):
                        if buf[j] == "P":
                            self._map.build_cell(i, j, Plain(i, j))
                        elif buf[j] == "M":
                            self._map.build_cell(i, j, Mountain(i, j))
                            self._map.get_cell(i, j).set_occupant(None)
                        elif buf[j] == "S":
                            self._map.build_cell(i, j, Swamp(i, j))
                        else:
                            print("INVALID DATA FILE.")
                            return None
            # END TODO

            self._player = Player(num_of_row - 1, 0, p_hp, p_ox)

            # TODO: initilize the position of the player
            #       using the set_occupant and occupying setter;
            #       add the player to _actors array
            self._player = Player(num_of_row-1, 0, p_hp, p_ox)
            initcell = self._map.get_cell(num_of_row-1, 0)
            initcell.set_occupant(self._player)
            self._player.occupying = initcell
            self._actors.append(self._player)
            # END TODO

            for gno in range(num_of_goblins):
                # TODO: initilize each Goblin on the map
                #       using the set_occupant and occupying setter;
                #       add each Goblin to _actors array
                tempstr = fp.readline()
                if not tempstr:
                    print("INVALID DATA FILE.")
                    return None
                buf = tempstr.split()
                if len(buf) < 2:
                    print("INVALID DATA FILE.")
                    return None
                gobrow = int(buf[0])
                buf.pop(0)
                gobcol = int(buf[0])
                buf.pop(0)
                gob = Goblin(gobrow, gobcol, buf)
                self._actors.append(gob)
                initcell = self._map.get_cell(gobrow, gobcol)
                initcell.set_occupant(gob)
                gob.occupying = initcell
                # END TOD

    def run(self):
        # main rountine of the game
        self.print_info()
        while not self.state():
            for obj in self._actors:
                if obj.active:
                    obj.act(self._map)
            self.print_info()
            self.clean_up()
        self.print_result()

    def clean_up(self):
        # TODO: remove all objects in _actors which is not active
        for obj in self._actors:
            if not obj.active:
                self._actors.remove(obj)
        # END TODO

    # check if the game ends and return if the player win or not.
    def state(self):
        # TODO: check if the game ends and
        #       return an integer for the game status
        if self._player.hp <= 0 or self._player.oxygen <= 0:
            return -1
        elif self._player.row == 0 and self._player.col == self._map.cols-1:
            return 1
        else:
            return 0
        # END TODO

    def print_info(self):
        self._map.display()
        # TODO: display the remaining oxygen and HP
        print("Oxygen: %d, HP: %d" % (self._player.oxygen, self._player.hp))
        # END TODO

    def print_result(self):
        # TODO: print a string that shows the result of the game.
        if self.state() == 1:
            print("\033[1;33;41mCongrats! You win!\033[0;0m")
        elif self.state() == -1:
            print("\033[1;33;41mBad Luck! You lose.\033[0;0m")
        # END TODO
