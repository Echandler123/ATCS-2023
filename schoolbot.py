# schoolbot.py
from fsm import FSM
from random import randint
# Generated by chatgpt edited and modified by me
class SchoolBotFSM(FSM):
    def __init__(self, width, height):
        super().__init__(initial_state="moving_to_class")
        self.width = width
        self.height = height
        # Define states
        self.add_transition("moving_to_class", "moving_to_class", self.move_to_class, "moving_to_class")
        self.add_transition("found_correct_class", "moving_to_class", self.found_correct_class, "success")
        # Initialize School Bot position
        self.school_bot_position = (200, 400)
    def move_to_class(self):
        print("Moving to class...")  
        # Replace with actual movement logic for the School Bot
        # Simulate random movement
        random_x = randint(-50, 50)
        random_y = randint(-50, 50)
        # Update School Bot position
        self.school_bot_position = (max(0, min(self.width- 30, self.school_bot_position[0] + random_x)),
        max(0, min(self.height - 30, self.school_bot_position[1] + random_y)))
    def found_correct_class(self):
        print("Found correct class! Congratulations!")     
    def not_found_correct_class(self):
        print("Incorrect class. Continuing the search...") 
