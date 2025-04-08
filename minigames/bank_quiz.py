
import pygame

class BankQuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is Superseed primarily designed to do?",
                "options": ["Mine Bitcoin", "Repay user debt automatically", "Create NFTs"],
                "answer": 1
            },
            {
                "question": "What is the name of the token used in Superseed?",
                "options": ["USDT", "SEED", "XRP"],
                "answer": 1
            },
            {
                "question": "How does Superseed reduce user debt?",
                "options": ["With donations", "Through engagement with the economy", "Random airdrops"],
                "answer": 1
            }
        ]
        self.current_question = 0
        self.score = 0
        self.finished = False

    def render(self, screen, font):
        if self.finished:
            message = f"Quiz complete! Score: {self.score}/{len(self.questions)}"
            text = font.render(message, True, (255, 255, 0))
            screen.blit(text, (100, 100))
            return

        q = self.questions[self.current_question]
        question_text = font.render(q["question"], True, (255, 255, 255))
        screen.blit(question_text, (50, 50))
        for i, option in enumerate(q["options"]):
            opt_text = font.render(f"{i+1}. {option}", True, (200, 200, 255))
            screen.blit(opt_text, (70, 100 + i * 40))

    def answer(self, index):
        if self.finished:
            return
        correct = self.questions[self.current_question]["answer"]
        if index == correct:
            self.score += 1
        self.current_question += 1
        if self.current_question >= len(self.questions):
            self.finished = True
