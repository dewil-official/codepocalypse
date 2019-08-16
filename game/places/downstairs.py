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
    # elevator
    "elevator": """Ahh yes, sweet peace. A quiet Elevator.

    // the elevator shudders, and drops suddenly

    Don’t be so scared of a little exercise. It won’t kill you...
""",
    # stairs
    "stairs": """// Walking up the stairs you hear an argument.

// as you get closer you see it is Adelina and Thomas

These stairs are far too much effort, and above you there's an argument. 

THANK YOU PEOPLE, this is EXACTLY what my headache needs right now...At least do it somewhere else.

Oh wait no...It’s Thomas and Adelina, they can do what they want...

but what they're saying is weird: “Dangerous”, “Reckless”, “like a virus”...

...Do you care enough to ask what they’re talking about?
"""
}

DOWNSTAIRS = {
    "stairs-or-elevator": point(text=MSG["stairs-or-elevator"], choice_type="list", choices=[
        choices.sub_choice(name="1. Elevator", cmds=["elevator", "1", "one"], next_place="outside_elevator"),
        choices.sub_choice(name="2. Stairs", cmds=["stairs", "2" "two"], next_place="downstairs_stairs"),
    ]),
    "elevator": point(text=MSG["elevator"], choice_type="txt", nxt="end_game"),
    "stairs": point(text=MSG["stairs"], choice_type="txt", nxt="upstairs"),
}