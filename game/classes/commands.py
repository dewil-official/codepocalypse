class command:
    name = ""
    aliases = []

    def isChoice(self, str):
        if str in self.aliases:
            return True
        else:
            return False

class yes(command):
    name = "yes"
    aliases = [
        "yes",
        "y",
        "yeah",
        "sure",
        "yee",
        "yees",
    ]

class no(command):
    name = "no"
    aliases = [
        "no",
        "n",
        "no way"
        "",
    ]

# These commands are always available:
class help(command):
    name = "help"
    aliases = [
        "help",
        "h",
        "choices",
        "what",
        "why",
        "no idea",
    ]

    def showHelp(self, cmd_list=[ command() ]):
        print("Right now, you could do the following:")
        for cmd in cmd_list:
            print(f"- {cmd.name}")
        print("")
