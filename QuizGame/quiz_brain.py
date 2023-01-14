class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    #Checking if we're the end of the quiz
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

    #Asking the questions
    def next_question(self):
        currentQuestion = self.question_list[self.question_number]
        self.question_number += 1

        userAnswer = input(f"Q.{self.question_number}: {currentQuestion.text} (True/False): ")

        self.check_answer(userAnswer, currentQuestion.answer)

    #Checking if the answer was correct
    def check_answer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is: {self.score}/{len(self.question_list)}\n")

