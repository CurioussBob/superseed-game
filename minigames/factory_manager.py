
import pygame

class FactoryManagerGame:
    def __init__(self):
        self.tasks = [
            {
                "worker": "Alice",
                "question": "What should I do with the coolant?",
                "options": ["Recycle it", "Dump it", "Ignore it"],
                "answer": 0
            },
            {
                "worker": "Bob",
                "question": "How many cycles should the reactor run today?",
                "options": ["2", "4", "8"],
                "answer": 1
            },
            {
                "worker": "Zara",
                "question": "Do I fix the pipe now or wait?",
                "options": ["Fix now", "Wait", "Ask manager"],
                "answer": 0
            }
        ]
        self.current_task = 0
        self.correct = 0
        self.finished = False
        self.font = pygame.font.Font(None, 30)

    def render(self, screen):
        if self.finished:
            message = f"Factory complete! Correct answers: {self.correct}/{len(self.tasks)}"
            text = self.font.render(message, True, (255, 255, 0))
            screen.blit(text, (80, 80))
            return

        task = self.tasks[self.current_task]
        worker_text = self.font.render(f"{task['worker']} asks:", True, (255, 255, 255))
        question_text = self.font.render(task['question'], True, (255, 255, 255))
        screen.blit(worker_text, (50, 50))
        screen.blit(question_text, (50, 90))
        for i, option in enumerate(task["options"]):
            opt_text = self.font.render(f"{i+1}. {option}", True, (200, 200, 255))
            screen.blit(opt_text, (70, 140 + i * 35))

    def answer(self, index):
        if self.finished:
            return
        correct = self.tasks[self.current_task]["answer"]
        if index == correct:
            self.correct += 1
        self.current_task += 1
        if self.current_task >= len(self.tasks):
            self.finished = True
