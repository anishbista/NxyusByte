import json
import random


class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display_question(self):
        print(self.question)
        for idx, option in enumerate(self.options, start=1):
            print(f"{idx}. {option}")
        print()

    def check_answer(self, user_answer):
        return user_answer == self.answer


class QuizGame:
    def __init__(self, questions_file):
        self.questions = self.load_questions(questions_file)
        self.current_question = None
        self.score = 0
        self.questions_asked = []

    def load_questions(self, file):
        with open(file, "r") as f:
            data = json.load(f)
        questions = []
        for item in data["questions"]:
            question = Question(item["question"], item["options"], item["answer"])
            questions.append(question)
        return questions

    def select_question(self):
        remaining_questions = [
            q for q in self.questions if q not in self.questions_asked
        ]
        if remaining_questions:
            self.current_question = random.choice(remaining_questions)
            self.questions_asked.append(self.current_question)
            return self.current_question
        else:
            return None

    def play_game(self):
        while True:
            selected_question = self.select_question()
            if selected_question is None:
                print("Congratulations! You've answered all the questions.")
                break
            selected_question.display_question()
            user_answer = input("Enter your answer (1, 2, 3, 4): ")
            if selected_question.check_answer(int(user_answer)):
                print("Correct answer!")
                self.score += 1
            else:
                print("Wrong answer.")
            print(f"Your current score is: {self.score}/{len(self.questions)}")
            print()

    def get_final_score(self):
        return self.score


if __name__ == "__main__":
    # Assuming questions are stored in a file named 'questions.json'
    quiz = QuizGame("questions.json")
    quiz.play_game()
    final_score = quiz.get_final_score()
    print(f"Your final score is: {final_score}/{len(quiz.questions)}")
