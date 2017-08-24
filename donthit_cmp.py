#donthit_cmp.py

import tkinter
import bars

CMP_MODE = True

ALG_1 = True
ALG_2 = False

LEFT_EVENT = "<Left>"
RIGHT_EVENT = "<Right>"


def alg_1(pad_location: int, dropping_round: list, canvas: tkinter.Canvas) -> int:    
    if bars.EMPTY not in dropping_round:
        return pad_location
    while dropping_round[pad_location] == bars.BAR:
        if bars.EMPTY in dropping_round[:pad_location]:
            canvas.event_generate(LEFT_EVENT)
            if pad_location > 0:
                pad_location -= 1
        elif bars.EMPTY in dropping_round[pad_location:]:
            canvas.event_generate(RIGHT_EVENT)
            if pad_location < bars.COL-1:
                pad_location += 1
    return pad_location

def alg_2(pad_location: int, dropping_round: list, canvas: tkinter.Canvas) -> int:
    if bars.EMPTY in dropping_round:
        for row_num in range(bars.COL):
            if dropping_round[row_num] == bars.EMPTY:
                return row_num
    else:
        return pad_location

def cmp_mode(pad_location: int, dropping_round: list, canvas: tkinter.Canvas) -> int:
    if ALG_1:
        return alg_1(pad_location, dropping_round, canvas)
    elif ALG_2:
        return alg_2(pad_location, dropping_round, canvas)

def get_alg_name() -> str:
    if ALG_1:
        return "ALG_1"
    elif ALG_2:
        return "ALG_2"
    
        
    
