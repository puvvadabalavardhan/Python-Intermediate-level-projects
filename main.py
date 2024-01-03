from question_model import Answers
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
   question_text=question["text"]
   question_answer=question["answer"]
   new_question=Answers(question_text,question_answer)
   question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_questions_remaianing():
    quiz.nextquestion()

print("you have completed the quiz")
print(f"Your final score is:{quiz.score}/{quiz.question_number}")

      