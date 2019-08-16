from game.classes.point import point
from game.classes import choices

# docs for "point" class:
# - text = The story being displayed, before making a choice.
# - choice_type = "list" or "yesno"
# - choices
#    (if yesno type:) [ yes, no ] = The names of the next places
#    (if list type:) [  ]

MSG = {
    # wake up
    "wakeup": """Morning sleepy...

Ouch, damn. Yeh, there must have been an update overnight.

They said that your new chip could burn from time to time...This is a really bad headache. 

Are you sure you want to go in to Code?""",
    # not going to Code will lead to the beginning
    "not-going": "test",
    # going to code will pop some text
    "going": """This was a bad decision! 

You know bed would have been better. But I respect your work ethic. 

But look...

What the hell are they doing? 

...Touching heads, weird. That is soooooo Berlin…""",
    # Take the elevator or stairs
    "stairs-or-elevator": """Shall I enter the elevator?

Don't want to be around this weird...head...touching people.

Anyway, stairs will give me more space...

It's up to you:  """,
}

OUTSIDE = {
    "intro": point(text=MSG["wakeup"], choice_type="yesno", choices=[ "outside_going", "outside_not-going" ]),
    "not-going": point(text=MSG["not-going"], choice_type="list", choices=[
        choices.sub_choice(name="type restart", cmds=["restart","start over"], next_place="outside_intro"),
    ]),
    "going": point(text=MSG["going"], choice_type="txt", nxt="outside_stairs-or-elevator"),
    "stairs-or-elevator": point(text="stairs-or-elevator", choice_type="list", choices=[
        choices.sub_choice(name="1. Elevator", cmds=["elevator", "1", "one"], next_place="outside_place-a"),
        choices.sub_choice(name="go to b", cmds=["go b", "b"], next_place="place-b"),
        choices.sub_choice(name="go to c", cmds=["go c", "c"], next_place="place-c"),
    ]),

    "someplace": point(text="...", choice_type="list", choices=[
        choices.sub_choice(name="go to a", cmds=["go a", "a"], next_place="outside_place-a"),
        choices.sub_choice(name="go to b", cmds=["go b", "b"], next_place="place-b"),
        choices.sub_choice(name="go to c", cmds=["go c", "c"], next_place="place-c"),
    ]),
}
