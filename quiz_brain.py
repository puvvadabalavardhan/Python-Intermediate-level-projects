class QuizBrain:
 def __init__(self,question_list):
  self.question_list=question_list
  self.question_number=0
  self.score=0

 def still_questions_remaianing(self):
  if self.question_number<len(self.question_list):
    return True
  else:
    return False

 def nextquestion(self):
  current_question=self.question_list[self.question_number]
  self.question_number += 1
  que=input(f"Q.{self.question_number}:{current_question.text}(True/Talse):").lower()
  self.check_answer(que,current_question.answer)
  

 def check_answer(self,que,correct_answer):
   if que.lower()==correct_answer.lower():
     print("you are right")
     self.score+=1
   else:
     print("you are wrong")
     print(f"the correct answer is {correct_answer}")
     print(f"your score is{self.score}/{self.question_number}")
     print("\n")
   