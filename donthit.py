#dont_hit.py

import tkinter
import time

import bars
import pad
import donthit_cmp
import alg_timer

PAD_COLOR = "red"
PAD_OVER_COLOR = "yellow"
BAR_COLOR = "white"


class DontHitState:
    """
    This class represents the game state
    """
    def __init__(self):
        self._bars = bars.DroppingBars()
        self._pad = pad.Paddle()
        self._game_over_flag = False
        
    def bars(self) -> bars.DroppingBars:
        return self._bars

    def pad(self) -> pad.Paddle:
        return self._pad

    def is_game_over(self) -> bool:
        return self._game_over_flag
    
    def next_frame(self) -> None:
        """
        A round procceds, one row of bars is dropped.
        If the location of the pad is where one of the bars is,
        then the game ends. 
        """
        dropped_round = self.bars().drop_a_round()
        if dropped_round[self._pad.get_pad_location()] == bars.BAR:
            self._game_over_flag = True
            
class DontHitApplication:
    """
    This class controls the gui and the flow of the game using
    event oriented programming features of tkinter.
    """
    def __init__(self):
        self._game_state = DontHitState()
        #the unit for self._time_limit is in ms
        self._time_limit = 250
        #Generating tkinter window and canvas to display the game
        self._root_window = tkinter.Tk()
        #Tkinter Canvas 
        self._canvas_width = 1000
        self._canvas_height = 500
        self._canvas = tkinter.Canvas(
            master = self._root_window, background = "black",
            width = self._canvas_width, height = self._canvas_height)
        self._canvas.grid(row = 0, column = 0,
                          sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        #The game supports resizing of the window
        self._canvas.bind("<Configure>", self._on_canvas_resized)
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.after(40, self._next_frame)
        
        self._canvas.focus_set()

        #Event binding to the canvas
        self._canvas.bind("<Left>", self._on_left)
        self._canvas.bind("<Right>", self._on_right)

        #Get algorithm name if CMP_MODE is one
        if donthit_cmp.CMP_MODE:
            self._alg_name = donthit_cmp.get_alg_name()
            self._alg_timer = alg_timer.alg_timer(self._alg_name)

    def run(self) -> None:
        self._root_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        #When the configuration of the window changes, new frame is drawn.
        self._draw_frame()

    def _on_left(self, event: tkinter.Event) -> None:
        """
        When "<Left>", event that occurs when left arrow on the keyboard is prssed,
        paddle moves left, and new frame is drawn
        """
        if self._game_state.is_game_over():
            return
        self._game_state.pad().move_left()
        self._draw_frame()

    def _on_right(self, event: tkinter.Event) -> None:
        """
        When "<Right>", event that occurs when right arrow on the keyboard is prssed,
        paddle moves right, and new frame is drawn
        """
        if self._game_state.is_game_over():
            return
        self._game_state.pad().move_right()
        self._draw_frame()

    def _next_frame(self) -> None:
        #Display Game state to the users visually
        ### DIRECT ACCESS TO THE PAD LOCATION WARNING
        #FOR CMP MODE 
        if donthit_cmp.CMP_MODE:
            alg_mode_start_time = time.clock()
            self._game_state.pad().change_pad_location(donthit_cmp.cmp_mode(self._game_state.pad().get_pad_location(),
                                                                          self._game_state.bars().get_rounds()[0],
                                                                          self._canvas))
            alg_mode_end_time = time.clock()
            #print("start_time: " + str(alg_mode_start_time) + " end_time: " + str(alg_mode_end_time) + " subtract: " + str(alg_mode_start_time-alg_mode_end_time))  
            self._alg_timer.add_to_total_time(alg_mode_end_time-alg_mode_start_time)
            self._alg_timer.increment_round_counter()            
            self._draw_frame()
        ###
        self._game_state.next_frame()
        self._draw_frame()
        
        if self._game_state.is_game_over():
            #When the game is over, game over message and the score are displayed
            self._draw_game_over() 
            return
        self._root_window.after(self._time_limit, self._next_frame)


    def _draw_frame(self) -> None:
        #Deletes the old frame and draws a new frame to the canvas
        self._canvas.delete(tkinter.ALL)
        self._draw_bars()
        self._draw_pad(PAD_COLOR)
        
    def _draw_bars(self) -> None:
        #Draws bars according to the game state
        pad_location = self._game_state.pad().get_pad_location()
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        board_row_num = bars.ROW
        board_col_num = bars.COL
        board_row_frac = 1/(board_row_num+1)
        board_col_frac = 1/board_col_num
        for row in range(board_row_num):
            for col in range(board_col_num):
                if self._game_state.bars().get_rounds()[row][col] == bars.BAR:
                    x1 = canvas_width*board_col_frac*col
                    y1 = canvas_height*board_row_frac*(board_row_num-row-1)
                    x2 = canvas_width*board_col_frac*(col+1)
                    y2 = canvas_height*board_row_frac*(board_row_num-row-0)
                    self._draw_bar(x1, y1, x2, y2)
        
    def _draw_bar(self, x1: float, y1: float, x2: float, y2: float) -> None:
        #Draws a bar using the given coordinates
        edge_const = 0.05
        self._canvas.create_rectangle(x1-edge_const, y1-edge_const,
                                      x2-edge_const, y2-edge_const,
                                      fill = BAR_COLOR)
        
    def _draw_pad(self, color: str) -> None:
        #Draws the pad
        pad_location = self._game_state.pad().get_pad_location()
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        board_row_num = bars.ROW
        board_col_num = bars.COL
        board_row_frac = 1/(board_row_num+1)
        board_col_frac = 1/board_col_num
        x1 = canvas_width*board_col_frac*pad_location
        y1 = canvas_height*board_row_frac*board_row_num
        x2 = canvas_width*board_col_frac*(pad_location+1)
        y2 = canvas_height*board_row_frac*(board_row_num+1)
        self._canvas.create_rectangle(x1, y1, x2, y2, fill = color)

    def _draw_game_over(self) -> None:
        #Shows Game Over Message with Score
        self._canvas.delete(tkinter.ALL)
        self._canvas.create_text(self._canvas_width/2, self._canvas_height/2, fill = "white", font = "Times 50", text = "GAME OVER\n SCORE:" + str(self._game_state.bars().get_round_counter()))
        if donthit_cmp.CMP_MODE:
            self._alg_timer.save_the_data()
if __name__ == "__main__":
    DontHitApplication().run()
    
    
