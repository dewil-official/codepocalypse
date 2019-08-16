from lib.classes import point
from lib.classes import choices

# docs for "point" class:
# - text = The story being displayed, before making a choice.
# - choice_type = "list" or "yesno"
# - choices
#    (if yesno type:) [ yes, no ] = The names of the next places
#    (if list type:) [  ]

OUTSIDE = {
    "intro": point(text="...", choice_type="yesno", choices=[ "outside_going", "outside_not-going" ]),
    "someplace": point(text="...", choice_type="list", choices=[
        sub_choice(name="go to a", cmds=["go a", "a"], next_place="place-a"),
        sub_choice(name="go to b", cmds=["go b", "b"], next_place="place-b"),
        sub_choice(name="go to c", cmds=["go c", "c"], next_place="place-c"),
    ]),
}
