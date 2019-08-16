from game.classes.point import point
from game.classes import choices

# docs for "point" class:
# - text = The story being displayed, before making a choice.
# - choice_type = "list" or "yesno"
# - choices
#    (if yesno type:) [ yes, no ] = The names of the next places
#    (if list type:) [  ]

MSG = {
    # Take the elevator or stairs
    "stairs-or-elevator": """Shall I enter the elevator?

Don't want to be around this weird...head...touching people.

Anyway, stairs will give me more space...

It's up to you:  """,
    "elevator": """Ahh yes, sweet peace. A quiet Elevator.

    // the elevator shudders, and drops suddenly

    Don’t be so scared of a little exercise. It won’t kill you...
"""
}

DOWNSTAIRS = {
    "stairs-or-elevator": point(text=MSG["stairs-or-elevator"], choice_type="list", choices=[
        choices.sub_choice(name="1. Elevator", cmds=["elevator", "1", "one"], next_place="outside_elevator"),
        choices.sub_choice(name="2. Stairs", cmds=["stairs", "2" "two"], next_place="downstairs_stairs"),
    ]),
    "elevator": point(text=MSG["elevator"], choice_type="txt" nxt="end_game"),
    "stairs": point(text=MSG["stairs", choice_type="txt" nxt="downstairs_"]),
    "someplace": point(text="...", choice_type="list", choices=[
        choices.sub_choice(name="go to a", cmds=["go a", "a"], next_place="outside_place-a"),
        choices.sub_choice(name="go to b", cmds=["go b", "b"], next_place="place-b"),
        choices.sub_choice(name="go to c", cmds=["go c", "c"], next_place="place-c"),
    ]),
}
