import os

from game.places import outside
from game.places import downstairs
from game.places import upstairs
from game.classes import choices
from game.classes import point

# The pathname should look like: place_point
# place being the filename in /places
# point being the actual point in story
def continue_path(pathname):
    os.system("cls")
    if pathname == "end_game":
        exit()
    path = pathname.split("_")
    if path[0] == "outside":
        outside.OUTSIDE[path[1]].exec()
    elif path[0] == "downstairs":
        downstairs.DOWNSTAIRS[path[1]].exec()
    elif path[0] == "upstairs":
        upstairs.UPSTAIRS[path[1]].exec()
