from game.classes.point import point
from game.classes import choices

MSG = {
    "": ""
}

UPSTAIRS = {
    "intro": point(text=MSG["wakeup"], choice_type="yesno", choices=[ "outside_going", "outside_not-going" ]),
    "not-going": point(text=MSG["not-going"], choice_type="list", choices=[
        choices.sub_choice(name="type restart", cmds=["restart","start over"], next_place="outside_intro"),
    ]),
}