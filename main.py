import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

no = int(input("No of questions you want :"))
x = random.sample(range(0, 49), no)

question_bank = []
for i in x:
    question_bank.append(Question(question_data[i]['question'], question_data[i]['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still():
    correct_answer, user_answer = quiz.next_question()
    quiz.check_answer(correct_answer, user_answer)
print("You have completed the quiz")
print(f"Your total score was : {quiz.score}/{len(quiz.question_list)}")
