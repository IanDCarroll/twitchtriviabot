class Timer:

    def __init__(self, tempo = "int used in real timer", settings = "obj used in real timer"):
        pass

    def start_question_timer(self):
        self._times_asked = 0

    def question_time_up(self):
        self._times_asked += 1
        return self._times_asked >= 18

    def question_hint_1_up(self):
        return self._times_asked >= 4

    def question_hint_2_up(self):
        return self._times_asked >= 8

    def wait(self):
        pass
