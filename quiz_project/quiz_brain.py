class QuizBrain:
    def __init__(self, q_list):
        """Initialize the quiz state and question list."""
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Return True when there are questions left."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Display the next question and collect an answer."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False?): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Check the user's answer and update the score."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")