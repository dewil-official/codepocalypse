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
    "to-the-toilet": """As you run, you notice little droplets of blood. It’s everywhere..
Think. Think. Touching heads. Fighting. What?! You see some students standing,
calm again, surrounding a face you recognise but don’t know.

Surely you need to help. Or do you?""",
    "help-infect": """You help and end up getting attacked.
And at once a beautiful peace overcomes you.

Who else can you help? Everyone deserves this peace…""",
    "hide": """You turn and run. Down the stairs and you
see Frank. You instant reaction is to fly forward with
fists. Desperate fists. But he knows you’re safe. 

“Stop! Stop! I’m not infected. Stop!”

You hear these words and take a step back, cautious.
You can see the fear in his eyes and feel comfort knowing
you are not alone.""",
    "frank-finds":"""Frank Explains:

“This is in the chip. It’s a virus. Just trust me.
We don’t have time to explain this. Just follow me,
I need your help. I can’t do this by myself. Just come!”

Do you trust Frank?""",
    "not-believe": """You sprint in the opposite direction,
checking behind to see if Frank is following you.
He’s not. He stands there watching you, arms stretched
out with fear in his face. But it’s too late. They have you.
And at once, you find peace…""",
    "trust-frank": """You follow frank down stairs to the
basement. It;s quiet and theres no blood. On the
way he explains that together, both of you will
try to reprogram the chips or destroy the program.
But he makes very certain that you know the consequences.

If we cannot reprogram the chip then there wont be
enough time to destroy the program. But if we destroy
the program we will kill everyone who is infected.

What do you choose? Destroy or Reprogram?""",
    "reprogram": """Under the instruction of Frank you do
what you can. But his instructions are alien to you.

Far too advanced. You cannot keep up and now He too is
engulfed by fear. He stops and looks at you. 

'We do not have time! they crash into the room. Flashing violence. And you are now one of them.'
""",
    "destroy": """As soon as you both begin to alter the program,
it fights back. You cannot delete anything. The code is
literally fighting back. And a rumble is coming. People
are running down the stairs. They crash through the door
and at once you are surrounded in a fire of chaos then you
too… You too have joined the great peace."""
}

UPSTAIRS = {
    "join-conversation": point(text=MSG["join-conversation"], choice_type="txt", nxt="upstairs_keep-going"),
    "keep-going": point(text=MSG["keep-going"], choice_type="list", choices=[
        choices.sub_choice(name="cola", cmds=[ "cola", "fritz","fritz cola"], next_place="upstairs_drink"),
        choices.sub_choice(name="mate", cmds=["mate", "club","club mate"], next_place="upstairs_drink"),
    ]),
    "drink": point(text=MSG["drink"], choice_type="txt", nxt="upstairs_to-the-toilet"),
    "to-the-toilet": point(text=MSG["to-the-toilet"], choice_type="list", choices=[
        choices.sub_choice(name="infect", cmds=["infect", "help infect"], next_place="upstairs_help-infect"),
        choices.sub_choice(name="hide", cmds=["hide","run","go away"], next_place="upstairs_hide"),
    ]),
    "help-infect":point(text=MSG["help-infect"], choice_type="txt", nxt="upstairs_end-game"),
    "hide":point(text=MSG["hide"], choice_type="txt", nxt="upstairs_frank-finds"),
    "frank-finds": point(text=MSG["frank-finds"], choice_type="list", choices=[
        choices.sub_choice(name="trust", cmds=["trust", "trust him", "trust frank"], next_place="upstairs_not-believe"),
        choices.sub_choice(name="nope", cmds=["nope","dont trust", "no"], next_place="upstairs_trust-frank"),
    ]),
    "not-believe": point(text=MSG["not-believe"], choice_type="txt", nxt="upstairs_end-game"),
    "trust-frank": point(text=MSG["trust-frank"], choice_type="list", choices=[
        choices.sub_choice(name="destroy", cmds=["destroy", "kill", "die"], next_place="upstairs_destroy"),
        choices.sub_choice(name="reprogram", cmds=["reprogram", "recode", "code"], next_place="upstairs_reprogram"),
    ]),
    "destroy":point(text=MSG["destroy"], choice_type="txt", nxt="end-game"),
    "reprogram":point(text=MSG["reprogram"], choice_type="txt", nxt="end-game"),
}
