from game.classes import commands
from game import story

class choice:
    options = [ commands.command() ]

    def print_options(self):
        str_options = " / ".join(cmd.name for cmd in self.options)
        str_options = f"({str_options})"
        print(str_options)

    def get_choice(self):
        pass

class yesno_choice(choice):
    options = [commands.yes(), commands.no()]

    def get_choice(self):
        self.print_options()
        while True:
            usr_input = strip_input(input("> "))
            if commands.help().isChoice(usr_input):
                commands.help().showHelp(self.options)
                continue
            if self.options[0].isChoice(usr_input):
                return True
            elif self.options[1].isChoice(usr_input):
                return False
            else:
                print("Invalid input. Try 'help' for a list of choices!")
                continue

# The list_choice() contains a list of sub_choice() objects.

class sub_choice():
    # cmds is a list of strings: all the possible aliases
    def __init__(self, name="", cmds=["",""], next_place=""):
        self.name = name
        self.cmds = cmds
        self.next_place = next_place
    
    def is_choice(self, check_str):
        for alias in self.cmds:
            if alias == check_str:
                return True
        else:
            return False

    def run_path(self):
        story.continue_path(self.next_place)

class list_choice(choice):
    def __init__(self, choices=[ sub_choice() ]):
        self.options = choices
    
    def get_choice(self):
        self.print_options()
        while True:
            usr_input = strip_input(input("> "))
            if commands.help().isChoice(usr_input):
                commands.help().showHelp(self.options)
                continue
            for op in self.options:
                if op.is_choice(usr_input):
                    return self.options.index(op)
            else:
                print("Invalid input. Try 'help' for a list of choices!")
                continue

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz 12"
def strip_input(str_input):
    str_input = str_input.lower()
    str_output = ""
    for char in str_input:
        if char in ALLOWED_CHARS:
            str_output += char
    return str_output
