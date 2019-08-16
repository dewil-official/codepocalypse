import choices

# "point" = A specific point in the story
class point:

    text = ""
    choices = [ choices.choice(), ]

    def __init__(self, choice_type="", text="", choices=[  ]):
        self.choice_type = choice_type
        self.text = text
        
        self.print_story()
        
        choice_nr = self.get_choice()

        self.choices[choice_nr].run_path()

    
    def print_story(self):
        for char in self.text:
            print(char, end="")
        print()

    def get_choice(self):
        if self.choice_type == "yesno":
            choice = choices.yesno_choice()
            if choice == True:
                return 0
            else:
                return 1
        if self.choice_type == "list":
            return choices.list_choice(self.choices)

    # points of continuation
