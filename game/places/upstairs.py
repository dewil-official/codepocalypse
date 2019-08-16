from game.classes.point import point
from game.classes import choices

MSG = {
    "join-conversation": """And just like magic you strolled right up to them
and asked what they’re talking about. Brave.
They pause for a second. Taken aback then Thomas begins:

You’re with Neuralink right? Yeh? Some of our students were
working on an app to supplement the Neuralink platform and
aid in digital transactions. But keep this on the down low.

It’s a little bugged… Anyway, Adelina and I need to go.""",
    "keep-going": """Time for a drink, see if you can help this damn headache.
The kitchen area is weirdly quiet, but people are doing that weird head
touch nonsense again. Weird… Anyway, what do you want? 

Fritz Cola or Club-Mate?""",
    "drink": """You take your drink and it tells you that you’ve bought 10?!
    
What the hell. Suddenly you hear a thud and a shout you turn around and
Adelina is attacking someone. You dont know who but it is vicious. And
Thomas, yes Thomas is also stamping rapidly at the stomach of this student.

Once the body goes limp, Adelina and Thomas, emotionless and calm, kneel down
and almost peacefully touch their foreheads gently on that of the wounded student.

You run.""",
}

UPSTAIRS = {
    "join-conversation": point(text=MSG["join-conversation"], choice_type="txt", nxt="keep-going"),
    "keep-going": point(text=MSG["keep-going"], choice_type="list", choices=[
        choices.sub_choice(name="cola", cmds=["fritz","fritz cola"], next_place="drink"),
        choices.sub_choice(name="mate", cmds=["club","club mate"], next_place="drink"),
    ]),
    "drink": "",
}