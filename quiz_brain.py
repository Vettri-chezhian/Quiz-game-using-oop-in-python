class QuizBrain:
    def __init__(self, qlist):
        self.question_no = 0
        self.question_list = qlist
        self.score = 0

    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"correct answer : {correct_answer}")
            print(f"score = {self.score}/{self.question_no}")
            print()
        else:
            print(f"correct answer : {correct_answer}")
            print(f"score = {self.score}/{self.question_no}")
            print()

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f"Q.{self.question_no}: {current_question.question} (true/false):")
        return current_question.ans, answer

    def still(self):
        return self.question_no < len(self.question_list)



