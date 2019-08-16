from game.classes.point import point
from game.classes import choices

# docs for "point" class:
# - text = The story being displayed, before making a choice.
# - choice_type = "list" or "yesno"
# - choices
#    (if yesno type:) [ yes, no ] = The names of the next places
#    (if list type:) [  ]

MSG = {
    "intro": "You wake up.."
}

OUTSIDE = {
    "intro": point(text=MSG["intro"], choice_type="yesno", choices=[ "outside_going", "outside_not-going" ]),
    "someplace": point(text="...", choice_type="list", choices=[
        choices.sub_choice(name="go to a", cmds=["go a", "a"], next_place="place-a"),
        choices.sub_choice(name="go to b", cmds=["go b", "b"], next_place="place-b"),
        choices.sub_choice(name="go to c", cmds=["go c", "c"], next_place="place-c"),
    ]),
}
