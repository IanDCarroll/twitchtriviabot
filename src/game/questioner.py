import re

class Questioner:
    hint_replacement = '_'

    def clean(answer):
        lower_case = answer.lower()
        letters_only = filter(str.isalpha, lower_case)
        return "".join(letters_only)

    def __init__(self, question):
        self.ask = question['Ask']
        self.answer = question['Answer']

    def check_answer(self, participant_answer):
        participant_answer = Questioner.clean(participant_answer)
        correct_answer = Questioner.clean(self.answer)
        return correct_answer in participant_answer

    def first_hint(self):
        hint = ""
        for index, char in enumerate(self.answer):
            hint += char if index % 3 == 0 else Questioner.hint_replacement
        return hint

    def second_hint(self):
        vowels = '[aeiou]'
        repl = Questioner.hint_replacement
        return re.sub(vowels, repl, self.answer, flags=re.I)
