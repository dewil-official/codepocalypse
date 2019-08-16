import time
import sys
import os
from game.classes import choices
from game import story

# "point" = A specific point in the story
class point:

    text = ""
    choices = [ choices.choice(), ]

    def __init__(self, choice_type="", text="", choices=[  ], nxt=""):
        self.choice_type = choice_type
        self.text = text
        self.choices = choices
        self.nxt = nxt

    def print_story(self):
        for char in self.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print()

    def get_choice(self):
        if self.choice_type == "yesno":
            choice = choices.yesno_choice().get_choice()
            if choice == True:
                return 0
            else:
                return 1
        if self.choice_type == "list":
            return choices.list_choice(self.choices).get_choice()
        if self.choice_type == "txt":
            os.system("pause")

    def exec(self):
        self.print_story()
        choice_nr = self.get_choice()
        if self.choice_type == "list":
            self.choices[choice_nr].run_path()
        elif self.choice_type == "yesno":
            story.continue_path(self.choices[choice_nr])
        elif self.choice_type == "txt":
            story.continue_path(self.nxt)
