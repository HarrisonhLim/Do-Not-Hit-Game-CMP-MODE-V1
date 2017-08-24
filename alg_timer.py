#alg_timer.py

"""
This class is used to save the data of the average time that took
to calculate the path to find the solution to each round  as a text file named "dont_hit_data.txt"
in the
format of
algorithm_name + " " + "rounds_played: " + round_counter + " " + "total_time: " + total_time +" " + "average_time_per_round: " + avg_time_per_round + "\n"
example:
ALG_1 rounds_played: 561 total_time: 4.287428231390196 average_time_per_round: 0.0076424745657579255
ALG_2 rounds_played: 211 total_time: 0.004446765305824634 average_time_per_round: 2.1074717089216276e-05
"""
class alg_timer():
    def __init__(self, alg_name: str):
        self._alg_name = alg_name
        self._total_time = 0
        self._round_counter = 0
        self._avg_time_per_round = 0

    def add_to_total_time(self, one_round_time: float) -> None:
        self._total_time += one_round_time
        
    def increment_round_counter(self) -> None:
        self._round_counter += 1
        
    def save_the_data(self) -> None:
        self._get_avg_time_per_round()
        data_file = open("dont_hit_data.txt", "a")
        data_file.write(self._alg_name + " " +
                        "rounds_played: " + str(self._round_counter) + " " +
                        "total_time: " + str(self._total_time) + " " +
                        "average_time_per_round: " + str(self._avg_time_per_round) + "\n")
        data_file.close()

    def _get_avg_time_per_round(self) -> None:
        self._avg_time_per_round = self._total_time/self._round_counter
