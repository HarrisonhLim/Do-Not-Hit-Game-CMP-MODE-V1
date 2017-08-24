#pad.py
import bars

PAD = 9999

"""
Paddle class can move left or right in the game board.
The size of game board is depending on the values in bars.py
"""

class Paddle:
    def __init__(self):
        #The Row and Col values depend on the values in bars.by
        self._row = bars.ROW
        self._col = bars.COL
        self._pad = []
        for col in range(self._col):
            self._pad.append(0)
        self._pad[int(self._col/2)] = PAD
        self._pad_location = int(self._col/2)

    def get_pad_location(self) -> int:
        return self._pad_location

    def move_left(self) -> None:
        #Move the paddle to the left
        if self._pad_location > 0:
            self._pad[self._pad_location] = bars.EMPTY
            self._pad_location -= 1
            self._pad[self._pad_location] = PAD
        
    def move_right(self) -> None:
        #Move the paddle to the right
        if self._pad_location < self._col-1:
            self._pad[self._pad_location] = bars.EMPTY
            self._pad_location += 1
            self._pad[self._pad_location] = PAD

    def change_pad_location(self, new_pad_location: int) -> None:
        #change pad locaiton to a given new pad location:
        self._pad_location = new_pad_location
        #print("pad location changed to", self._pad_location)
