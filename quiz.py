
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)

        for number in range(4):
            print(f"{number + 1}. {self.choices[number]}")

    def is_correct(self, choice):
        return choice == self.answer
