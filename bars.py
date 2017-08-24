#bars.py
import random

EMPTY = 0
BAR = 1

ROW = 10
COL = 20

"""
DroppingBars includes a two dimmensional array that has 10 rounds of dropping bars.
The number of bars dropping is generated randomly,
but its range varies depending on the level.
The bars locations are also generated randomly.
"""
class DroppingBars:
    def __init__(self):
        self._counter = 0
        self._game_setting()
        self._level = 1
        self._rounds = []
        self._make_initial_rounds()
        
    def drop_a_round(self) -> list:
        """
        Remove and return the first round.
        Newly generated round is appended to the rounds. 
        """
        self._update_level()
        dropping_round = self._rounds.pop(0)
        self._rounds.append(self._make_a_round())
        self._counter += 1
        return dropping_round

    def get_rounds(self) -> list:
        return self._rounds

    def get_round_counter(self) -> list:
        return self._counter
    
    def get_row(self) -> int:
        return self._row

    def get_col(self) -> int:
        return self._col
        
    def _game_setting(self) -> None:
        #Range of number of bars dropping for each level
        self._lvl_1_min = 0
        self._lvl_1_max = 5
        self._lvl_2_min = 6
        self._lvl_2_max = 10
        self._lvl_3_min = 11
        self._lvl_3_max = 15
        self._lvl_4_min = 16
        self._lvl_4_max = 19
        self._lvl_5_min = 20
        self._lvl_5_max = 20
        #Number of rounds played for each level
        self._lvl_1 = 50
        self._lvl_2 = 50
        self._lvl_3 = 50
        self._lvl_4 = 400
        self._lvl_5 = 1
        #Number of Rows and Columns of the game board
        self._row = ROW
        self._col = COL
        
    def _make_initial_rounds(self) -> None:
        #Generates the first ten rounds of the game
        for row in range(self._row):
            self._rounds.append(self._make_a_round())
            
    def _make_a_round(self) -> list:
        #Generates a new round
        one_round = []
        for col in range(self._col):
            one_round.append(EMPTY)
        random.seed()
        bar_num = random.randrange(self._get_level_min(),
                                   self._get_level_max()+1)
        while bar_num > 0:
            temp_bar_col = random.randrange(0, self._col)
            if one_round[temp_bar_col] == EMPTY:
                one_round[temp_bar_col] = BAR
                bar_num -= 1
        return one_round

    def _update_level(self) -> None:
        #Updates level depending on the rounds 
        if self._counter < self._lvl_1:
            self._level = 1
        elif self._counter < self._lvl_1+self._lvl_2:
            self._level = 2
        elif self._counter < self._lvl_1+self._lvl_2+self._lvl_3:
            self._level = 3       
        elif self._counter < self._lvl_1+self._lvl_2+self._lvl_3+self._lvl_4:
            self._level = 4
        else:
            self._level = 5

    
    def _get_level_min(self) -> int:
        #returns the minimum number of bars for the level
        if self._level == 1:
            return self._lvl_1_min
        elif self._level == 2:
            return self._lvl_2_min
        elif self._level == 3:
            return self._lvl_3_min
        elif self._level == 4:
            return self._lvl_4_min
        elif self._level == 5:
            return self._lvl_5_min
            
    def _get_level_max(self) -> int:
        #Returns the maximum number of bars for the level
        if self._level == 1:
            return self._lvl_1_max
        elif self._level == 2:
            return self._lvl_2_max
        elif self._level == 3:
            return self._lvl_3_max
        elif self._level == 4:
            return self._lvl_4_max
        elif self._level == 5:
            return self._lvl_5_max        
        
